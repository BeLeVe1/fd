<!-- 此例子是结合bootstrap的Datatables，暂且定位为最基本的例子吧 -->
<!-- 引入必须的css和js文件 -->
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix='fmt' uri="http://java.sun.com/jsp/jstl/fmt"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn"%>
<!DOCTYPE HTML>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8">
<meta name="renderer" content="webkit|ie-comp|ie-stand">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport"
	content="width=device-width,initial-scale=1,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<!-- <link rel="stylesheet" type="text/css" href="css/dataTables.bootstrap.min.css" /> 
<link rel="stylesheet" type="text/css" href="css/dataTables.bootstrap.css" />  -->
<script src="js/Hui-js/lib/jquery.js"></script>
<script src="js/Hui-js/lib/datatables/1.10.0/jquery.dataTables.min.js"></script>
<link rel="stylesheet" type="text/css"
	href="static/h-ui/css/H-ui.min.css" />
<link rel="stylesheet" type="text/css"
	href="static/h-ui.admin/css/H-ui.admin.css" />
<link rel="stylesheet" type="text/css"
	href="js/Hui-js/lib/Hui-iconfont/1.0.8/iconfont.css" />
<link rel="stylesheet" type="text/css"
	href="static/h-ui.admin/skin/default/skin.css" id="skin" />
<link rel="stylesheet" type="text/css"
	href="static/h-ui.admin/css/style.css" />
<script type="text/javascript" src="js/Hui-js/lib/jquery/1.9.1/jquery.min.js"></script>
<script type="text/javascript" src="js/Hui-js/lib/layer/2.4/layer.js"></script>
<script type="text/javascript" src="static/h-ui/js/H-ui.min.js"></script>
<script type="text/javascript" src="static/h-ui.admin/js/H-ui.admin.js"></script>
<!--/_footer /作为公共模版分离出去-->
<!--请在下方写此页面业务相关的脚本-->
<script type="text/javascript" src="js/Hui-js/lib/My97DatePicker/4.8/WdatePicker.js"></script>
<script type="text/javascript" src="js/Hui-js/lib/datatables/1.10.0/jquery.dataTables.min.js"></script>
<script type="text/javascript" src="js/Hui-js/lib/laypage/1.2/laypage.js"></script>
<script type="text/javascript"></script>
<!-- HTML代码片段中请勿添加<body>标签 //-->
</head>
<body>
	<div id="container">
		<div class="text-c" style="margin-top:1%;">			
			<button onclick="Importconsume();" class="btn btn-success" style="background-color: #337AB7;" type="submit"></i><i class="Hui-iconfont">&#xe644;</i> 导入消耗件</button>
			<button onclick="Importrepair();" class="btn btn-success" style="background-color: #337AB7;" type="submit"></i><i class="Hui-iconfont">&#xe644;</i> 导入可修件</button>
			<button onclick="Excelbutton();" class="btn btn-success" style="background-color: #337AB7;" type="submit"></i><i class="Hui-iconfont">&#xe644;</i> 备份</button>
			<button onclick="returnbutton();" class="btn btn-success" style="background-color: #337AB7;" type="submit"></i><i class="Hui-iconfont">&#xe68f;</i> 刷新</button>
		</div>
		<!-- 定义一个表格元素 -->
	</div>
<script type="text/javascript">	
/*Javascript代码片段*/
function Importconsume(){
	var fg="总部";
	$.ajax({
	    type: "POST",
	    url:'adminsumplanlistconsumeajax',
	    data: {fg:fg},
	    success: function(data) {
		    if(data.code==100){
		    	layer.msg('导入消耗件成功');	
		    }else{	
				layer.msg('系统错误，请联系后台管理员');	
		    }
	    }
	    });
}

function Importrepair(){
	var fg="总部";
	$.ajax({
	    type: "POST",
	    url:'adminsumplanlistrepairajax',
	    data: {fg:fg},
	    success: function(data) {
		    if(data.code==100){
		    	layer.msg('导入可修件成功');	
		    }else{	
				layer.msg('系统错误，请联系后台管理员');	
		    }
	    }
	    });
}

function  reload(){  
	 var index = layer.getFrameIndex(window.name);
	 layer.close(index);
	 location.reload();
	 }

function returnbutton(){
	location.reload();
}

//条件查询

function Excelbutton(){
	$.ajax({
	    type: "POST",
	    url:'adminstorehouseExcel',
	    success: function(data) {
		    if(data.code==100){
		    	/* window.location.href="http://test.jikewangluo.cn/upload/数据处理.xls"; */
		    	window.location.href="http://localhost:8081/depot/upload/库存记录.xls";
		    }else{	
				layer.msg('系统错误，请联系后台管理员');	
		    }
	    }
	});
}
</script>
</body>
</html>
