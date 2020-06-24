

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

for (key in marker_list){
    var btn = new ButtonClass(marker_list[key], key);
};

document.getElementById('shoplist').addEventListener('click', function(e){
    console.log(e.target);
    if(e.target.type === "button"){
        removeAllMarker();
        var position = new naver.maps.LatLng(marker_list[e.target.id].bldg_lat, marker_list[e.target.id].bldg_lng);
        var marker = addMarker(position, e.target.id);
        markers.push(marker);
        obj_map.setCenter(position);
    }
    else{

    }
});
