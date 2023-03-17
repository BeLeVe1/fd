var map,point;
var searchCon = "店";

$(function(){

	// 初始化百度地图 
	map = new BMap.Map("merchant-location-content", {enableMapClick:false});
	if(typeof(x_pos) != "undefined" && typeof(y_pos) != "undefined"){
		point = new BMap.Point(x_pos , y_pos );
	} else {
		point = new BMap.Point(116.413063,39.911042);
	}

	map.panTo(point);
	
	map.centerAndZoom(point,19);
	map.enableScrollWheelZoom(true);
 	map.enableDragging();   
	
 	$("#map-pin").css("margin-top", $("#merchant-location-content").height() / 2 - 29 );
 		
 	if(typeof(x_pos) == "undefined" || typeof(y_pos) == "undefined"){
	 	goToCurrLocation(function(){
	 		searchNearBy(searchCon);
	 	});
 	}
	
 	// 添加定位控件
  	var geolocationControl = new BMap.GeolocationControl();
  	geolocationControl.addEventListener("locationSuccess", function(e){
  		map.centerAndZoom( e.point,19);
  		moveToLocation(e.point);
    	point = e.point;
  	});
  	geolocationControl.addEventListener("locationError",function(e){
    	alert(e.message);
  	});
 	map.addControl(geolocationControl);
 	
 	// 添加地图点击定位功能
//	map.addEventListener("click",function(e){
//		point = e.point;
//		moveToLocation(point);
//		searchNearBy(searchCon);
//	}); 
 	
 	// moving
 	map.addEventListener("moveend",function(e){
		point = map.getCenter();
		if (!relocation){
			searchNearBy(searchCon);
		} else {
			relocation = false;
		}
			
 	});
	
	$("#merchant-location-submit> button").click(function(){
		if (point) {
			backMerchant();
		}
	});
});

function mySearch(e, tar){
	if(event.keyCode == "13")  {  
     var thing = $(tar).val();
     $(tar).val("");
     $(tar).blur();
     if (thing != ""){
     	searchCon = thing;
     	search(thing);
     }
   }  
}

function searchLocation(e ,tar) {
	 var inp = $(tar).next();
	 var thing = $(inp).val();
     $(inp).val("");
     if (thing != ""){
     	searchCon = thing;
     	search(thing);
     }
}
	
// 在附近搜索	
function searchNearBy(thing) {
	var options = {
		onSearchComplete: function(results){
			
			// 判断状态是否正确
			if (local.getStatus() == BMAP_STATUS_SUCCESS){
				$("#merchant-location-footer").html("");
				for (var i = 0; i < results.getCurrentNumPois(); i ++){
					var div = $('<div class="rec-location btn" id="no-' + i +'"></div>');
					var title = $('<div class="rec-location-title">'+ results.getPoi(i).title +'</div>');
					var address = $('<div class="rec-location-address">'+ results.getPoi(i).address +'</div>');
					div.html(title);
					div.append(address);
					
					if (i == 0) {
						title.prepend("[推荐位置]");
						div.addClass("rec-location-first");
					}
					$("#merchant-location-footer").append(div);
					
				}
				
				$(".rec-location").click(function(e){
					recLocationClick(e, results);
				});
			}
		}
	};
	var local = new BMap.LocalSearch(map, options);
	local.searchNearby(thing , point,200);
}

function search(thing) {
	var options = {
		onSearchComplete: function(results){
			
			// 判断状态是否正确
			if (local.getStatus() == BMAP_STATUS_SUCCESS){
				$("#merchant-location-footer").html("");
				for (var i = 0; i < results.getCurrentNumPois(); i ++){
					var div = $('<div class="rec-location btn" id="no-' + i +'"></div>');
					var title = $('<div class="rec-location-title">'+ results.getPoi(i).title +'</div>');
					var address = $('<div class="rec-location-address">'+ results.getPoi(i).address +'</div>');
					div.html(title);
					div.append(address);
					if (i == 0) {
						title.prepend("[推荐位置]");
						div.addClass("rec-location-first");
						moveToLocation(results.getPoi(i).point);
					}
					$("#merchant-location-footer").append(div);
				}
				
				$(".rec-location").click(function(e){
					recLocationClick(e, results);
				});
			}
		}
	};
	
	var local = new BMap.LocalSearch(map, options);
	local.search(thing , point,200);
}

var relocation = false;
function recLocationClick(e, results){
	relocation = true;
	
	var tar = $(e.target).parent().eq(0);
	var no = $(tar).prop("id").split("-")[1];
	moveToLocation(results.getPoi(no).point);
	
	$(".rec-location-first").removeClass("rec-location-first");
	tar.addClass("rec-location-first");
} 

function moveToLocation(pt){
	point = pt;
	map.panTo(pt);
}

// 定位当前位置
function goToCurrLocation(func){

	var geolocation = new BMap.Geolocation();
	geolocation.getCurrentPosition(function(r){
			if(this.getStatus() == BMAP_STATUS_SUCCESS){
				moveToLocation(r.point);
				if (func)
					func();
			}
			else {
				alert('failed'+this.getStatus());
			}        
		}, function(error){
			switch(error.code){
				case error.TIMEOUT :
					alert( " 连接超时，请重试 " );
					break;
				case error.PERMISSION_DENIED :
					alert( " 您拒绝了使用位置共享服务，查询已取消 " );
					break;
				case error.POSITION_UNAVAILABLE : 
					alert( " 亲爱的火星网友，非常抱歉，我们暂时无法为您所在的星球提供位置服务 " );
					break;
			}
		},  {enableHighAccuracy: true, timeout: 5000, maximumAge:60000});
}

function backMerchant(){
	//WeixinJSBridge.call("closeWindow");
	$("#location-point").html(point.lng + "-" + point.lat);
	$("#mapaddressy").val(point.lat);
	$("#mapaddressx").val(point.lng);
	$(".merchant-mask").remove();
	showMain();
	$("#merchant-location").css("z-index", "-1");
}  

