

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
    // 지도에 마커 생성
    for (var key in marker_list){
        var marker = new naver.maps.Marker({
            position: new naver.maps.LatLng(marker_list[key].bldg_lat, marker_list[key].bldg_lng),
            title: marker_list[key].shop_name,
            map: obj_map
        });
    };
}
