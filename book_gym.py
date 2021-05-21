from config import opts_init
from utils import get_session, time_visual, time_enable, cookie_to_dict
import time


class Gym_Book():
    def __init__(self):
        self.opts = opts_init()
        self.session = get_session()
        self.cate_d = {'pingpang':'乒乓球', 'badminton':'羽毛球', 'swim':'游泳', 'dance':'舞蹈'}
        self.query_d = {
            'badminton': list(range(16, 24)) + list(range(67, 75)),
            'pingpang': list(range(38, 61)) + list(range(26, 29)),
            'swim': [65, ],
            'dance': [25, 77, 170, 172, 173],
        }

    def order_info(self):
        ''' 查询并显示空余场地 '''
        query_list, fill_list = self._query_list()
        gym_time = {}
        for changguan_id in query_list:
            resp = self._get_idgym(changguan_id)
            gym_time.update({changguan_id: resp})
        time_visual(gym_time, fill_list)

    def _query_list(self):
        ''' 分别返回能够预约与不能预约的场馆id '''
        if self.opts.query_l == 'default':
            query_l = self.query_d.get(self.opts.category)
        else:
            query_l = self.opts.custom_l
        opened_id = self._query_id()
        query_list = set(query_l) & set(opened_id)
        fill_list = set(query_l) - set(opened_id)
        return query_list, fill_list

    def _query_id(self):
        ''' 查看开放预定的场地id并返回 '''
        url = 'http://yy-tky.nnu.edu.cn/inc/ajax/get/getChangguan?'
        payload = {
            'page_size': 0, 'page': 1, 'pagecount': 2, 'listcount': 0, 'isWeb': 1,
            'url': 'http://yy-tky.nnu.edu.cn/wap/list',
            'changguan_xiaoqu': "仙林校区",
            'changguan_weizhi': '室内',
            'changguan_view': 1,
            'changguan_type': self.cate_d.get(self.opts.category),
        }
        self.session.headers.update({
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://yy-tky.nnu.edu.cn/wap/list',
        })
        resp = self.session.get(url=url, params=payload)
        if resp.status_code == 200:
            resp_data = resp.json()
            resp_l = resp_data.get('data').get('list')
            displayed_id = [int(a.get('changguan_id')) for a in resp_l]
        else:
            print('something wrong')
        return displayed_id

    def _get_idgym(self, id):
        ''' 获取当前id场馆的信息(可预约时间和价格) '''
        url = 'http://yy-tky.nnu.edu.cn/inc/ajax/get/getChangguanYuyuetime?'
        payload = {
            'page_size': 0, 'page': 1, 'pagecount': 0, 'listcount': 0, 'isWeb': 1,
            'url': f'http://yy-tky.nnu.edu.cn/wap/yuyue?id={id}',
            'changguan': id,
            'riqi': self.opts.date,
            'neibu': 1,
        }
        self.session.headers.update({
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': f'http://yy-tky.nnu.edu.cn/wap/yuyue?id={id}',
        })
        resp = self.session.get(url=url, params=payload)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f'error for the {id}_gym request!')
            exit()

    def seckill(self):
        opened_id = self._query_id()
        query_list = set(self.opts.order_info_l) & set(opened_id)
        for changguan_id in query_list:
            resp = self.get_idgym(changguan_id)
            enable_l = time_enable(resp)
            if set(self.opts.time_s) <= set(enable_l):
                self.order_place(changguan_id)
                return True
        print('No gym on current period.')

    def order_place(self, gym_id):
        url = 'http://yy-tky.nnu.edu.cn/inc/ajax/save/saveYuyue'
        cookie_d = cookie_to_dict(self.opts.cookie)
        cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        payload = [
            ('isWeb', 1), ('API', 'saveYuyue'), ('noSave', 'yuyue_id'), ('back', 'yuyue_id'),
            ('yuyue_desc', ''), ('yuyue_view', -1), ('yuyue_fujiafei', '0.00'), ('yuyue_neibu', 1),
            ('yuyue_riqi', self.opts.date),
            ('yuyue_name', self.opts.name),
            ('yuyue_xuehao', self.opts.uid),
            ('yuyue_hp', self.opts.ph),
            ('yuyue_changguan', gym_id),
            ('yuyue_jine', self.opts.price),
            ('yuyue_openid', cookie_d.get('myopenid')),
            ('yuyue_date', cur_time)
        ]
        time_num = len(self.opts.time_s)
        if time_num not in [1, 2]:
            print('no time choised or beyond two hours')
            exit()
        for i in range(time_num):
            payload.append(('yuyue_time', self.opts.time_s[i]))
        self.session.headers.update({
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://yy-tky.nnu.edu.cn'
        })
        resp = self.session.post(url, data=payload)
        if resp.status_code == 200:
            print(resp.text)
        else:
            print('Place on Order Failed!')

