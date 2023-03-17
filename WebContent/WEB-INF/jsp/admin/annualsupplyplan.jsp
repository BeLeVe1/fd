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
			<input type="text" name="jqcode" id="jqcode" placeholder="战区编号" style="width:100px" class="input-text">
			<input type="text" name="bdcode" id="bdcode" placeholder="部队编号" style="width:100px" class="input-text">
			<input type="text" name="qccode" id="qccode" placeholder="器材代码" style="width:100px" class="input-text">
			<input type="text" name="qcname" id="qcname" placeholder="器材名称" style="width:100px" class="input-text">
			<!-- <input type="text" name="fg" id="fg" placeholder="分工" style="width:100px" class="input-text"> -->
			<button onclick="selectbutton();" class="btn btn-success" style="background-color: #337AB7;" type="submit"></i><i class="Hui-iconfont">&#xe665;</i> 查询</button>
		</div>
		<div class="text-c" style="margin-top:1%;">
			<button onclick="Importconsume();" class="btn btn-success" style="background-color: #337AB7;" type="submit"></i><i class="Hui-iconfont">&#xe644;</i> 导入消耗件</button>
			<button onclick="Excelbutton();" class="btn btn-success" style="background-color: #337AB7;" type="submit"></i><i class="Hui-iconfont">&#xe644;</i> 备份</button>
			<button onclick="returnbutton();" class="btn btn-success" style="background-color: #337AB7;" type="submit"></i><i class="Hui-iconfont">&#xe68f;</i> 刷新</button>
		</div>
		<!-- 定义一个表格元素 -->
		<div style="height: 10px"></div>
		<div style="width: 98%; margin-left: 10px">
			<table id="example" class="table table-striped table-bordered">
				<thead>
					<tr>
						<th style="text-align: center;width: 1%">序号</th>
<!-- 						<th style="text-align: center;width: 1%"><input type="checkbox" onclick="ckAll();" id="allChecks" name="" value="" style="zoom:150%;"></th> -->
						<th style="text-align: center;width: 1%">战区编号</th>
						<th style="text-align: center;width: 1%">部队编号</th>
						<th style="text-align: center;width: 1%">装备代码</th>
						<th style="text-align: center;width: 1%">器材代码</th>
						<th style="text-align: center;width: 1%">器材名称</th>
<!-- 						<th style="text-align: center;width: 1%">单位</th> -->
<!-- 						<th style="text-align: center;width: 1%">单价</th> -->
<!-- 						<th style="text-align: center;width: 1%">单装用数</th> -->
						<th style="text-align: center;width: 1%">分工</th>
						<th style="text-align: center;width: 1%">预测消耗数量</th>
						<th style="text-align: center;width: 1%">计划申请数量</th>
						<th style="text-align: center;width: 1%">计划自筹/申请数量</th>
						<th style="text-align: center;width: 1%">期初库存</th>						
						<th style="text-align: center;width: 1%">当前库存</th>
						<th style="text-align: center;width: 1%">计划供应数量</th>
						<th style="text-align: center;width: 1%">备注</th>
						<th style="text-align: center;width: 1%">操作</th>
					</tr>
				</thead>
				<tbody></tbody>
			</table>
		</div>
	</div>
<script type="text/javascript">	
/*Javascript代码片段*/
$(document).ready(selectbutton());

function selectbutton(){
	var sort="";
// 	if(document.getElementById("plannumber").checked==true){
// 		sort="plannumber";
// 	}
// 	if(document.getElementById("number").checked==true){
// 		sort="number";
// 	}
// 	if(document.getElementById("lastnumber").checked==true){
// 		sort="lastnumber";
// 	}
	
	var jqcode=$("#jqcode").val();
	var bdcode=$("#bdcode").val();
	var zbcode="";
	var qccode=$("#qccode").val();
	var qcname=$("#qcname").val();
	var fg="";
	$(document).ready(function() {
		 $('#example').dataTable().fnDestroy();
	     $('#example').DataTable( {
	        "ajax":{
	        	  "url": "adminannualsupplyplanajax",
	              "type": "post",
	              "data": {jqcode:jqcode,bdcode:bdcode,zbcode:zbcode,qccode:qccode,qcname:qcname,fg:fg,sort:sort}
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
// 				 	{ "data": function(obj){return "<span><center><input type='checkbox' value='"+obj.dataprocess_id+"' name='check' style='zoom:150%;'></center></span>"}},
				 	{ "data": "jqcode" },
				 	{ "data": "bdcode" },
				 	{ "data": "zbcode" },
				 	{ "data": "qccode" },
		            { "data": "qcname" },
// 		            { "data": "unit" },
// 		            { "data": "unitprice" },
// 		            { "data": "dzys" },
		            { "data": "fg" },
		            { "data": "predictionnumber" },
		            { "data": "plannumber" },		            
		            { "data": "lastnumber" },
		            { "data": "number" },
		            { "data": "currentnumber" },
		            { "data": "realsupply" },
		            { "data": "comments" },
		            { "data": function(obj){
		            	if(obj.czflag==1){
		            		return "<span><center><a onclick=\"open_layer('调拨','adminallotrecordedit?sharedpart_id="+obj.dataprocess_id+"&plannumber="+obj.plannumber+"&number="+obj.number+"&lastnumber="+obj.lastnumber+"&jqcode="+obj.jqcode+"&bdcode="+obj.bdcode+"&qccode="+obj.qccode+"&qcname="+obj.qcname+"&fg="+obj.fg+"&currentnumber="+obj.currentnumber+"&realsupply="+obj.realsupply+"','900','450')\">调拨</a>  <a onclick=\"open_layer('修改','adminrealsupplyedit?jqcode="+obj.jqcode+"&bdcode="+obj.bdcode+"&qccode="+obj.qccode+"&qcname="+obj.qcname+"&fg="+obj.fg+"&realsupply="+obj.realsupply+"&comments="+obj.comments+"','900','450')\">修改</a></center></span>"
		            	}else{
		            		return "<span><center>——</span></center>"
		            	}
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


function  open_layer(title,url,w,h){
	layer_show(title,url,w,h);
}  
  
function  reload(){  
	var index = layer.getFrameIndex(window.name);
	layer.close(index);
	location.reload();
}
//全选
function ckAll(){
    var flag=document.getElementById("allChecks").checked;
    var cks=document.getElementsByName("check");
    for(var i=0;i<cks.length;i++){
        cks[i].checked=flag;
    }
}

// function checkbtn2(){
// 	if(document.getElementById("plannumber").checked==true){
// 		document.getElementById("number").checked=false;
// 		document.getElementById("lastnumber").checked=false;
// 		selectbutton();
// 	}else{
// 		selectbutton();
// 	}
// }
// function checkbtn3(){
// 	if(document.getElementById("number").checked==true){
// 		document.getElementById("plannumber").checked=false;
// 		document.getElementById("lastnumber").checked=false;
// 		selectbutton();
// 	}else{
// 		selectbutton();
// 	}
// }
// function checkbtn4(){
// 	if(document.getElementById("lastnumber").checked==true){
// 		document.getElementById("plannumber").checked=false;
// 		document.getElementById("number").checked=false;
// 		selectbutton();
// 	}else{
// 		selectbutton();
// 	}
// }

function returnbutton(){
	location.reload();
}

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

function Excelbutton(){
	$.ajax({
	    type: "POST",
	    url:'adminplanbdExcel',
	    success: function(data) {
		    if(data.code==100){
		    	/* window.location.href="http://test.jikewangluo.cn/upload/制定计划-部队.xls"; */
		    	window.location.href="http://localhost:8081/depot/upload/年度供应计划-部队.xls";
		    }else{	
				layer.msg('系统错误，请联系后台管理员');	
		    }
	    }
	});
}
</script>
</body>
</html>
