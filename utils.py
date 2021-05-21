import requests
from config import opts_init
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns

opts = opts_init()

def get_session():
    '''初始化session head和cookie'''
    s = requests.Session()
    s.headers = {
        'User-Agent': opts.user_agent,
        'Connection': 'keep-alive',
        'Host': 'yy-tky.nnu.edu.cn',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    cookie_dict = cookie_to_dict(opts.cookie)
    s.cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
    return s

def cookie_to_dict(cookie):
    ''' 将字符串转为字典 '''
    cookie_dict = {}
    for item in cookie.split(';'):
        name, value = item.strip().split('=', 1)
        cookie_dict[name] = value
    return cookie_dict

def time_visual(gym_time, fill_list):
    ''' 红色(值为0)表示被预定，白色为数据缺失，只有绿色区域(值为1)能够预约 '''
    id_index, data_time = [], []
    for gym_id, resp in gym_time.items():
        soup = BeautifulSoup(resp.get('data').get('time'), 'lxml')
        enable, time_col = [], []
        for item in soup.find_all('input'):
            time_dict = item.attrs
            time_col.append(time_dict.get('value'))
            enable.append(int('disabled' not in time_dict))
        data_time.append(pd.Series(enable, index=time_col))
        if gym_id in opts.gym_id2name.get(opts.category):
            id_index.append(opts.gym_id2name.get(opts.category).get(gym_id))
        else:
            id_index.append(gym_id)
    s = pd.DataFrame(data_time, index=id_index)
    plt.figure(0)
    plt.title(f'{opts.category} on {opts.date}', y=-0.14)
    text = f'No. {fill_list} are not open at the current time.'
    if fill_list:
        plt.text(0, 0 ,text, va='bottom', wrap=True)
    my_color = LinearSegmentedColormap.from_list('', ['red', 'green'])
    sns.heatmap(s, cbar=False, cmap=my_color, linewidths=1, annot=True, center=0.4, yticklabels=True)
    plt.show()

def time_enable(resp):
    ''' 返回可以预约的时间 '''
    soup = BeautifulSoup(resp.get('data').get('time'), 'lxml')
    time_enable_l = []
    for item in soup.find_all('input'):
        time_dict = item.attrs
        if 'disabled' not in time_dict:
            time_enable_l.append(int(time_dict.get('value')))
    return time_enable_l
