<!-- 此例子是结合bootstrap的Datatables，暂且定位为最基本的例子吧 -->
<!-- 引入必须的css和js文件 -->
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix='fmt' uri="http://java.sun.com/jsp/jstl/fmt" %> 
<!DOCTYPE HTML>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8">
<meta name="renderer" content="webkit|ie-comp|ie-stand">
<meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" />
<link rel="Bookmark" href="/favicon.ico" >
<link rel="Shortcut Icon" href="/favicon.ico" />
<!--[if lt IE 9]>
<script type="text/javascript" src="lib/html5shiv.js"></script>
<script type="text/javascript" src="lib/respond.min.js"></script>
<![endif]-->
<link rel="Bookmark" href="/favicon.ico" >
<link rel="Shortcut Icon" href="/favicon.ico" />
<link rel="stylesheet" type="text/css" href="static/h-ui/css/H-ui.min.css" />
<link rel="stylesheet" type="text/css" href="static/h-ui.admin/css/H-ui.admin.css" />
<link rel="stylesheet" type="text/css" href="js/Hui-js/lib/Hui-iconfont/1.0.8/iconfont.css" />
<link rel="stylesheet" type="text/css" href="static/h-ui.admin/skin/default/skin.css" id="skin" />
<link rel="stylesheet" type="text/css" href="static/h-ui.admin/css/style.css" />
<link rel="stylesheet" type="text/css" href="js/Hui-js/lib/jquery/jquery-easyui-1.4.5/themes/icon.css" />
<link id="easyuiTheme" rel="stylesheet" type="text/css" href="js/Hui-js/lib/jquery/jquery-easyui-1.4.5/themes/ui-pepper-grinder/easyui.css" />
<!--[if IE 6]>
<script type="text/javascript" src="lib/DD_belatedPNG_0.0.8a-min.js" ></script>
<script>DD_belatedPNG.fix('*');</script>
<![endif]-->
<!--/meta 作为公共模版分离出去-->
<script language="javascript" type="text/javascript" src="js/Hui-js/lib/jquery/jquery-easyui-1.4.5/jquery.min.js"></script>
<script language="javascript" type="text/javascript" src="js/Hui-js/lib/jquery/jquery-easyui-1.4.5/jquery.easyui.min.js"></script>
<script language="javascript" type="text/javascript" src="js/Hui-js/lib/jquery/jquery-easyui-1.4.5/locale/easyui-lang-zh_CN.js"></script>
<script type="text/javascript" src="js/Hui-js/lib/layer/2.4/layer.js"></script>
<!--建议手动加在语言，避免在ie下有时因为加载语言失败导致编辑器加载失败-->
<title>数据录入</title>
</head>
<body style="width: 100%;padding-left:0%;">
	<form  method="post" class="form form-horizontal" id="forms"  enctype="multipart/form-data">
	<table border="0px solid #ccc" WIDTH="50" HEIGHT="50" ALIGN="CENTER">
	<tr>
		<td>
		<div class="row cl" style="padding-top:2%;display:none">
			<label class="form-label col-xs-4 col-sm-2">departmentNum：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${departmentNum}" placeholder="" id="departmentNum" name="departmentNum"> 
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;padding-left:10%;">
			<label class="form-label col-xs-4 col-sm-4">部门名称：</label>
			<div class="formControls col-xs-4 col-sm-6">
				<input type="text" class="input-text"  value="${dataprocess.departmentName}" placeholder="" id="departmentName" name="departmentName">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;padding-left:10%;">
			<label class="form-label col-xs-4 col-sm-4">部门编号：</label>
			<div class="formControls col-xs-4 col-sm-6">
				<input type="text" class="input-text"  disabled="disabled" value="${dataprocess.departmentNum}" placeholder="" id="departmentNum" name="departmentNum">
			</div>
		</div>
		
		
		</td>
<!-- 		<td> -->
<!-- 		<div class="row cl" style="padding-top:2%;padding-right:30%;"> -->
<!-- 			<label class="form-label col-xs-4 col-sm-4">加工能耗：</label> -->
<!-- 			<div class="formControls col-xs-4 col-sm-8" contenteditable = "true"> -->
<%-- 				<input type="text" class="input-text" value="${dataprocess.machine_processpower}" placeholder="" id="machine_processpower" name="machine_processpower"> --%>
<!-- 			</div> -->
<!-- 		</div> -->
<!-- 		<div class="row cl" style="padding-top:2%;padding-right:30%;"> -->
<!-- 			<label class="form-label col-xs-4 col-sm-4">空闲能耗：</label> -->
<!-- 			<div class="formControls col-xs-4 col-sm-8"> -->
<%-- 				<input type="text" class="input-text" value="${dataprocess.machine_idlepower}" placeholder="" id="machine_idlepower" name="machine_idlepower"> --%>
<!-- 			</div> -->
<!-- 		</div> -->
<!-- 		<div class="row cl" style="padding-top:2%;padding-right:30%;"> -->
<!-- 			<label class="form-label col-xs-4 col-sm-4">设置能耗：</label> -->
<!-- 			<div class="formControls col-xs-4 col-sm-8"> -->
<%-- 				<input type="text" class="input-text" value="${dataprocess.machine_midpower}" placeholder="" id="machine_midpower" name="machine_midpower"> --%>
<!-- 			</div> -->
<!-- 		</div> -->
<!-- 		<div class="row cl" style="padding-top:2%;padding-right:30%;"> -->
<!-- 			<label class="form-label col-xs-4 col-sm-4">机器类型：</label> -->
<!-- 			<div class="formControls col-xs-4 col-sm-8"> -->
<!-- 				<span class="select-box" style="width:100%;"> -->
<!-- 				<select class="select" id="machine_type" name="machine_type" size="1"> -->
<!-- 					<option value="">请选择</option> -->
<!-- 					<option value="离散机">离散机</option> -->
<!-- 					<option value="批处理机">批处理机</option> -->
<!-- 				</select> -->
<!-- 				</span> -->
<%--			<input type="text" class="input-text" disabled="disabled" value="${dataprocess.machine_type}" placeholder="" id="jqcode" name="jqcode"> --%> 
<!-- 			</div> -->
<!-- 		</div> -->
<!-- 		</td> -->
	</tr>
	<tr style="width: 100%;"> 
	<td colspan="2"> <!-- 合并两列单元格 -->
		<div class="mt-20 text-c" style="width: 100%;">
			<input class="btn btn-primary radius" type="button" id="Btn" onClick="sub();" value="&nbsp;&nbsp;提交&nbsp;&nbsp;  ">
		</div>
		</td>
	</tr>
	</table>
	</form>


<script>
window.PROJECT_CONTEXT = "${ctx}/";
</script>
<script type="text/javascript">


function sub(){
		
    var params = $("#forms").serialize();
   	
//     if(forms.machine_type.value==""){
//     	layer.msg('机器类型不能为空');
//     	return false;
//     }
    
    $.ajax( {  
        type : 'POST',  
        url : 'adminfd_departmentresetajax',  
        data : params,  
        success : function(data) {
        	if(data.code==100){
        		alert("提交成功");
        		//layer.msg(data.info);  
    			parent.reload();
        	}else{
        		layer.msg(data.info);
        	}
		}  
    }); 
}

</script> 
</body>
</html>