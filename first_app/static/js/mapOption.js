

window.onload = function(){
    var mapOptions = {
        center: new naver.maps.LatLng(37.402799, 127.111505),
        zoom:17,
        minZoom: 14,
        maxBounds: new naver.maps.LatLngBounds(
            new naver.maps.LatLng(37.393587, 127.096515),
            new naver.maps.LatLng(37.415317, 127.138466),
        ),
    };

    obj_map = new naver.maps.Map('map', mapOptions);
//    // 지도에 마커 생성 >> 클러스터로 변경해주기
    for (var key in marker_list){
        var marker = new naver.maps.Marker({
            position: new naver.maps.LatLng(marker_list[key].bldg_lat, marker_list[key].bldg_lng),
            title: marker_list[key].bldg,
            map: obj_map
        });
        markers.push(marker);
    };
}

function addMarker(position, id){
    var marker = new naver.maps.Marker({
        position: position,
        map: obj_map,
        title: marker_list[id].shop_name,
        animation: naver.maps.Animation.BOUNCE,
    });
    marker.setMap(obj_map);
    return marker;
}

function removeAllMarker(){
    for( var i=0; i < markers.length; i++){
        markers[i].setMap(null);
    };
    markers = [];
}