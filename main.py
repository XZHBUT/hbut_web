import analysis_grade as ag
import analysus_class_schedule as acs
import HBUT_Login as lo
import analysis_user_information as ui
import _pyinstaller_hooks_contrib

# user = {'username': '1910311318', 'password': '250023'}
# driver = lo.login_to_hbutedu(user)
# htmltext = lo.get_student_grade(driver)
# # print(ag.get_Data_fromGrade(htmltext))
# print(ag.get_jidian(htmltext[0]))
# print(ag.get_Data_fromGrade(htmltext))
username = input('输入学号:')
password = input('官网信息门户密码（身份证后六位）:')
user = {'username': username, 'password': password}

htmltext = lo.get_class_my_schedule(user)           # 课表    元素为['大学物理(一)-2', '罗山梦黛-主讲', '2-403', '1237891011125(上课周)', 1(星期几), 1(第几节)], ['大学英语-3分级教学时段', '具体安排另行通知', '教室5', '123456789101112131415', 2, 1]...
a = acs.get_Data_formschedule(htmltext)
print('课表：')
print(a)

htmltext = lo.get_student_grade(user)               #从开学到现在所有成绩 第一个为当前学期以此类推    [全部[学期['201920310', '大学语文', '11通识教育必修课', '1.8000', '1.5', '88', '54', 'A:40,C:60', '68', '不允许报名', '已公布', ''....]]]
datalist = ag.get_Data_fromGrade(htmltext)
print('各科目成绩')
print(datalist)
print('历年学期绩点')
print(ag.get_jidian_all_item(datalist))             # 每学期绩点  [(当前学期)3.6108991825613077, 3.8804953560371516, 3.501932367149758]

htmltext = lo.get_student_grade(user)
print('综合绩点')
print(ag.get_jidian(htmltext))                                     # 综合绩点


htmltext = lo.get_user_information(user)            # 个人信息 # 班级 学号 姓名 身份证号 性别 民族 所属学院 专业名称 学制 政治面貌 出生日期 入校日期 离校日期
print('身份信息')
print(ui.get_Data_from_information(htmltext))
