

// button 동적 이벤트 바인딩


var ButtonClass = class {
    constructor(model, id) {
        this.shop_name = model.shop_name;
        this.bldg_lat = model.bldg_lat;
        this.bldg_lng = model.bldg_lng;
        this.bldg_name = model.bldg;
        this.btn_id = id;
        this.target = 'shoplist';

        this.btn = document.createElement('input');
        this.btn.setAttribute('type', 'button');
        this.btn.setAttribute('id', id);
        this.btn.setAttribute('style', 'background-color:white; border:1.5px #797979; border-radius:5px; outline-color:#90cc90; font-size:18px; color:#409040;');
        this.btn.setAttribute('value', this.shop_name);

        document.getElementById(this.target).appendChild(this.btn);
        document.write('<p style="font-size:12px; color:gray">');
        document.write(this.bldg_name+'<br>'+'</p>');
    }
}

for (key in shop_info_list){
    var btn = new ButtonClass(shop_info_list[key], key);
};

document.getElementById('shoplist').addEventListener('click', function(e){
    console.log(e.target);
    if(e.target.type === "button"){
        var position = new naver.maps.LatLng(shop_info_list[e.target.id].bldg_lat, shop_info_list[e.target.id].bldg_lng);
        obj_map.setCenter(position);
        removeAllMarker();
        removeAllCluster();
        var htmlMarker_pink = {
            content: '<div style="cursor:pointer;width:35px;height:35px;line-height:52px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(/static/img/map-marker-2.png);background-size:contain;"></div>',
            size: new naver.maps.Size(40, 40),
            anchor: new naver.maps.Point(20, 20)
        };
        addMarker_img(position, e.target.id, htmlMarker_pink);

    }
    else{

    }
});

