$(document).ready(function() {
    // summernote
    var mySummernote = $('.summernote');
    // summernote图文编辑器配置
    mySummernote.summernote({
        lang : 'zh-CN',// 语言
        height : 600, // 高度
        minHeight : 300, // 最小高度
        placeholder : '请输入文章内容', // 提示
        callbacks : { // 回调函数
            // 上传图片时使用的回调函数
            onImageUpload : function(files) {
                // 具体的上传图片方法
                uploadImages(files);
            }
        },
        // summernote自定义配置
        toolbar: [
          ['operate', ['undo','redo']],
          ['magic',['style']],
          ['style', ['bold', 'italic', 'underline', 'clear']],
          ['para', ['height','fontsize','ul', 'ol', 'paragraph']],
          ['font', ['strikethrough', 'superscript', 'subscript']],
          ['color', ['color']],
          ['insert',['picture','video','link','table','hr']],
          ['layout',['fullscreen','codeview']],
        ]
    })
    // summernote具体的上传图片方法
    function uploadImages(files) {
        // 这里files是因为我设置了可上传多张图片，所以需要依次添加到formData中
        // 进度条
        $("#loadingText").html("正在上传图片...0%");
        $("#loadingToast").show();
        // 上传图片的form
        var formData = new FormData();
        for (f in files) {
            formData.append("file", files[f]);
        }
        // XMLHttpRequest 对象
        var xhr = new XMLHttpRequest();
        xhr.open("post", 'uploadImage', true);
        xhr.onreadystatechange = function(){
            if(xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200){
                console.info("上传完成");
                var result = JSON.parse(xhr.responseText);
                console.info(result);
                if (result!=null) {
                    /* for (i in result) {
	                    // 调用insertImage将上传后的图片插入summernote编辑器中
	                    mySummernote.summernote('insertImage',result[i].url, result[i].fileName);
                    } */
                    for(var i=0;i<result.length;i++){
                    	// 调用insertImage将上传后的图片插入summernote编辑器中
	                    mySummernote.summernote('insertImage',result[i].url);
                    }
                    $("#loadingToast").hide();
                }else{
                    $("#loadingToast").hide();
                    toastr.error("图片上传失败：" + result);
                    console.info("上传失败");
                }
            }
        };
        xhr.upload.addEventListener("progress", progressFunction, false);
        xhr.send(formData);
    }
    // 进度条
    function progressFunction(evt) {
        if (evt.lengthComputable) {
            var completePercent = Math.round(evt.loaded / evt.total * 100)+ "%";
            // console.info(completePercent);
            $("#loadingText").html("正在上传图片..." + completePercent);
            if(completePercent=="100%"){
                $("#loadingText").html("图片上传成功,正在处理");
            }
        }
    };
    /* var ctx = $("#ctx").val().trim(); */
    $("#publishArticleBtn").click(function(){
        var name=$("#articleName").val().trim();
        if(name.length==0){
            NodeFocus($("#articleName"));
            return ;
        }
        if (mySummernote.summernote('isEmpty')) {
            toastr.error('请输入文章内容');
            return;
        }
        var content = mySummernote.summernote('code');
        alert("文章内容<br>"+content);
    })
});