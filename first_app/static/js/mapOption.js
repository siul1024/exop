

document.write('<scr'+'ipt src="http://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=4uq9o7p9kq"></scr'+'ipt>');

//<script src="http://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=4uq9o7p9kq"></script>

var mapOptions = {
                    center: new naver.maps.LatLng(37.402799, 127.111505),
                    zoom:17,
                    minZoom: 14,
                    maxBounds: new naver.maps.LatLngBounds(
                        new naver.maps.LatLng(37.393587, 127.096515),
                        new naver.maps.LatLng(37.415317, 127.138466)
                    ),
                };

                var map = new naver.maps.Map('map', mapOptions);

                // 지도에 마커 생성.
                for (var key in marker_list){
                    var marker = new naver.maps.Marker({
                        position: new naver.maps.LatLng(marker_list[key].bldg_lat, marker_list[key].bldg_lng),
                        title: marker_list[key].shop_name,
                        map: map
                    });
                };

