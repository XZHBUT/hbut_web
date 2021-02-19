from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re


def double_role_ornot(htmltext):  # 判断是否双角色
    temp = re.compile('<a data-toggle="dropdown" class="dropdown-toggle" href="#" title="切换角色">')
    if temp.search(htmltext):
        return True


def login_to_hbutedu(user):  # user = {'username': 账号, 'password': 密码}
    # option = webdriver.ChromeOptions()
    # option.set_headless()
    # driver = webdriver.Chrome(chrome_options=option)
    driver = webdriver.Chrome()
    # driver.get('https://www.hbut.edu.cn/')
    # driver.find_element_by_link_text('学生').click()
    driver.get('http://portal.hbut.edu.cn/')
    print("登录地址：", driver.current_url)
    driver.find_element_by_id('username').send_keys(user['username'])
    driver.find_element_by_id('password').send_keys(user['password'])
    driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td[2]/table/tbody/tr[5]/td[4]/img[1]').click()
    print("登录成功")
    if double_role_ornot(driver.page_source):
        driver.find_element_by_class_name('dropdown-toggle').click()
        driver.find_element_by_link_text('学生').click()
        time.sleep(1)
    # driver.find_element_by_link_text('教学系统').click()
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[8]/div[1]/div/div/a').click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    print("教务系统切换成功：", driver.current_url)
    return driver

#################################################################################
def get_student_grade(driver): # 驱动   返回html列表 一个学期一格
    htmltext = []
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/table/tbody/tr/td/div/ul/li[5]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/table/tbody/tr/td/div/ul/li[5]/ul/li[2]/a').click()
    time.sleep(2)
    driver.switch_to.frame('_mainFrame')
    driver.find_element_by_id('SemesterName').click()
    time.sleep(1)
    # print(driver.page_source)
    # quit()
    handle = driver.current_window_handle
    itemnuber = get_student_grade_find_select(driver.page_source)  # 返回学期数
    # print(itemnuber)
    for i in range(1, itemnuber+1):
        driver.find_element_by_xpath('//*[@id="SemesterName"]/option[%d]' % i).click()
        time.sleep(1)
        # driver.switch_to.window(handle)
        # time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.switch_to.frame('_mainFrame')
        htmltext.append(driver.page_source)
    print("学生成绩单html爬取成功")
    return htmltext


def get_student_grade_find_select(htmltext): # 返回学期数
    soup = BeautifulSoup(htmltext, "html.parser")
    itemnumber = soup.find_all('option')
    return len(itemnumber)

########################################################################

# def get_class_schedule(driver):  # 驱动 学院 班级
#     time.sleep(1)
#     driver.find_element_by_xpath('//*[@id="PanelBar"]/li[2]/a').click()
#     time.sleep(1)
#     driver.find_element_by_xpath('//*[@id="PanelBar"]/li[2]/ul/li[1]/a').click()
#     time.sleep(5)
#     driver.find_element_by_link_text('计算机学院').click()
#     pass
#
# def get_class_schedule_find_shoole_address():

if __name__ == '__main__':
    user = {'username': '1910311210', 'password': '191017'}
    driver = login_to_hbutedu(user)

    # print(htmltext)

    # htmlfile = open('.\\HBUTedu.html', 'w', encoding='utf-8')
    # htmlfile.write(htmltext)
    # htmlfile.close()
