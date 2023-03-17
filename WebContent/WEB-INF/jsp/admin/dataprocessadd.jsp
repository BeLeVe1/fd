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
<body style="width: 80%;padding-left:10%;">
	<form  method="post" class="form form-horizontal" id="forms"  enctype="multipart/form-data">
		<div class="row cl" style="padding-top:2%;display:none">
			<label class="form-label col-xs-4 col-sm-2">ID：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess_id}" placeholder="" id="dataprocess_id" name="dataprocess_id">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">装备代码：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.zbcode}" placeholder="" id="zbcode" name="zbcode">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">器材代码：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.qccode}" placeholder="" id="qccode" name="qccode">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">器材名称：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.qcname}" placeholder="" id="qcname" name="qcname">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">规格件号：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.ggjh}" placeholder="" id="ggjh" name="ggjh">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">单位：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.unit}" placeholder="" id="unit" name="unit">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">单价：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.unitprice}" placeholder="" id="unitprice" name="unitprice">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">单装用数：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.dzys}" placeholder="" id="dzys" name="dzys">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">分工：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.fg}" placeholder="" id="fg" name="fg">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">长度：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.length}" placeholder="" id="length" name="length">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">宽度：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.width}" placeholder="" id="width" name="width">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">高度：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.height}" placeholder="" id="height" name="height">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-2">重量：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${dataprocess.weight}" placeholder="" id="weight" name="weight">
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
   	
    if(forms.zbcode.value==""){
    	layer.msg('装备代码不能为空');
    	return false;
    }
    if(forms.qccode.value==""){
    	layer.msg('器材代码不能为空');
    	return false;
    }
    if(forms.qcname.value==""){
    	layer.msg('器材名称不能为空');
    	return false;
    }
    if(forms.ggjh.value==""){
    	layer.msg('规格件号不能为空');
    	return false;
    }
    if(forms.unit.value==""){
    	layer.msg('单位不能为空');
    	return false;
    }
    if(forms.unitprice.value==""){
    	layer.msg('单价不能为空');
    	return false;
    }
    if(forms.dzys.value==""){
    	layer.msg('单装用数不能为空');
    	return false;
    }
    if(forms.fg.value==""){
    	layer.msg('分工不能为空');
    	return false;
    }
    if(forms.length.value==""){
    	layer.msg('长度不能为空');
    	return false;
    }
    if(forms.width.value==""){
    	layer.msg('宽度不能为空');
    	return false;
    }
    if(forms.height.value==""){
    	layer.msg('高度不能为空');
    	return false;
    }
    if(forms.weight.value==""){
    	layer.msg('重量不能为空');
    	return false;
    }
    
    
    $.ajax( {  
        type : 'POST',  
        url : 'admindataprocessaddajax',  
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