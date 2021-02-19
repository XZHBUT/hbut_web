from bs4 import BeautifulSoup
import re


def get_Data_from_information(htmltext):    # 班级 学号 姓名 身份证号 性别 民族 所属学院 专业名称 学制 政治面貌 出生日期 入校日期 离校日期
    Data_information = []
    soup = BeautifulSoup(htmltext, 'html.parser')
    for i in soup.find_all('tr'):
        soup_data = BeautifulSoup(str(i), 'html.parser')
        for td in soup_data.find_all('td'):
            Data_information.append(str(td).replace('<td>', '').replace('</td>', ''))

    return Data_information


a = '''
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Cache-Control" content="no-cache,no-store, must-revalidate" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="0" />
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    <title>学生个人信息</title>
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

    
    
    <style type="text/css">
        div.allDiv
        {
            min-width:750px;
        }
    
        
        div.table-list
        {
            word-break:break-all;
        }

    </style>

</head>
<body style="background-color: #fff; margin-left: 15px; margin-right: 15px;">
    <div id="action_activity_pane" style="position: absolute; width: 100%; height: 100%;
        display: none;">
    </div>
    <div id="mainContent">
        




<div class="allDiv">

    <div style="padding-bottom: 14px; padding-top: 8px; padding-left: 8px" align="center">
        <h2  >个人学籍信息</h2>
    </div>
    <div class="table-list">
<form action="/T_Student/OwnInfo" method="post">        <table>
            <tr>
                <th><label for="Class">班级</label></th>
                <th><label for="ID">学号</label></th>
                <th><label for="Name">姓名</label></th>
                 <th><label for="ID_card">身份证号</label></th>
                <th><label for="Sex">性别</label></th>
                <th><label for="Nation">民族</label></th>
                <th><label for="Department">所属学院</label></th>
                <th><label for="Specialty">专业名称</label></th>
                <th><label for="EduYears">学制</label></th>
                <th><label for="Political">政治面貌</label></th>
                <th><label for="Birthday">出生日期</label></th>
                <th><label for="In_day">入校日期</label></th>
                <th><label for="Out_day">离校日期</label></th>

            </tr>
                <tr>
                    <td>19大数据2</td>
                    <td>1910311210</td>
                    <td>许兆</td>
                    <td>410721200108191017</td>
                    <td>男</td>
                    <td>汉族</td>
                    <td>计算机学院</td>
                    <td>数据科学与大数据技术</td>
                    <td>4</td>
                    <td>共青团员</td>
                    <td>2001-08-19</td>
                    <td>2019-09-01</td>
                    <td>2023-06-20</td>
                </tr>
        </table>
</form>    
    </div>
   
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
    c = get_Data_from_information(a)
    print(c)