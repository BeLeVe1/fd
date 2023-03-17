$(function(){
	
	var clipArea = new PhotoClip(".imageBox", {
		 outputQuality: 1,
         file: "#pic-file",
         view: "#viewImg",
         ok: "#btnCrop",
         loadStart: function() {
             console.log("照片读取中");
         },
         loadComplete: function() {
             console.log("照片读取完成");
             showPicSeletor();
         },
         clipFinish: function(dataURL) {
        	 console.log("照片剪切完成");
         }
     });
	
	var submiting = true;
	// 提交截图
	$("#pic-submit>button").click(function(){
		if ($("#viewImg").prop("src").length== 0 || $("#viewImg").prop("src").indexOf("http") > -1) {
			// 还未截取图片
			alert("还未截取图片");
			return;
		}
		
		// 重复提交
		if (submiting)
			return;
		
		submiting = true;
		var srcImg = $(".cropped").find("img").eq(0).prop("src");
		var type = $("#pic-type").val();
		$.post("merchantupload" , {file: srcImg}, function(data){
			if (data.errorCode == 0) {
				showMain();
				var id = data.result;
				addPic(id, type, true);
				
				// 还原现场
				$("#pic-file").val("");
				$("#viewImg").prop("src","");
			}
		});
	});
	
	// 选择Logo
	$("#select-logo").click(function(){
		submiting = false;
		$("#pic-type").val("logo");
		$("#viewImg").css("width",340);
		clipArea.setSize(340,170);
		clipArea.setOutputSize(340,170);
	});
	
	// 选择介绍图片
	$("#select-desc").click(function(){
		submiting = false;
		$("#pic-type").val("desc");
		$("#viewImg").css("width",170*(1800/1342));
		clipArea.setSize(1800/6,1342/6);
		clipArea.setOutputSize(1800,1342);
	});
	
	$(".location").click(function(){
		showLocation();
	});

});

/**
 * 添加图片/logo
 * @param id	图片/logo标识符
 * @param type 类型：logo/desc
 * @param timelyupdate	是否及时更新input值，如果不是及时，完成后需要手动调用一下updateImgIdInput()
 */
function addPic(id, type, timelyupdate){
	var imgid = id;
	if(imgid.indexOf(".") > -1)
		imgid = imgid.replace(/\./g, "_");
	
	var img = $('<img imgsrc="'+id+'" id="' + imgid+ '" class="selected-img-item" src="upload/' + id+ '" height="50" style="float:left">'
			+'<span style="background-image: url(img/merchant/delete.png)" class="delete-selected-img"></span>');
	if (type == "logo") {
		$("#show-logo").html(img);
	} else if (type = "desc") {
		$("#show-desc").append(img);
	}
	
	if (timelyupdate)
		updateImgIdInput();
	
	// 删除图片
	$(".delete-selected-img").unbind("click").bind("click", function(){
		var id = $(this).prev().prop("id");
		$("#"+id).remove();
		$(this).remove();
		
		// 更新input内容
		updateImgIdInput();
	});
}

/**
 * 更新图片input及选取提示
 */
function updateImgIdInput(){
	if ($("#show-logo .selected-img-item").length > 0 ){
		$("#show-logo .selected-img-item").each(function(i,item){
			var id = $(item).attr("imgsrc");
			$("#logo-id").val(id);
		});
		$("#select-logo").html("重新选择");
	} else {
		$("#logo-id").val("");
		$("#select-logo").html("选取图片");
	}
	
	if ($("#show-desc .selected-img-item").length > 0 ){
		var descids = "";
		$("#show-desc .selected-img-item").each(function(i,item){
			var id = $(item).attr("imgsrc");
			descids += (id + ",");
		});
		$("#desc-ids").val(descids);
		
		if ($("#show-desc .selected-img-item").length >=1000 ){
			// 停止添加图片
			$("#select-desc").prop("for", "");
			$("#select-desc").html("最多上传1000张图片!");
		} else {
			$("#select-desc").prop("for", "pic-file");
			$("#select-desc").html("继续添加");
		}
	} else {
		$("#desc-ids").val("");
		$("#select-desc").html("选取图片");
	}
	
}

function showMain(){
	$("#merchant-info").css("display" , "block");
	$("#pic-selector").css("display" , "none");
}

function showPicSeletor(){
	$("#merchant-info").css("display" , "none");
	$("#pic-selector").css("display" , "block");
}

function showLocation(){
	$("#merchant-info").css("display" , "none");
	$("#pic-selector").css("display" , "none");
	$("#merchant-location").css("z-index", "999");
}
