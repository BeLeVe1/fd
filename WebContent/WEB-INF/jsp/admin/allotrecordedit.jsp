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
<title>调拨单</title>
</head>
<body onload="desclick();" style="width: 80%;padding-left:10%;">
	<form  method="post" class="form form-horizontal" id="forms"  enctype="multipart/form-data">
		<div class="row cl" style="padding-top:2%;display:none;">
			<label class="form-label col-xs-4 col-sm-2">dataprocess：</label>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${jqcode}" placeholder="" id="jqcode" name="jqcode">
			</div>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${sharedpart_id}" placeholder="" id="sharedpart_id" name="sharedpart_id">
			</div>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${fg}" placeholder="" id="fg" name="fg">
			</div>
			<div class="formControls col-xs-7 col-sm-9">
				<input type="text" class="input-text" value="${qccode}" placeholder="" id="qccode" name="qccode">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">出库单编号：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" readonly="readonly" value="1" placeholder="" id="supplyplan_id" name="supplyplan_id">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">仓库编号：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" readonly="readonly" value="2" placeholder="" id="selfplan_id" name="selfplan_id">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">仓库：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" readonly="readonly" value="${jqcode}" placeholder="" id="jqcode" name="jqcode">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">库位：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" readonly="readonly" value="${bdcode}" placeholder="" id="bdcode" name="bdcode">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">出库日期：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" readonly="readonly" value="${qccode}" placeholder="" id="qccode" name="qccode">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">备件类型：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="${qcname}" placeholder="" id="qcname" name="qcname">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">备件名称：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="叶片" placeholder="" id="this_allot_number" name="this_allot_number">
			</div>
		</div>
		
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">备件编号	：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="1" placeholder="" id="plan_supply_number" name="plan_supply_number">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">规格型号	：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="UP115-2MW" placeholder="" id="sum_allot_number" name="sum_allot_number">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">数量	：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="1" placeholder="" id="create_people" name="create_people">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">计量单位	：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="UP115-2MW" placeholder="" id="createtime" name="createtime">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">单价	：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="1477876.11" placeholder="" id="receive_people" name="receive_people">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">总价	：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="147788" placeholder="" id="total_price" name="total_price">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">客户名称	：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="无" placeholder="" id="customer_name" name="customer_name">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">审核人	：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="杜亚东" placeholder="" id="checker" name="checker">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">合同号	：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="-" placeholder="" id="receive_people" name="receive_people">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">制单时间	：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="杜亚东" placeholder="" id="receive_people" name="receive_people">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">审核时间	：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="2021-12-23 19:56:45" placeholder="" id="receive_people" name="receive_people">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">修改人	：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="${receive_people}" placeholder="" id="receive_people" name="receive_people">
			</div>
		</div>
		<div class="row cl" style="padding-top:2%;">
			<label class="form-label col-xs-4 col-sm-3">修改日期：</label>
			<div class="formControls col-xs-7 col-sm-8">
				<input type="text" class="input-text" value="${createtime}" placeholder="" id="createtime" name="createtime">
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
//用新增数组方法操作数据
//var testdata = ${"#testdata"};
//var data=[{des:1},{des:2},{des:3},{des:4},{des:5}];
//用map接收数据
/*function desclick(){
	var jqcode = $("#jqcode").val();
	var qccode = $("#qccode").val();
	//alert(jqcode);
	$.ajax( {  
        type : 'get',  
        url : 'queryDesbdcode',
        datatype : 'json', 
        data : {jqcode:jqcode,qccode:qccode},
        success : function(resData) {
        	//alert("触发方法取值");
        	var len = resData.resData;
        	//console.log(len);
        	//console.log("触发");
        	$('#desbdcode').empty();
        	$('#desbdcode').append("<option>--请选择目标仓库--</option>");
        	for(var i=0;i<len.length;i++){
        		//console.log(len[i].bdcode);
        		$('#desbdcode').append("<option value='"+len[i].currentinventory+"'>"+len[i].bdcode+"</option>");
        	}
		}
    }); */
//获取相应元素
}
</script>
<script type="text/javascript">


function sub(){
	
// 	var desbdcode = document.getElementById('desbdcode');
//     var pindex = desbdcode.selectedIndex;
//     var pValue = desbdcode.options[pindex].value;
//     var pText = desbdcode.options[pindex].text;
//     console.log(pText);
//     desbdcode.options[document.getElementById('desbdcode').selectedIndex].value=pText;
    
	var params = $("#forms").serialize();
	
	if(forms.recordnumber.value==""){
    	layer.msg('请输入计划自筹数量！');
    	return false;
    }
	if(forms.create_people.value==""){
    	layer.msg('计划人为空！');
    	return false;
    }
	if(forms.createtime.value==""){
    	layer.msg('计划时间为空！');
    	return false;
    }
	if(forms.receive_people.value==""){
    	layer.msg('领用人为空！');
    	return false;
    }
    $.ajax( {  
        type : 'POST',  
        url : 'adminallotrecordeditajax',  
        //data : {params:params,bdcode:bdcode,qcname:qcname},
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
<script type="text/javascript">
function chkind(){
	document.getElementById('descurrentinventory').value=document.getElementById('desbdcode').value;
// 	var desbdcode = document.getElementById('desbdcode');
//     var pindex = desbdcode.selectedIndex;
//     var pValue = desbdcode.options[pindex].value;
//     var pText = desbdcode.options[pindex].text;
//     console.log(pText);
	//alert(pText);
}
</script> 
<!--/请在上方写此页面业务相关的脚本-->
</body>
</html>