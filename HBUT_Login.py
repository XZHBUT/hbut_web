import requests
from bs4 import BeautifulSoup
import datetime
import re
import time

def Get_lt(f):  # 获取参数 lt 的函数
    soup = BeautifulSoup(f.content, "lxml")
    once = soup.find('input', {'name': 'lt'})['value']
    return once

def login_to_hbutedu(user):
    url = 'https://sso.hbut.edu.cn:7002/cas/login'
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }
    page = requests.session()
    page.headers = headers
    f = page.get(url)
    lt = Get_lt(f)
    data = {
        'lt': lt,
        '_eventId': 'submit',
        'loginType': '0',
        'username': '{}'.format(user['username']),
        'password': '{}'.format(user['password']),
        'j_digitPicture': '',
    }

    q = page.post(url, data=data, headers=headers)
    soup = BeautifulSoup(q.text, "html.parser")
    if str(soup.find_all('title')[0]) == '<title>湖北工业大学 -- 统一身份认证</title>':
        print('账号密码输入错误或其他问题')
        quit()
    f_edu = page.get('http://run.hbut.edu.cn/Account/sso')
    return page, f_edu

#################################################################################################################################################


def get_student_grade_find_select(user):                                    # 返回学期数  学年列表 （['20201', '20192', '20191']）
    datayear = []
    page, f_edu= login_to_hbutedu(user)
    f = page.get('http://run.hbut.edu.cn/StuGrade/Index')

    soup_temp = BeautifulSoup(f.text, "html.parser")
    soup = BeautifulSoup(f_edu.text, "html.parser")
    itemnumber = soup_temp.find_all('option')
    nowitem = re.findall('<strong>(.*?)</strong>', str(soup))[0]
    if nowitem[8] == '一':
        nowitem = nowitem[0:4] + '1'
    else:
        nowitem = nowitem[0:4] + '2'
    # print(len(itemnumber), int(nowitem))
    datayear.append(nowitem)
    soup = BeautifulSoup(f.text, "html.parser")
    itemnumber = soup.find_all('option')
    # print(len(itemnumber))
    for i in range(1, len(itemnumber)):
        if nowitem[-1] == '1':
            nowitem = str(int(nowitem[0:4]) - 1) + '2'
            datayear.append(nowitem)
        else:
            nowitem = str(int(nowitem) - 1)
            datayear.append(nowitem)  # 学年列表 （['20201', '20192', '20191']）
    return len(itemnumber), datayear


def get_student_grade(user):
    htmltext = []

    itemnuber, datayear = get_student_grade_find_select(user)

    for i in datayear:
        page, f_edu = login_to_hbutedu(user)
        f = page.get('http://run.hbut.edu.cn/StuGrade/Index?SemesterName={}'.format(i))
        htmltext.append(f.text)

    return htmltext

#######################################################################################################################
def get_class_my_schedule(user):
    page, f_edu = login_to_hbutedu(user)
    f_schedule = page.get('http://run.hbut.edu.cn/ArrangeTask/MyselfSchedule')
    return f_schedule.text

#######################################################################################################################

def get_user_information(user):
    page, f_edu = login_to_hbutedu(user)
    f_schedule = page.get('http://run.hbut.edu.cn/T_Student/OwnInfo')
    return f_schedule.text

#######################################################################################################################
if __name__ == '__main__':
    user = {'username': '1910311210', 'password': '191017'}
    print(get_user_information(user))