# 解析成绩html

from bs4 import BeautifulSoup
import re

findtd = re.compile(r'<td.*?>(.*?)</td>', re.S)
findlabel = re.compile(r'<label>(.*?)<label>', re.S)
findjidian = re.compile(r'<div.*?平均学分绩点(.*?)</div>', re.S)

def get_jidian(htmltext):   # 返回累计绩点
    soup = BeautifulSoup(htmltext[0], "html.parser")

    jidian = re.findall(findjidian, str(soup))[0]
    jidian = jidian.replace('\r', '')
    jidian = jidian.replace('\n', '')
    jidian = jidian.replace(' ', '')                #获得绩点
    return jidian

def get_Data_fromGrade(htmltext):   # 返回datalist学期列表
    datalist = []
    item_datalist = []  # 一个学期的
    for i in range(0, len(htmltext)):
        soup = BeautifulSoup(htmltext[i], "html.parser")
        for item in soup.find_all('tr'):                 # 课程
            data_one_item = []  # 一个课程信息
            item = str(item)
            # print(item)
            td = re.findall(findtd, item)
            for td_one in td:
                td_one = re.sub('<label.*?>', '', td_one)
                td_one = td_one.replace('\n', '')
                td_one = td_one.replace('\r', '')
                td_one = re.sub(r'/', '', td_one)
                td_one = re.sub(' ', '', td_one)
                td_one = re.sub('<label>', '', td_one)
                data_one_item.append(td_one)
            item_datalist.append(data_one_item)
        if not item_datalist[0]:
            del item_datalist[0]
        datalist.append(item_datalist)
        item_datalist = []

    return datalist
#######################################################################################
#  平均学分绩点=∑（课程学分×课程绩点）/∑（课程学分）
# ['201910534', '军事理论', '11通识教育必修课', '2.4000', '1.0', '85', '69', 'A:30,C:70', '74', '不允许报名', '已公布', '']]]
def get_jidian_all_item(datalist):
    datalist_jidian = []
    for one_item in datalist:
        jidian_one_item = 0
        finzi = 0
        finmu = 0

        for one_class in one_item:
            if one_class[3] != '' :             # 出分的
                finzi = (float(one_class[4]) * float(one_class[3])) + finzi
                finmu = finmu + float(one_class[4])
                # print(finzi, finmu)

        jidian_one_item = finzi / finmu
        datalist_jidian.append(jidian_one_item)
    return datalist_jidian

if __name__ == '__main__':
    pass




    # print(htmltext)
    #     htmltext = '''
    #     <tr class="alter">
    # <td>
    #                 202018018
    # </td>
    # <td>
    #                 可再生能源与低碳社会
    #             </td>
    # <td>
    #                 公选课
    #             </td>
    # <td>
    #                 4.8000
    #             </td>
    # <td>
    #                 1.0
    #             </td>
    # <td>
    # </td>
    # <td>
    # </td>
    # <td>
    #                 C:100
    #             </td>
    # <td>
    #                 98
    #             </td>
    # <td rowno="0">
    # <label style="color: Gray">不允许报名</label>
    # </td>
    # <td>
    # <label>
    #                         已公布
    #                     </label>
    # </td>
    # <td>
    # </td>
    # </tr>
    # '''