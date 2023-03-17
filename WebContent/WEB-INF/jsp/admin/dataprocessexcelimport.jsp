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
<title>数据导入</title>
</head>
<body style="width: 80%;padding-left:10%;">
	<div align="center" style="color: red;">导入需要一些时间，请耐心等待导入成功对话框提示！</div>
	<form  method="post" class="form form-horizontal" id="forms"  enctype="multipart/form-data">
		<div class="row cl" style="padding-top:10%;">
			<div class="formControls col-xs-7 col-sm-9">
				<input style="padding-left:50%;" type="file" name="excelfile" id="excelfile" accept="file" />
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
	var files = document.getElementById('excelfile').files; //files是文件选择框选择的文件对象数组
	var form = new FormData(), 
    url = 'uploadfile2', //服务器上传地址
    file = files[0];
	form.append('file', file);
	
	var xhr = new XMLHttpRequest();
	xhr.open("post", url, true);
	
	//上传进度事件
	xhr.upload.addEventListener("progress", function(result) {
    	if (result.lengthComputable) {
        	//上传进度
        	var percent = (result.loaded / result.total * 100).toFixed(2); 
    	}
	}, 	false);
	
	xhr.addEventListener("readystatechange", function() {
   	 	var result = xhr;
    	if (result.status != 200) { //error
        	console.log('上传失败', result.status, result.statusText, result.response);
        	//alert("上传失败");
    	}else if (result.readyState == 4) { //finished
        	console.log('上传成功', result);
        	console.log(JSON.parse(result.response).filepath);
        	//picfile=JSON.parse(result.response).filepath;
    		//alert("上传成功");
    		$.ajax( {  
    	        type : 'POST',  
    	        url : 'admindataprocessexcelimportajax',
    	        data : {filename:JSON.parse(result.response).filepath},
    	        success : function(data) {
    	        	if(data.code==100){
    	        		alert("导入成功");
    	    			parent.reload();
    	        	}else{
    	        		alert("提交失败");
    	        	}
    			}  
    	    });
    	}
	});
	xhr.send(form); //开始上传
}

</script> 
<!--/请在上方写此页面业务相关的脚本-->
</body>
</html>