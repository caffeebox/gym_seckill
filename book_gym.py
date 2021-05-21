import requests
from config import opts_init
from utils import get_session, time_visual, time_enable, cookie_to_dict
import time


class Gym_Book():
    def __init__(self):
        self.opts = opts_init()
        self.session = get_session()

    def order_info(self):
        opened_id = self.open_id()
        query_list = set(self.opts.order_info_l) & set(opened_id)
        fill_list = set(self.opts.order_info_l) - set(opened_id)
        gym_time = {}
        for changguan_id in query_list:
            resp = self.get_idgym(changguan_id)
            gym_time.update({changguan_id: resp})
            # time.sleep(0.1s)
        time_visual(gym_time)
        print('These gym_id cannot be ordered in current date: ', fill_list)

    def open_id(self):
        url = 'http://yy-tky.nnu.edu.cn/inc/ajax/get/getChangguan?'
        payload = {
            'page_size': 0, 'page': 1, 'pagecount': 2, 'listcount': 0, 'isWeb': 1,
            'url': 'http://yy-tky.nnu.edu.cn/wap/list',
            'changguan_xiaoqu': "仙林校区",
            'changguan_weizhi': '室内',
            'changguan_view': 1,
            'changguan_type': self.opts.category,
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

    def get_idgym(self, id):
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
        opened_id = self.open_id()
        query_list = set(self.opts.order_info_l) & set(opened_id)
        for changguan_id in query_list:
            resp = self.get_idgym(changguan_id)
            enable_l = time_enable(resp)
            if set(self.opts.time_s) <= set(enable_l):
                self.order_place(changguan_id)
                break

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


gym = Gym_Book()
gym.order_info()
# gym.seckill()