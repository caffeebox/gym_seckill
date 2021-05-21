from bs4 import BeautifulSoup
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns

# gym_id2name = {0: '场馆0好', 1: '场馆1号', 2: 'test2', 3: 'test3'}
# resp = '{"errCode":"0","errMsg":"","data":{"time":"<div class=\"next2 box\">\t<input name=\"yuyue_time\" id=\"yuyue_time17\" value=\"17\" type=\"checkbox\" disabled=\"disabled\">\t<label for=\"yuyue_time17\"></label><label for=\"yuyue_time17\">17:00</label></div><div class=\"next2 box\">\t<input name=\"yuyue_time\" id=\"yuyue_time18\" value=\"18\" type=\"checkbox\" disabled=\"disabled\">\t<label for=\"yuyue_time18\"></label><label for=\"yuyue_time18\">18:00</label></div><div class=\"next2 box\">\t<input name=\"yuyue_time\" id=\"yuyue_time19\" value=\"19\" type=\"checkbox\" disabled=\"disabled\">\t<label for=\"yuyue_time19\"></label><label for=\"yuyue_time19\">19:00</label></div><div class=\"next2 box\">\t<input name=\"yuyue_time\" id=\"yuyue_time20\" value=\"20\" type=\"checkbox\" disabled=\"disabled\">\t<label for=\"yuyue_time20\"></label><label for=\"yuyue_time20\">20:00</label></div>","jine":"40.00"}}'
# resp_j_16 = {'errCode': '0', 'errMsg': '', 'data': {'time': '<div class="next2 box">\t<input name="yuyue_time" id="yuyue_time17" value="17" type="checkbox" disabled="disabled">\t<label for="yuyue_time17"></label><label for="yuyue_time17">17:00</label></div><div class="next2 box">\t<input name="yuyue_time" id="yuyue_time18" value="18" type="checkbox" disabled="disabled">\t<label for="yuyue_time18"></label><label for="yuyue_time18">18:00</label></div><div class="next2 box">\t<input name="yuyue_time" id="yuyue_time19" value="19" type="checkbox" disabled="disabled">\t<label for="yuyue_time19"></label><label for="yuyue_time19">19:00</label></div><div class="next2 box">\t<input name="yuyue_time" id="yuyue_time20" value="20" type="checkbox" disabled="disabled">\t<label for="yuyue_time20"></label><label for="yuyue_time20">20:00</label></div>', 'jine': '40.00'}}
# resp_j_17 = {'errCode': '0', 'errMsg': '', 'data': {'time': '<div class="next2 box">\t<input name="yuyue_time" id="yuyue_time17" value="17" type="checkbox" disabled="disabled">\t<label for="yuyue_time17"></label><label for="yuyue_time17">17:00</label></div><div class="next2 box">\t<input name="yuyue_time" id="yuyue_time18" value="18" type="checkbox" disabled="disabled">\t<label for="yuyue_time18"></label><label for="yuyue_time18">18:00</label></div><div class="next2 box">\t<input name="yuyue_time" id="yuyue_time19" value="19" type="checkbox" disabled="disabled">\t<label for="yuyue_time19"></label><label for="yuyue_time19">19:00</label></div><div class="next2 box">\t<input name="yuyue_time" id="yuyue_time20" value="20" type="checkbox" disabled="disabled">\t<label for="yuyue_time20"></label><label for="yuyue_time20">20:00</label></div>', 'jine': '40.00'}}
# resp_j_18 = {'errCode': '0', 'errMsg': '', 'data': {'time': '<div class="next2 box">\t<input name="yuyue_time" id="yuyue_time18" value="18" type="checkbox" disabled="disabled">\t<label for="yuyue_time18"></label><label for="yuyue_time18">18:00</label></div><div class="next2 box">\t<input name="yuyue_time" id="yuyue_time19" value="19" type="checkbox" disabled="disabled">\t<label for="yuyue_time19"></label><label for="yuyue_time19">19:00</label></div><div class="next2 box">\t<input name="yuyue_time" id="yuyue_time20" value="20" type="checkbox" disabled="disabled">\t<label for="yuyue_time20"></label><label for="yuyue_time20">20:00</label></div>', 'jine': '40.00'}}
# resp_j_19 = {'errCode': '0', 'errMsg': '', 'data': {'time': '<div class="next2 box">\t<input name="yuyue_time" id="yuyue_time17" value="17" type="checkbox" >\t<label for="yuyue_time17"></label><label for="yuyue_time17">17:00</label></div><div class="next2 box">\t<input name="yuyue_time" id="yuyue_time18" value="18" type="checkbox" disabled="disabled">\t<label for="yuyue_time18"></label><label for="yuyue_time18">18:00</label></div><div class="next2 box">\t<input name="yuyue_time" id="yuyue_time19" value="19" type="checkbox" disabled="disabled">\t<label for="yuyue_time19"></label><label for="yuyue_time19">19:00</label></div><div class="next2 box">\t<input name="yuyue_time" id="yuyue_time20" value="20" type="checkbox" disabled="disabled">\t<label for="yuyue_time20"></label><label for="yuyue_time20">20:00</label></div>', 'jine': '40.00'}}
# resps = [resp_j_16, resp_j_17, resp_j_18, resp_j_19]
# id_index, vsu = [], []
# for i, resp in enumerate(resps):
#     soup = BeautifulSoup(resp.get('data').get('time'), 'lxml')
#     enable, time_col = [], []
#     for item in soup.find_all('input'):
#         time_dict = item.attrs
#         time_col.append(time_dict.get('value'))
#         enable.append(int('disabled' not in time_dict))
#     vsu.append(pd.Series(enable, index=time_col))
#     id_index.append(gym_id2name.get(i))
#
# s = pd.DataFrame(vsu, index=id_index)
# plt.figure(0)
# my_color = LinearSegmentedColormap.from_list('', ['red', 'green'])
# sns.heatmap(s, cbar=False, cmap=my_color, linewidths=1)
# plt.show()

# resp = {'errCode': '0', 'errMsg': '', 'data': {'page_size': '50', 'page': '1', 'pagecount': '1', 'listcount': '8', 'list': [{'changguan_id': '67', 'changguan_no': 'X14-1', 'changguan_xiaoqu': '仙林校区', 'changguan_weizhi': '室内', 'changguan_fujiafei': '0.00', 'changguan_beizhu': '', 'changguan_view': '1', 'changguan_title': '仙林五楼羽毛球馆1号场', 'changguan_type': '羽毛球', 'changguan_pic': '', 'changguan_unit': '片', 'changguan_count': '1', 'changguan_sort': '1', 'changguan_jinemin': '1500', 'changguan_jineminw': '4000'}, {'changguan_id': '68', 'changguan_no': 'X14-2', 'changguan_xiaoqu': '仙林校区', 'changguan_weizhi': '室内', 'changguan_fujiafei': '0.00', 'changguan_beizhu': '', 'changguan_view': '1', 'changguan_title': '仙林五楼羽毛球馆2号场', 'changguan_type': '羽毛球', 'changguan_pic': '', 'changguan_unit': '片', 'changguan_count': '1', 'changguan_sort': '2', 'changguan_jinemin': '1500', 'changguan_jineminw': '4000'}, {'changguan_id': '69', 'changguan_no': 'X14-3', 'changguan_xiaoqu': '仙林校区', 'changguan_weizhi': '室内', 'changguan_fujiafei': '0.00', 'changguan_beizhu': '', 'changguan_view': '1', 'changguan_title': '仙林五楼羽毛球馆3号场', 'changguan_type': '羽毛球', 'changguan_pic': '', 'changguan_unit': '片', 'changguan_count': '1', 'changguan_sort': '3', 'changguan_jinemin': '1500', 'changguan_jineminw': '4000'}, {'changguan_id': '70', 'changguan_no': 'X14-4', 'changguan_xiaoqu': '仙林校区', 'changguan_weizhi': '室内', 'changguan_fujiafei': '0.00', 'changguan_beizhu': '', 'changguan_view': '1', 'changguan_title': '仙林五楼羽毛球馆4号场', 'changguan_type': '羽毛球', 'changguan_pic': '', 'changguan_unit': '片', 'changguan_count': '1', 'changguan_sort': '4', 'changguan_jinemin': '1500', 'changguan_jineminw': '4000'}, {'changguan_id': '71', 'changguan_no': 'X14-5', 'changguan_xiaoqu': '仙林校区', 'changguan_weizhi': '室内', 'changguan_fujiafei': '0.00', 'changguan_beizhu': '', 'changguan_view': '1', 'changguan_title': '仙林五楼羽毛球馆5号场', 'changguan_type': '羽毛球', 'changguan_pic': '', 'changguan_unit': '片', 'changguan_count': '1', 'changguan_sort': '5', 'changguan_jinemin': '1500', 'changguan_jineminw': '4000'}, {'changguan_id': '72', 'changguan_no': 'X14-6', 'changguan_xiaoqu': '仙林校区', 'changguan_weizhi': '室内', 'changguan_fujiafei': '0.00', 'changguan_beizhu': '', 'changguan_view': '1', 'changguan_title': '仙林五楼羽毛球馆6号场', 'changguan_type': '羽毛球', 'changguan_pic': '', 'changguan_unit': '片', 'changguan_count': '1', 'changguan_sort': '6', 'changguan_jinemin': '1500', 'changguan_jineminw': '4000'}, {'changguan_id': '73', 'changguan_no': 'X14-7', 'changguan_xiaoqu': '仙林校区', 'changguan_weizhi': '室内', 'changguan_fujiafei': '0.00', 'changguan_beizhu': '', 'changguan_view': '1', 'changguan_title': '仙林五楼羽毛球馆7号场', 'changguan_type': '羽毛球', 'changguan_pic': '', 'changguan_unit': '片', 'changguan_count': '1', 'changguan_sort': '7', 'changguan_jinemin': '1500', 'changguan_jineminw': '4000'}, {'changguan_id': '74', 'changguan_no': 'X14-8', 'changguan_xiaoqu': '仙林校区', 'changguan_weizhi': '室内', 'changguan_fujiafei': '0.00', 'changguan_beizhu': '', 'changguan_view': '1', 'changguan_title': '仙林五楼羽毛球馆8号场', 'changguan_type': '羽毛球', 'changguan_pic': '', 'changguan_unit': '片', 'changguan_count': '1', 'changguan_sort': '8', 'changguan_jinemin': '1500', 'changguan_jineminw': '4000'}]}}
# resp_l = resp.get('data').get('list')
# result = [int(a.get('changguan_id')) for a in resp_l]
# print(result)

# import time
# cur = time.strftime('%Y-%m-%d+%H:%M:%S', time.localtime())
# print(cur)

# list1 = [3, 2, 5, 6, 1, 4, 7]
# list2 = [1, 3, 5, 6, 2]
# set1 = list(set(list1) & set(list2))
# set1.sort(key=list1.index)
# print(set1)
