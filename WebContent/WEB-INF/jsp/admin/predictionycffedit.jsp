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
<title>编辑管理员</title>
</head>
<body style="width: 80%;padding-left:10%;">
	<form  method="post" class="form form-horizontal" id="forms"  enctype="multipart/form-data">
		<div class="row cl" style="padding-top:2%;display:none;">
			<label class="form-label col-xs-4 col-sm-2">dataprocess_id：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.dataprocess_id}" placeholder="" id="dataprocess_id" name="dataprocess_id">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">选择权限：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<span class="select-box" style="width:150px;">
				<select class="select" id="ycff" name="ycff" size="1">
					<option value="0">请选择</option>
					<option value="1" <c:if test="${dataprocess.ycff==1}"> selected="selected"</c:if>>简单移动平均法</option>
					<option value="2" <c:if test="${dataprocess.ycff==2}"> selected="selected"</c:if>>指数平滑法</option>
					<option value="3" <c:if test="${dataprocess.ycff==3}"> selected="selected"</c:if>>线性回归法</option>
					<option value="4" <c:if test="${dataprocess.ycff==4}"> selected="selected"</c:if>>误差平方和倒数组合预测</option>
				</select>
				</span>
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">平滑常数：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.anumber}" placeholder="" id="anumber" name="anumber">
			</div>
		</div>
	<div class="mt-20 text-c">
		<input class="btn btn-primary radius" type="button" id="Btn" onClick="sub();" value="&nbsp;&nbsp;提交&nbsp;&nbsp;  ">
	</div>
	</form>


<script>
window.PROJECT_CONTEXT = "${ctx}/";
</script>
<script type="text/javascript">


function sub(){
	
	var params = $("#forms").serialize();
	
	if(forms.ycff.value=="0"){
    	layer.msg('请选择预测方法！');
    	return false;
    }
    $.ajax( {  
        type : 'POST',  
        url : 'adminpredictionycffeditajax',  
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
<!--/请在上方写此页面业务相关的脚本-->
</body>
</html>