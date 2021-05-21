import argparse


#----- 信息保密，请替换自己的cookie和ua ------------
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/333333 MicroMessenger/8.0.4(0x1800042c) NetType/WIFI Language/zh_CN'
cookie = 'ASPSESSIONIDCCQDBRCD=HHFmMACCAIACBBBEFPBNBMAE; myopenid=orZpA5%5Fc7wOCH8VxtV9PgcQ2IW8E; njurst=1.0.1; ifrmsrc=%2Fundefined; njurst=1.0.1; casuid=183333333; casuser=%25u3333%25u3333%25u3333'
badminton_id2name = {16:'1F1N', 17:'1F2N', 18:'1F3N', 19:'1F4N', 20:'1F5N', 21:'1F6N', 22:'1F7N', 23:'1F8N',
                    67:'5F1N', 68:'5F2N', 69:'5F3N', 70:'5F4N', 71:'5F5N', 72:'5F6N', 73:'5F7N', 74:'5F8N'}
pingpang_id2name = {26:'1F1N', 27:'1F2N', 28:'1F3N', 38:'1F7N', 39:'1F8N', 40:'1F9N', 41:'1F10N', 42:'1F11N',
                    43:'1F12N', 44:'1F13N', 45:'1F14N', 46:'1F15N', 47:'1F16N', 48:'1F17N', 49:'1F18N', 50:'1F19N',
                    51:'1F20N', 52:'1F21N', 53:'1F22N', 54:'1F23N', 55:'1F24N', 56:'1F25N', 57:'1F26N', 58:'1F27N', 59:'1F28N', 60:'1F29N'}
dance = {25:'1F_room', 77:'5F_room', 170:'2F_hall', 172:'4F_hall', 173:'5F_hall'}
swim = {}
gym_id2name = {'badminton': badminton_id2name, 'pingpang': pingpang_id2name, 'dance': dance, 'swim': swim}
query_d = {
    'badminton': list(range(16, 24)) + list(range(67, 75)),
    'pingpang': list(range(38, 61)) + list(range(26, 29)),
    'swim': [65,],
    'dance': [25, 77, 170, 172, 173],
}

def opts_init():
    ''' 初始化参数 '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, default='query', help='query/order')
    parser.add_argument('--date', type=str, default='2021-05-23')
    parser.add_argument('--category', type=str, default='badminton', help='badminton/pingpang/swim/dance')
    parser.add_argument('--query_l', type=str, default='default', help='custom/default')
    parser.add_argument('--custom_l', type=list, default=[74,70,73,72,69,71,68,67], help='used when custom selected')

    parser.add_argument('--time_s', type=list, default=[19, 20])
    parser.add_argument('--price', type=int, default=30, help='注意价格')

    parser.add_argument('--uid', type=str, default='183333333')
    parser.add_argument('--name', type=str, default='XXX')
    parser.add_argument('--ph', type=str, default='13333333333')
    parser.add_argument('--user_agent', type=str, default=user_agent)
    parser.add_argument('--cookie', type=str, default=cookie)
    parser.add_argument('--gym_id2name', type=dict, default=gym_id2name)
    opts = parser.parse_args()
    return opts

