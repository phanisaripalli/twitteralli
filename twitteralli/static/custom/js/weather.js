
if ("geolocation" in navigator) {
  $('.js-geolocation').show(); 
} else {
  $('.js-geolocation').hide();
}

forecast = []
geo_location = "Berlin"

/* Where in the world are you? */
$('.js-geolocation').on('click', function() {
  navigator.geolocation.getCurrentPosition(function(position) {
    loadWeather(position.coords.latitude+','+position.coords.longitude); //load weather using your lat/lng coordinates
  });
});



$(document).ready(function() {    
  loadWeather("Berlin", '');   
});

function loadWeather(location, woeid) {
  geo_location = location
  $.simpleWeather({
    location: location,
    woeid: woeid,
    unit: 'c',
    success: function(weather) {
      html = '<h2><i class="icon-'+weather.code+'"></i> '+weather.temp+'&deg;'+weather.units.temp+'</h2>';
      html += '<ul><li>'+weather.city+', '+weather.region+'</li>';
      html += '<li class="currently">'+weather.currently+'</li>';      
      
      $("#weather").html(html);
      forecast[0] = ['Day', 'Min', 'Max', 'Avg.']
      for(var i=0;i<7;i++) {        
        forecast[i+1] = [weather.forecast[i].day, parseInt(weather.forecast[i].low), parseInt(weather.forecast[i].high), (parseInt(weather.forecast[i].low) + parseInt(weather.forecast[i].high))/2]        
      }            
    },
    error: function(error) {
      $("#weather").html('<p>'+error+'</p>');
    }
  });   
}


