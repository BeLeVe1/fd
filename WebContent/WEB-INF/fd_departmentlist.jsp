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
	<div class="cl pd-5 bg-1 bk-gray mt-10">
		<span class="l" style="margin-left:5px;margin-top:1%;">
			<button onclick="open_layer('信息添加','adminfd_departmentadd','900','450')" href="javascript:;" class="btn btn-success" style="background-color: #337AB7;" type="submit"></i><i class="Hui-iconfont">&#xe645;</i> 添加信息</button>
<!-- 			<button onclick="Excelbutton();" class="btn btn-success" style="background-color: #337AB7;" type="submit"></i><i class="Hui-iconfont">&#xe644;</i> 备份</button> -->
			<button onclick="returnbutton();" class="btn btn-success" style="background-color: #337AB7;" type="submit"></i><i class="Hui-iconfont">&#xe68f;</i> 刷新</button>
		</span>
		<div class="text-c" style="margin-top:1%;">
		    <input type="text" name="bdcode" id="bdcode" placeholder="部门名称" style="width:100px" class="input-text">
			<input type="text" name="jqcode" id="jqcode" placeholder="部门编号" style="width:100px" class="input-text">
			
			<!-- <input type="text" name="cdcode" id="cdcode" placeholder="电话号码" style="width:100px" class="input-text">
			<input type="text" name="ddcode" id="ddcode" placeholder="职务" style="width:100px" class="input-text"> -->
			<button onclick="selectbutton1();" class="btn btn-success" style="background-color: #337AB7;" type="submit"></i><i class="Hui-iconfont">&#xe665;</i> 查询</button>
	    </div>
	</div>
		<!-- 定义一个表格元素 -->
		<div style="height: 10px"></div>
		<div style="width: 98%; margin-left: 10px">
			<table id="example" class="table table-striped table-bordered">
				<thead>
					<tr>
						 <th style="text-align: center;width: 1%">序号</th>
						 <th style="text-align: center;width: 1%">部门名称</th>
						<th style="text-align: center;width: 1%">部门编号</th>
						<th style="text-align: center;width: 1%">操作</th>
					</tr>
				</thead>
				<tbody></tbody>
			</table>
		</div>
	</div>
<script type="text/javascript">	
/*Javascript代码片段*/
$(document).ready(selectbutton1());

function  open_layer(title,url,w,h){  
	
		layer_show(title,url,w,h);
		
		 }
function  reload(){  
	 var index = layer.getFrameIndex(window.name);
	 layer.close(index);
	 location.reload();
	 }


function selectbutton1(){
	
	var jqcode=$("#jqcode").val();
	var bdcode=$("#bdcode").val();
	
	$(document).ready(function() {
		 $('#example').dataTable().fnDestroy();
	     $('#example').DataTable( {
	        "ajax":{
	        	  "url": "adminfd_departmentlist1ajax",
	              "type": "post",
	              "data": {jqcode:jqcode,bdcode:bdcode}
	            },
	            "lengthChange": false,//是否允许用户自定义显示数量
	            "bPaginate": true, //翻页功能
	            "bFilter": false, //列筛序功能
	            "searching": false,//本地搜索
	            "ordering": false, //排序功能
	            "Info": true,//页脚信息
	            "autoWidth": true,//自动宽度
		        "serverSide":true, 
		        /* "bLengthChange":false, 
		        "searching" : false, */
		        "fnDrawCallback" : function(){
		        	     　　this.api().column(0).nodes().each(function(cell, i) {
		        	        　　　　cell.innerHTML =  i + 1;
		        	      　　});
		                }, 
		        "columns": [        
				 		{ "data": null,"targets": 0}, 
				    	{ "data": "departmentName" },
				    	{ "data": "departmentNum" },
		            { "data": function(obj){
		                	return "<span><center><a onclick=\"open_layer('编辑','adminfd_departmentreset?departmentNum="+obj.departmentNum+"','500','350')\">编辑</a>&nbsp;<a onclick=\"deleteobj("+obj.departmentNum+")\">删除</a></center></span>"
		                	}
		                 }
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

	 
	  });
	
}

function returnbutton(){
	location.reload();
}
function Excelbutton(){
	$.ajax({
	    type: "POST",
	    url:'adminfd_departmentlistExcel',
	    success: function(data) {
		    if(data.code==100){
		    	/* window.location.href="http://test.jikewangluo.cn/upload/预测查询.xls"; */
		    	window.location.href="http://localhost:8081/depot/upload/机器信息表.xls";
		    }else{	
				layer.msg('系统错误，请联系后台管理员');	
		    }
	    }
	});
}
function deleteobj(id){
	layer.confirm('确定要执行此删除操作吗?', {icon: 3, title:'提示'}, function(index){
		  $.ajax({
			    cache: true,
			    type: "POST",
			    url:'adminfd_departmentdeleteajax',
			    data:{id:id},
			    async: false,
			    error: function(request) {
			        layer.msg("连接错误，请联系后台管理员");
			    },
			    success: function(data) {
				    
			     if(data.code==100){
			    	 layer.msg('删除成功..');
			    	 location.reload();
				   }else{	
					   layer.msg('系统错误，请联系后台管理员');	
					}
			      
			    }
			});		  
		  layer.close(index);
		});
	  return false; 
}
</script>
</body>
</html>