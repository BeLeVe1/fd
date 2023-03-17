/**
 * Created by ezgoing on 14/9/2014.
 */

"use strict";
(function (factory) {
    if (typeof define === 'function' && define.amd) {
        define(['jquery'], factory);
    } else {
        factory(jQuery);
    }
}(function ($) {
    var cropbox = function(options, el){
        var el = el || $(options.imageBox),
            obj =
            {
        		thresholdlocal:options.thresholdlocal,
                state : {},
                ratio : 1,
                options : options,
                imageBox : el,
                thumbBox : el.find(options.thumbBox),
                spinner : el.find(options.spinner),
                image : new Image(),
                getDataURL: function ()
                {
                    var width = this.thumbBox.width(),
                        height = this.thumbBox.height(),
                        canvas = document.createElement("canvas"),
                        dim = el.css('background-position').split(' '),
                        size = el.css('background-size').split(' '),
                        dx = parseInt(dim[0]) - el.width()/2 + width/2,
                        dy = parseInt(dim[1]) - el.height()/2 + height/2,
                        dw = parseInt(size[0]),
                        dh = parseInt(size[1]),
                        sh = parseInt(this.image.height),
                        sw = parseInt(this.image.width);

                    canvas.width = width;
                    canvas.height = height;
                    var context = canvas.getContext("2d");
                    context.drawImage(this.image, 0, 0, sw, sh, dx, dy, dw, dh);
                    var imageData = canvas.toDataURL('image/png');
                    return imageData;
                },
                getBlob: function()
                {
                    var imageData = this.getDataURL();
                    var b64 = imageData.replace('data:image/png;base64,','');
                    var binary = atob(b64);
                    var array = [];
                    for (var i = 0; i < binary.length; i++) {
                        array.push(binary.charCodeAt(i));
                    }
                    return  new Blob([new Uint8Array(array)], {type: 'image/png'});
                },
                zoomIn: function ()
                {
                	if ( this.ratio > 3)
                		return;
                    this.ratio*=1.1;
                    setBackground();
                },
                zoomOut: function ()
                {
                	var bgsize = $(el).css("background-size");
                	var width = bgsize.substring(0,bgsize.indexOf("px"));
                	if (parseInt(width)/ this.thumbBox.width() < 0.25 )
                		return;
                    this.ratio*=0.9;
                    setBackground();
                }
            },
            setBackground = function()
            {
                var w =  parseInt(obj.image.width)*obj.ratio;
                var h =  parseInt(obj.image.height)*obj.ratio;

                var pw = (el.width() - w) / 2;
                var ph = (el.height() - h) / 2;

                el.css({
                    'background-image': 'url(' + obj.image.src + ')',
                    'background-size': w +'px ' + h + 'px',
                    'background-position': pw + 'px ' + ph + 'px',
                    'background-repeat': 'no-repeat'});
            },
            imgMouseDown = function(e)
            {
                e.stopImmediatePropagation();

                obj.state.dragable = true;
                obj.state.mouseX = e.clientX;
                obj.state.mouseY = e.clientY;
            },
            imgMouseMove = function(e)
            {
                e.stopImmediatePropagation();

                if (obj.state.dragable)
                {
                    var x = e.clientX - obj.state.mouseX;
                    var y = e.clientY - obj.state.mouseY;

                    var bg = el.css('background-position').split(' ');

                    var bgX = x + parseInt(bg[0]);
                    var bgY = y + parseInt(bg[1]);

                    el.css('background-position', bgX +'px ' + bgY + 'px');

                    obj.state.mouseX = e.clientX;
                    obj.state.mouseY = e.clientY;
                }
            },
            imgMouseUp = function(e)
            {
                e.stopImmediatePropagation();
                obj.state.dragable = false;
            },
            zoomImage = function(e)
            {
                e.originalEvent.wheelDelta > 0 || e.originalEvent.detail < 0 ? obj.ratio*=1.1 : obj.ratio*=0.9;
                setBackground();
            }

        obj.spinner.show();
        obj.image.onload = function() {
            obj.spinner.hide();
            setBackground();

			var currX=0,endX=0;
			$(".imageBox").on('touchstart touchmove touchend', function(event){
				
			    var touch1 = event.originalEvent.touches[0] || event.originalEvent.targetTouches[0],  // 第一根手指touch事件
			        touch2 = event.originalEvent.touches[1] || event.originalEvent.targetTouches[1],  // 第二根手指touch事件
			        fingers = event.originalEvent.touches.length;   // 屏幕上手指数量

			    //手指放到屏幕上的时候，还没有进行其他操作
			    if (event.type == 'touchstart') {
			    	event.preventDefault();
			        if (fingers == 2) {
			            // 缩放图片的时候指间距离
			            currX = Math.sqrt( Math.pow(Math.abs(touch1.pageX - touch2.pageX),2) +  Math.pow(Math.abs(touch1.pageY - touch2.pageY),2));
			        }
			        else if (fingers == 1) {
			        	event.clientX = touch1.pageX;
			        	event.clientY =  touch1.pageY;
			        	imgMouseDown(event);
			        }
			
			    }
			    //手指在屏幕上滑动
			  /* else if (event.type == 'touchmove') {
			        if (fingers == 2) {
			            // 缩放图片的时候X坐标滑动变化值
			            endX = Math.abs(touch1.pageX - touch2.pageX);
			           if (endX > currX) {
			        	   cropper.zoomIn();
			           } else if (endX < currX){
			        	   cropper.zoomOut();
			           }*/
			    //手指在屏幕上滑动
			    else if (event.type == 'touchmove') {
			        if (fingers == 2) {
			            // 缩放图片的时候指间距离
			            endX = Math.sqrt( Math.pow(Math.abs(touch1.pageX - touch2.pageX),2) +  Math.pow(Math.abs(touch1.pageY - touch2.pageY),2));
			           if (endX- currX >obj.thresholdlocal) {
			        	   cropper.zoomIn();
			           } else if (currX - endX>obj.thresholdlocal ){
			        	   cropper.zoomOut();
			           }
			        	
			           currX = endX;
			        }else if (fingers == 1) {     	
			        	 event.clientX = touch1.pageX;
			        	 event.clientY = touch1.pageY;
			        	 imgMouseMove(event);
			        }
			    }
			    //手指移开屏幕
			    else if (event.type == 'touchend') {
			    	 if (fingers == 1) {     	
			         	 event.clientX = touch1.pageX;
			         	 event.clientY = touch1.pageY;
			        	 imgMouseUp(event);
			         }
			    	 // 截图
					$('#btnCrop').click();
			    }
			});

            el.bind('mousedown', imgMouseDown);
            el.bind('mousemove', imgMouseMove);
            $(window).bind('mouseup', imgMouseUp);
            el.bind('mousewheel DOMMouseScroll', zoomImage);
        };
        obj.image.src = options.imgSrc;
        el.on('remove', function(){$(window).unbind('mouseup', imgMouseUp)});

        return obj;
    };

    jQuery.fn.cropbox = function(options){
        return new cropbox(options, this);
    };
}));

