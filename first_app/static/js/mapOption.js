
window.onload = function(){


    var mapOptions = {
        center: new naver.maps.LatLng(37.402799, 127.111505),
        zoom:17,
        minZoom: 15,
        maxZoom: 19,
        maxBounds: new naver.maps.LatLngBounds(
            new naver.maps.LatLng(37.393587, 127.096515),
            new naver.maps.LatLng(37.415317, 127.138466),
        ),
    };

    obj_map = new naver.maps.Map('map', mapOptions);

    var htmlMarker = {
        content: '<div style="cursor:pointer;width:50px;height:50px;line-height:52px;font-size:15px;color:white;text-align:center;font-weight:bold;background:url(/static/img/cluster-marker-2.png);background-size:contain;"></div>',
        size: new naver.maps.Size(40, 40),
        anchor: new naver.maps.Point(20, 20)
    };
    var htmlMarker_blue = {
        content: '<div style="cursor:pointer;width:35px;height:35px;line-height:52px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(/static/img/map-marker-1.png);background-size:contain;"></div>',
        size: new naver.maps.Size(40, 40),
        anchor: new naver.maps.Point(20, 20)
    };

    for (var key in shop_info_list){
        var position = new naver.maps.LatLng(shop_info_list[key].bldg_lat, shop_info_list[key].bldg_lng);
        addMarker_img(position, key, htmlMarker_blue);
    };



    markerClustering = new MarkerClustering({
        minClusterSize: 2,
        maxZoom: 20,
        markers: markers,
        map: obj_map,
        disableClickZoom: false,
        gridSize: 100,
        icons: [htmlMarker, ],
        indexGenerator: [10,],// 100, 200, 500, 1000],
        stylingFunction: function(clusterMarker, count) {
            $(clusterMarker.getElement()).find('div:first-child').text(count);
        }
    });
}

function addMarker(position, id){
    var marker = new naver.maps.Marker({
        position: position,
        map: obj_map,
        title: shop_info_list[id].shop_name,
        animation: naver.maps.Animation.BOUNCE,
    });
    marker.setMap(obj_map);
    markers.push(marker);
    return marker;
}


function addMarker_img(position, id, html_marker){
    var marker = new naver.maps.Marker({
        position: position,
        map: obj_map,
        icon: html_marker,
        title: shop_info_list[id].shop_name,
        animation: naver.maps.Animation.BOUNCE,
    });
    marker.setMap(obj_map);
    markers.push(marker);
    return marker;
}


function removeAllMarker(){
    for( var i=0; i<markers.length; i++){
        markers[i].setMap(null);
    };
    markers = [];
}

function removeAllCluster(){
    for( var i=0; i<markerClustering._clusters.length; i++){
        markerClustering._clusters[i].destroy();
    }
    markerClustering._clusters = [];
}
