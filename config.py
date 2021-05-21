import argparse


user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.4(0x1800042c) NetType/WIFI Language/zh_CN'
cookie = 'ASPSESSIONIDCCQDBRCD=HHFFMACCHIANBBBEFPBNBMAE; myopenid=orZpM5%5FcgwOCH8VxEV9PgcQ2IW8E; njurst=1.0.1; ifrmsrc=%2Fundefined; njurst=1.0.1; casuid=182202001; casuser=%25u9648%25u79D1%25u8F89'
gym_id2name = {16:'1F1N', 17:'1F2N', 18:'1F3N', 19:'1F4N', 20:'1F5N', 21:'1F6N', 22:'1F7N', 23:'1F8N',
               67:'5F1N', 68:'5F2N', 69:'5F3N', 70:'5F4N', 71:'5F5N', 72:'5F6N', 73:'5F7N', 74:'5F8N'}
order_info_d = {
    'badminton': list(range(16, 24)) + list(range(67, 75)),
    'table_tennis': list(range(38, 61)) + list(range(26, 29)),
    'swim': [65,],
    'dance': [25, 77, 170, 172, 173],
    'test': [39, 26]
}

def opts_init():
    ''' 初始化参数 '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--user_agent', type=str, default=user_agent, help='user agent')
    parser.add_argument('--cookie', type=str, default=cookie, help='cookie')
    parser.add_argument('--gym_id2name', type=dict, default=gym_id2name)
    parser.add_argument('--order_info_l', type=list, default=order_info_d.get('test'))
    parser.add_argument('--category', type=str, default='乒乓球', help='羽毛球/乒乓球/游泳/舞蹈/健身')
    parser.add_argument('--time_s', type=list, default=[19, 20])
    parser.add_argument('--price', type=int, default=20, help='注意价格')
    parser.add_argument('--date', type=str, default='2021-05-23')
    parser.add_argument('--uid', type=str, default='182202001')
    parser.add_argument('--name', type=str, default='陈科辉')
    parser.add_argument('--ph', type=str, default='13080645035')
    opts = parser.parse_args()
    return opts

