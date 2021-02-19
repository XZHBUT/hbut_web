from bs4 import BeautifulSoup
import re
import time as sleep
findtd = re.compile(r'<td.*?>(.*?)<br/>(..*?)<br/>(.*?)<br/><br/>', re.S)

find_classname = re.compile(r'>(.*?)<br/>.*?周.*?<br/><br/>', re.S)
find_classname_other = re.compile(r'<br/><br/>(.*?)<br/>', re.S)
find_class_room = re.compile(r'<br/>(.*?)\n*?第',re.S)
find_class_time = re.compile(r'<br/>\n*?(.*?)\n*?<br/><br/>', re.S)


find_teather_ornot = re.compile(r'')
def get_Data_formschedule(htmltext):                # 返回学期列表，元素类似 (课程，老师，地点，时间，星期，节数)['大学物理(一)-2', '罗山梦黛-主讲', '2-403', '123456789101112131415', 1, 1], ['大学英语-3分级教学时段', '具体安排另行通知', '教室5', '第1-15周', 2, 1], ['大学物理(一)-2', '罗山梦黛-主讲', '2-403', '第1-3周第7-12周第5周', 3, 1]
    data_one_item = []
    soup = BeautifulSoup(htmltext, "html.parser")
    classnode = -1
    for row_data in soup.find_all('tr'):
        classnode = classnode + 1
        weekday = 0
        row_data = str(row_data)
        soup_row_data = BeautifulSoup(row_data, "html.parser")
        for td_data in soup_row_data.find_all('td', align="left"):
            weekday = weekday + 1
            data_one_class = []
            if len(re.findall(find_classname, str(td_data))) >0 :
                class_name_first = re.findall(find_classname, str(td_data))[0]
                # print(re.findall(find_classname, str(td_data)))
                class_name_first = class_name_first.replace('\n', '')
                class_name_first = class_name_first.replace('\r', '')
                # print(class_name_first)
                # print(str(td_data))
                class_name_first = class_name_first.replace('(', '\(')
                class_name_first = class_name_first.replace(')', '\)')
                # print(str(td_data))
                # print()
                # print(re.findall(re.compile(r'{}<br/>\D*?<br/>.*?第.*?<br/><br/>'.format(class_name_first), re.S), str(td_data)))
                if len(re.findall(re.compile(r'{}<br/>\D*?<br/>.*?第.*?<br/><br/>'.format(class_name_first), re.S), str(td_data))) == 0:     # 如果没有老师
                    # print(class_name_first)
                    class_name_first = class_name_first.replace('\(', '(')
                    class_name_first = class_name_first.replace('\)', ')')
                    data_one_class.append(class_name_first)
                    data_one_class.append('')
                    room = re.findall(find_class_room, str(td_data))[0].replace('\n', '').replace('\r', '').replace(' ', '')
                    data_one_class.append(room)
                    time = re.findall(find_class_time, str(td_data))[0].replace('\n', '').replace('\r', '').replace(' ', '')
                    # print(str(td_data))
                    time = time.replace(room, '').replace(' ', '')
                    data_one_class.append(time)
                    data_one_class.append(weekday)
                    data_one_class.append(classnode)
                    data_one_item.append(data_one_class)
                    # print(data_one_class)
                else:

                    # print(str(td_data))
                    teather = re.findall(re.compile(r'{}<br/>(.*?)<br/>.*?第.*?<br/><br/>'.format(class_name_first), re.S), str(td_data))[0]
                    teather = teather.replace('\n', '').replace('\r', '').replace(' ', '')
                    class_name_first = class_name_first.replace('\(', '(')
                    class_name_first = class_name_first.replace('\)', ')')
                    data_one_class.append(class_name_first)
                    data_one_class.append(teather)
                    room = re.findall(find_class_room, str(td_data))[0].replace('\n', '').replace('\r', '').replace(' ', '')
                    room = room.replace(teather, '').replace('<br/>', '')
                    data_one_class.append(room)
                    time = re.findall(find_class_time, str(td_data))[0].replace('\n', '').replace('\r', '').replace(' ', '')
                    # print(str(td_data))
                    time = time.replace(room, '').replace(' ', '').replace('<br/>', '').replace(teather, '')
                    data_one_class.append(time)
                    data_one_class.append(weekday)
                    data_one_class.append(classnode)
                    data_one_item.append(data_one_class)
                    # print(data_one_class)
                # print(class_name_first)
                if len(re.findall(find_classname, str(td_data))) >1:
                    data_one_class = []
                    class_name_other = re.findall(find_classname_other, str(td_data))
                    # print(class_name_other)
                    '''
                       JAVA程序设计_上机<br/>
   宗欣露-上机指导<br/>
   6A4-2-3    第8-11周 <br/><br/>
                       '''
                    for class_name_other_one in class_name_other:
                        data_one_class = []
                        class_name_other_one = class_name_other_one.replace('\n', '')
                        class_name_other_one = class_name_other_one.replace('\r', '')
                        class_name_other_one = class_name_other_one.replace('(', '\(')
                        class_name_other_one = class_name_other_one.replace(')', '\)')
                        # print(class_name_other_one)
                        # print(str(td_data))
                        # print(class_name_other_one)
                        teather = re.findall(re.compile(r'{}<br/>(.*?)<br/>'.format(class_name_other_one), re.S),str(td_data))[0]
                        # print(teather)
                        # try:
                        #     teather = re.findall(re.compile(r'{}.*<br/>(.*?)<br/>.*第.*?<br/><br/>'.format(class_name_other_one), re.S), str(td_data))[0]
                        # except IndexError:
                        #     try:
                        #         teather = re.findall(re.compile(r'{}.*<br/>(.*?)<br/>.*第.*?<br/><br/>'.format(class_name_other_one), re.S), str(td_data))[0]
                        #     except IndexError:
                        #         teather = re.findall(re.compile(r'{}.*<br/>(.*?)<br/>.*第.*?<br/><br/>'.format(class_name_other_one), re.S), str(td_data))[0]
                        teather = teather.replace('\n', '').replace('\r', '').replace(' ', '')
                        # print(teather)
                        class_name_other_one = class_name_other_one.replace('\(', '(')
                        class_name_other_one = class_name_other_one.replace('\)', ')')
                        data_one_class.append(class_name_other_one)
                        data_one_class.append(teather)
                        class_name_other_one = class_name_other_one.replace('(', '\(')
                        class_name_other_one = class_name_other_one.replace(')', '\)')
                        if len(re.findall(re.compile(r'<br/><br/>.*{}.*<br/>.*{}.*?<br/>(.*?)第.*?<br/>'.format(class_name_other_one, teather), re.S), str(td_data))) ==1:
                            room = re.findall(re.compile(r'<br/><br/>.*{}.*<br/>.*{}.*?<br/>(.*?)第.*?<br/>'.format(class_name_other_one, teather), re.S), str(td_data))[0].replace('\n', '').replace('\r', '').replace(' ', '')
                            room = room.replace(teather, '').replace('<br/>', '')
                            data_one_class.append(room)
                            time = \
                            re.findall(re.compile(r'<br/>.*?{}(.*?)<br/><br/>'.format(room), re.S), str(td_data))[0].replace('\n', '').replace('\r', '').replace(' ', '')
                            # print(str(td_data))
                            time = time.replace(room, '').replace(' ', '').replace('<br/>', '').replace(teather, '')
                            data_one_class.append(time)
                            data_one_class.append(weekday)
                            data_one_class.append(classnode)
                            data_one_item.append(data_one_class)
                            # print(data_one_class)
                        else:
                            for i_room in re.findall(re.compile(r'<br/><br/>.*{}.*<br/>.*{}.*?<br/>(.*?)第.*?<br/>'.format(class_name_other_one, teather), re.S), str(td_data)):
                                i_room = i_room.replace('\n', '').replace('\r', '').replace(' ', '')
                                data_one_class.append(i_room)
                                time = re.findall(re.compile(r'<br/>.*?{}(.*?)<br/><br/>'.format(i_room), re.S), str(td_data))[0].replace('\n', '').replace('\r', '').replace(' ', '')
                                # print(str(td_data))
                                time = time.replace(i_room, '').replace(' ', '').replace('<br/>', '').replace(teather, '')
                                data_one_class.append(time)
                                data_one_class.append(weekday)
                                data_one_class.append(classnode)
                                data_one_item.append(data_one_class)
                                # print(data_one_class)
                            break
    for i in range(0, len(data_one_item)):
        data_one_item[i][3] = class_time_hanzhi_to_int(data_one_item[i][3])
    return data_one_item

def class_time_hanzhi_to_int(str_s):                    # ('第1-10周第11-12周第5,15,17周') -> 12345678910111251517
    findtime = re.compile(r'第(.*?)周')

    time_str_number = re.findall(findtime, str_s)
    time_class = []
    time = ''
    # print(time_str_number)
    for i in time_str_number:
        time_number = ''
        if i.find('-') != -1:
            a = i.find('-')
            for j in range(int(i[0:a]), int(i[a+1:])+1):
                time_number = time_number + str(j)
            time_class.append(time_number)
        elif i.find(',') != -1:
            time_number = i.replace(',', '')
            time_class.append(time_number)
        else:
            time_class.append(i)
    for i in time_class:
        time = time + i
    return time



a = '''
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Cache-Control" content="no-cache,no-store, must-revalidate" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="0" />
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    <title>课程表安排</title>
    <link href="/favicon.ico" type="image/x-icon" rel="icon"/>
    <link href="/favicon.ico" type="image/x-icon" rel="shortcut icon"/>
    <link type="text/css" href="/Content/Telerik/telerik.common.css" rel="stylesheet"/>
<link type="text/css" href="/Content/Telerik/telerik.office2007.css" rel="stylesheet"/>

    <link href="/Content/default1.css" rel="stylesheet" type="text/css" />
    <script src="/Scripts/jquery-1.6.4.min.js" type="text/javascript"></script>

    <script language="javascript" type="text/javascript">
        //此处放Javascript全局变量
        var rootHref = "/";
        var firstFlag = true;

        $(document).ready(function(){

            //页面出现滚动条但弹窗不出现滚动条
            var frame = self.parent.frames["_mainFrame"];
            if(frame != undefined){
                //设置滚动条
                frame.document.body.style.overflow="auto"
                //最小宽度
                frame.document.body.style.minWidth="805px"
            }

        });
    </script>

    <script src="/Scripts/js_min.js" type="text/javascript"></script>
    <script src="/Content/lhgDialog/lhgdialog.min.js" type="text/javascript"></script>
    <script src="/Scripts/default.js" type="text/javascript"></script>
    <script src="/Scripts/textbox.js" type="text/javascript"></script>
    <script src="/Scripts/linkerManage.js" type="text/javascript"></script>

    <script src="/Scripts/string-ext.js" type="text/javascript"></script>

    <script src="/Scripts/easyUI/jquery.easyui.min.js" type="text/javascript"></script>
    <link href="/Scripts/easyUI/icon.css" rel="stylesheet" type="text/css" />
    <link href="/Scripts/easyUI/default/easyui.css" rel="stylesheet" type="text/css" />



</head>
<body style="background-color: #fff; margin-left: 15px; margin-right: 15px;">
    <div id="action_activity_pane" style="position: absolute; width: 100%; height: 100%;
        display: none;">
    </div>
    <div id="mainContent">

<link href="/Content/TimeSchedule.css" rel="stylesheet" type="text/css" />

<style>
    div#weekSchedule
    {
        text-align:left;
    }
    div#weekSchedule table
    {
        border:0px;
        width:auto;
    }

    div#weekSchedule td
    {
        padding-left:15px;
        padding-bottom:5px;
        word-break:break-all;
        word-wrap:break-word;
        max-width:250px;
        border:0px;
        background:#fff;
        }
</style>

<div>
        <h2 style="padding-bottom:17px;padding-top:17px" align="center">
            <span>19大数据2 2020学年 第一学期 课程表安排</span>
        </h2>
</div>
<div class = "table-Schedule" align="center" style="margin: 0px 0px 0px 10px;" >
    <table>
        <tr>
            <th width="9%"></th>
            <th width="13%">星期一</th>
            <th width="13%">星期二</th>
            <th width="13%">星期三</th>
            <th width="13%">星期四</th>
            <th width="13%">星期五</th>
            <th width="13%">星期六</th>
            <th width="13%">星期日</th>
        </tr>

            <tr>
                    <th>第1-2节</th>
                                <td align="left">
大学物理(一)-2<br />
罗山梦黛-主讲<br />
2-403    第1-3周 第7-12周 第5周<br /><br />
                                </td>
                                <td align="left">
大学英语-3分级教学时段<br />
具体安排另行通知<br />
教室5    第1-15周 <br /><br />
                                </td>
                                <td align="left">
大学物理(一)-2<br />
罗山梦黛-主讲<br />
2-403    第1-3周 第7-12周 第5周<br /><br />
                                </td>
                                <td align="left">
数据结构<br />
吴歆韵-主讲<br />
2-410    第1-3周 第7-12周 <br /><br />
                                </td>
                                <td align="left">
大学英语-3<br />
艾思-主讲<br />
3-104    第1-3周 第7-12周 第5周<br /><br />
                                </td>
                                <td align="left">
兴趣体育选修课-1<br />
中心操场1    第12-14周 <br /><br />
JAVA程序设计_上机<br />
宗欣露-上机指导<br />
6A4-2-3    第8-11周 <br /><br />
大学英语-3分级教学时段<br />
具体安排另行通知<br />
教室5    第15周<br /><br />
                                </td>
                                <td align="left">
                                </td>
            </tr>
            <tr>
                    <th>第3-4节</th>
                                <td align="left">
JAVA程序设计<br />
宗欣露-主讲<br />
3-207    第2-3周 第7-12周 第5周<br /><br />
                                </td>
                                <td align="left">
毛泽东思想和中国特色社会主义理论体系概论<br />
何家华-主讲<br />
2-107    第1-3周 第7-12周 第5,15周<br /><br />
                                </td>
                                <td align="left">
JAVA程序设计<br />
宗欣露-主讲<br />
3-207    第7-11周 第5周<br /><br />
                                </td>
                                <td align="left">
毛泽东思想和中国特色社会主义理论体系概论<br />
何家华-主讲<br />
2-107    第1-3周 第7-12周 第5,15周<br /><br />
                                </td>
                                <td align="left">
概率论与数理统计(一)<br />
张水坤-主讲<br />
2-101    第1-3周 第7-12周 第5周<br /><br />
                                </td>
                                <td align="left">
                                </td>
                                <td align="left">
                                </td>
            </tr>
            <tr>
                    <th>第5-6节</th>
                                <td align="left">
概率论与数理统计(一)<br />
张水坤-主讲<br />
2-101    第1-3周 第7-12周 第5周<br /><br />
                                </td>
                                <td align="left">
大学英语-3<br />
艾思-主讲<br />
3-104    第7-12周 <br /><br />
                                </td>
                                <td align="left">
离散数学<br />
陈卓-主讲<br />
3-205    第1-3周 第7-12周 <br /><br />
                                </td>
                                <td align="left">
兴趣体育选修课-1<br />
中心操场1    第3-15周 <br /><br />
                                </td>
                                <td align="left">
大学物理(一)-2<br />
罗山梦黛-主讲<br />
2-403    第7-12周 第3,5周<br /><br />
                                </td>
                                <td align="left">
                                </td>
                                <td align="left">
                                </td>
            </tr>
            <tr>
                    <th>第7-8节</th>
                                <td align="left">
JAVA程序设计_上机<br />
宗欣露-上机指导<br />
6A4-2-3    第5周<br /><br />
毛泽东思想和中国特色社会主义理论体系概论<br />
何家华-主讲<br />
2-107    第11-12周 第15周<br /><br />
离散数学<br />
陈卓-主讲<br />
3-101    第1-3周 第7-10周 <br /><br />
                                </td>
                                <td align="left">
数据结构<br />
吴歆韵-主讲<br />
2-208    第1-3周 第7-12周 <br /><br />
                                </td>
                                <td align="left">
云计算与大数据平台<br />
陈建峡-主讲,董新华-主讲<br />
6A2-1-3    第7-12周 第3周<br /><br />
                                </td>
                                <td align="left">
概率论与数理统计(一)<br />
张水坤-主讲<br />
2-202    第9-12周 <br /><br />
云计算与大数据平台<br />
陈建峡-主讲,董新华-主讲<br />
6A2-1-3    第7-8周 <br /><br />
                                </td>
                                <td align="left">
毛泽东思想和中国特色社会主义理论体系概论<br />
何家华-主讲<br />
2-107    第1-3周 第7-12周 第5,15周<br /><br />
                                </td>
                                <td align="left">
                                </td>
                                <td align="left">
                                </td>
            </tr>
            <tr>
                    <th>第9-10节</th>
                                <td align="left">
数据结构_上机<br />
吴歆韵-上机指导<br />
6A4-2-1    第11-13周 <br /><br />
数据结构_上机<br />
吴歆韵-上机指导<br />
6A4-2-4    第14-15周 <br /><br />
形势与政策(一)-3<br />
张艳丽-主讲<br />
2-002    第7-10周 <br /><br />
                                </td>
                                <td align="left">
数据结构<br />
吴歆韵-主讲<br />
2-202    第6周<br /><br />
云计算与大数据平台<br />
陈建峡-主讲,董新华-主讲<br />
6A2-1-3    第7-8周 <br /><br />
                                </td>
                                <td align="left">
大学生创业基础<br />
张珍-主讲<br />
2-413    第1-11周 <br /><br />
                                </td>
                                <td align="left">
云计算与大数据平台_上机<br />
陈建峡-上机指导,董新华-上机指导<br />
6A2-1-3    第9-11周 <br /><br />
                                </td>
                                <td align="left">
离散数学<br />
陈卓-主讲<br />
3-101    第1-3周 第7-8周 <br /><br />
数据结构_上机<br />
吴歆韵-上机指导<br />
6A4-2-1    第9-11周 <br /><br />
                                </td>
                                <td align="left">
                                </td>
                                <td align="left">
                                </td>
            </tr>
    </table>

    <br />
    <div id = "weekSchedule">
    <table >
        <tr>
            <td>数据结构课程设计,</td>
            <td>第15周,</td>
            <td>星期一~星期六,</td>
            <td>第1~8节,</td>
            <td>地点:JSJ</td>
        </tr>
        <tr>
            <td>金工实习(一),</td>
            <td>第16~17周,</td>
            <td>星期一~星期六,</td>
            <td>第1~8节,</td>
            <td>地点:JSJ</td>
        </tr>
        <tr>
            <td>电子实习(一),</td>
            <td>第4周,第6周,</td>
            <td>星期一~星期六,</td>
            <td>第1~8节,</td>
            <td>地点:JSJ</td>
        </tr>
    </table>
    </div>
    <br />

    <div>&nbsp</div>


</div>
    </div>

    <script type="text/javascript">
//<![CDATA[
jQuery(document).ready(function(){
if(!jQuery.telerik) jQuery.telerik = {};
jQuery.telerik.cultureInfo={"shortDate":"yyyy-M-d","longDate":"yyyy\u0027年\u0027M\u0027月\u0027d\u0027日\u0027","longTime":"H:mm:ss","shortTime":"H:mm","fullDateTime":"yyyy\u0027年\u0027M\u0027月\u0027d\u0027日\u0027 H:mm:ss","sortableDateTime":"yyyy\u0027-\u0027MM\u0027-\u0027dd\u0027T\u0027HH\u0027:\u0027mm\u0027:\u0027ss","universalSortableDateTime":"yyyy\u0027-\u0027MM\u0027-\u0027dd HH\u0027:\u0027mm\u0027:\u0027ss\u0027Z\u0027","generalDateShortTime":"yyyy-M-d H:mm","generalDateTime":"yyyy-M-d H:mm:ss","monthDay":"M\u0027月\u0027d\u0027日\u0027","monthYear":"yyyy\u0027年\u0027M\u0027月\u0027","days":["星期日","星期一","星期二","星期三","星期四","星期五","星期六"],"abbrDays":["周日","周一","周二","周三","周四","周五","周六"],"shortestDays":["日","一","二","三","四","五","六"],"abbrMonths":["一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月",""],"months":["一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月",""],"am":"上午","pm":"下午","dateSeparator":"-","timeSeparator":":","firstDayOfWeek":0,"currencydecimaldigits":2,"currencydecimalseparator":".","currencygroupseparator":",","currencygroupsize":3,"currencynegative":2,"currencypositive":0,"currencysymbol":"￥","numericdecimaldigits":2,"numericdecimalseparator":".","numericgroupseparator":",","numericgroupsize":3,"numericnegative":1,"percentdecimaldigits":2,"percentdecimalseparator":".","percentgroupseparator":",","percentgroupsize":3,"percentnegative":1,"percentpositive":1,"percentsymbol":"%"};
});
//]]>
</script>
</body>
</html>
'''

if __name__ == '__main__':
    user = {'username': '1710300728', 'password': '240623'}
    a = get_Data_formschedule(a)
    print(a)