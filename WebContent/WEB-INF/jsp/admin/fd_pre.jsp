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
<script type="text/javascript"
	src="js/Hui-js/lib/jquery/1.9.1/jquery.min.js"></script>
<script type="text/javascript" src="js/Hui-js/lib/layer/2.4/layer.js"></script>
<script type="text/javascript" src="static/h-ui/js/H-ui.min.js"></script>
<script type="text/javascript" src="static/h-ui.admin/js/H-ui.admin.js"></script>




<!--/_footer /作为公共模版分离出去-->
<!--请在下方写此页面业务相关的脚本-->
<script type="text/javascript"
	src="js/Hui-js/lib/My97DatePicker/4.8/WdatePicker.js"></script>
<script type="text/javascript"
	src="js/Hui-js/lib/datatables/1.10.0/jquery.dataTables.min.js"></script>
<script type="text/javascript"
	src="js/Hui-js/lib/laypage/1.2/laypage.js"></script>
<script type="text/javascript"></script>
<!-- HTML代码片段中请勿添加<body>标签 //-->
</head>
<body>
	<div id="container">
		<div class="text-c" style="margin-top: 1%;">
			<input type="text" name="part_name" id="part_name" placeholder="备件名称"
				style="width: 200px" class="input-text">
			<button onclick="selectbutton();" class="btn btn-success"
				style="background-color: #337AB7;" type="submit">
				</i><i class="Hui-iconfont">&#xe665;</i> 查询
			</button>
			<button onclick="prebutton();" class="btn btn-success"
				style="background-color: #337AB7;" type="submit">
				</i><i class="Hui-iconfont">&#xe606;</i> 预测
			</button>
		</div>
		<div class="text-c" style="margin-top: 1%;">
			<button onclick="addbutton();" class="btn btn-success"
				style="background-color: #337AB7;" type="submit">
				</i><i class="Hui-iconfont">&#xe644;</i> 添加出库记录
			</button>
			<button onclick="returnbutton();" class="btn btn-success"
				style="background-color: #337AB7;" type="submit">
				</i><i class="Hui-iconfont">&#xe68f;</i> 刷新
			</button>
		</div>
		<!-- 定义一个表格元素 -->
		<div style="height: 10px"></div>
		<div style="width: 98%; margin-left: 10px">
			<table id="example" class="table table-striped table-bordered">
				<thead>
					<tr>
						<th style="text-align: center; width: 1%">序号</th>
						<th style="text-align: center; width: 1%">备件名称</th>
						<th style="text-align: center; width: 1%">出库日期</th>
						<th style="text-align: center; width: 1%">预测值</th>
						<th style="text-align: center; width: 1%">运行时间</th>

					</tr>
				</thead>
				<tbody></tbody>
			</table>
		</div>
	</div>
	<script type="text/javascript">	
	
	$(document).ready(selectbutton());

	function selectbutton(){
		var sort="";
		
		var part_name=$("#part_name").val();
		
	$(document).ready(function() {
		$('#example').dataTable().fnDestroy();
		$('#example').dataTable({
			"ajax":{
				"url":"adminfd_preajax",
				"type": "post",
				"data":{part_name:part_name}
				},
            "lengthChange": true,//是否允许用户自定义显示数量
            "bPaginate": true, //翻页功能
            "bFilter": false, //列筛序功能
            "searching": false,//本地搜索
            "ordering": false, //排序功能
            "Info": true,//页脚信息
            "autoWidth": true,//自动宽度
	        "serverSide":true, 
	        /* "bLengthChange":false, */
	        "fnDrawCallback" : function(){
	        	     　　this.api().column(0).nodes().each(function(cell, i) {
	        	        　　　　cell.innerHTML =  i + 1;
	        	      　　});
	                }, 
	        "columns": [
	        	{ "data": null,"targets": 0}, 
			 	{ "data": "part_name" },
			 	{ "data": "prediction_date" },
			 	{ "data": "prediction_value" },
			 	{ "data": "running_date" }
	        ],
	        
	        "columnDefs": [
	                       {
	                          
	                       }
	                   ],
	        "oLanguage": {    // 语言设置  
	        	"sProcessing": "处理中...",
	            "sLengthMenu": "显示 _MENU_ 项结果",
	            "sZeroRecords": "没有匹配结果",
	            "sInfo": "显示第 _START_ 至 _END_ 项结果，共 _TOTAL_ 项",
	            "sInfoEmpty": "显示第 0 至 0 项结果，共 0 项",
	            "sInfoFiltered": "(由 _MAX_ 项结果过滤)",
	            "sInfoPostFix": "",
	            "sUrl": "",
	            "sEmptyTable": "表中数据为空",
	            "sLoadingRecords": "载入中...",
	            "sInfoThousands": ",",
	            "oPaginate": {
	                "sFirst": "首页",
	                "sPrevious": "上页",
	                "sNext": "下页",
	                "sLast": "末页"
	          }
	        }
		});
		} );
	}
	function modaldemo(){
		  $("#modal-demo").modal("show")
		}
		function modalalertdemo() {
		  $("body").Huimodalalert({
		    content: '我是消息框，2秒后我自动滚蛋！',
		    speed: 2000
		  })
		}
	function prebutton(){
		alert("算法开始运行")
		$.ajax({
		    type: "POST",
		    url:'adminfd_preAlgorithmtest',
		    success: function(data){
		     	//alert(data)
			 	 if(data.code=="100"){
			      	
			 		prompt("算法运行成功")
			 			 		
			 		
			      	
		    }
		    }
		});
		
	}
			 
		
		
	
</script>
</body>
</html>
