
function onPageLoad() {
    console.log( "Document loaded" );
    var url_district = "http://127.0.0.1:7000/get_district_names"; 
    var url_direction = "http://127.0.0.1:7000/get_direction_names"
    var url_balcony = "http://127.0.0.1:7000/get_balcony_names"

    $.get(url_district, function(data, status) {
        console.log("got response for get_district_names request");
        if(data) {
            var items = data.districts;
            var uiDistrict = document.getElementById("uiDistrict");
            $('#uiDistrict').empty();
            
            for(var i in items) {
                var opt = new Option(items[i]);
                $('#uiDistrict').append(opt);
            }
        }
    });

    $.get(url_direction, function(data, status) {
        console.log("got response for get_district_names request");
        if(data) {
            var items = data.directions;
            var uiDirection = document.getElementById("uiDirection");
            $('#uiDirection').empty();
            
            for(var i in items) {
                var opt = new Option(items[i]);
                $('#uiDirection').append(opt);
            }
        }
    });

    $.get(url_balcony, function(data, status) {
        console.log("got response for get_district_names request");
        if(data) {
            var items = data['balcony directions'];
            var uiBalcony = document.getElementById("uiBalcony");
            $('#uiBalcony').empty();
            
            for(var i in items) {
                var opt = new Option(items[i]);
                $('#uiBalcony').append(opt);
            }
        }
    });
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    
    var area = document.getElementById("uiArea").value;
    var frontage = document.getElementById("uiFrontage").value;
    var access_road = document.getElementById("uiRoad").value;
    var floors = document.getElementById("uiFloors").value;
    var bedrooms = document.getElementById("uiBed").value;
    var bathrooms = document.getElementById("uiBath").value;
    var direction = document.getElementById("uiDirection").value;
    var balcony = document.getElementById("uiBalcony").value;
    var district = document.getElementById("uiDistrict").value;
    
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:7000/predict_house_price";

    $.ajax({
        url: url,
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            "area": parseFloat(area),
            "frontage": parseFloat(frontage),
            "access_road": parseInt(access_road),
            "floors": parseInt(floors),
            "bedrooms": parseInt(bedrooms),
            "bathrooms": parseInt(bathrooms),
            "direction": direction,
            "balcony": balcony,
            "district": district,
        }),
        success: function(data) {
            console.log(data);
            estPrice.innerHTML = "<h2> Price: " + data.price + "</h2>";
        },
        error: function(xhr, status, error) {
            console.error("Error:", error);
            estPrice.innerHTML = "<h2>Error: Can't call API</h2>";
        }
    });
}

window.onload = onPageLoad;