$('document').ready(function(){

	$('.bxslider').bxSlider();

	$('.mobile-nav-link').on('click',function(){

		  $( ".nav-wrapper.for-mobile > ul" ).animate({
			    right: "0",
			}, 500);
	});

	$('.close-menu-link').on('click',function(){

	  	$( ".nav-wrapper.for-mobile > ul"  ).animate({
		    right: "-300",
		}, 500);

	});

	//Scroll Down
	$('#scoll_down').click(function() {       
       $("html, body").animate({
         scrollTop: $('#About_us').offset().top
    }, 800);
    });
    
   $("#contact_name").on("blur", function() {
       var regex = /^[a-zA-Z\s]+$/;
       if (regex.test($("#contact_name").val())) {
            
        } else {
            alert("Please enter a valid name");
        }
    });

	if($(window).width() === 320)
		{
			$(".niceFileInput").niceFileInput({  
			'width'  : '300'	
			});
		}
	else{
		$(".niceFileInput").niceFileInput({  
			'width'  : '400'	
		});
	}	
	initializeMap(); // contact page google map
});

function initializeMap() {
  var coviamLatLng = {lat: 12.917355, lng: 77.648843};

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 14,
    center: coviamLatLng
  });

  var marker = new google.maps.Marker({
    position: coviamLatLng,
    map: map,
  });
}

$( window ).scroll(function(){

	if($(window).scrollTop() > 260)
	{
		$('.chart').easyPieChart( { 
				size : 			165, 
				lineWidth : 	7, 
				lineCap : 		'square', 
				animate : 		1500, 
				scaleColor : 	false, 
				trackColor : 	false, 
				barColor : function () { 
					return $(this.el).data('bar-color');
				},
				onStep: function(from, to, percent) {
					var this_percent = $(this.el).data('percent');
					
					$(this.el).next().find('.counter').text(this_percent + "%");
				}
			} );
	}	  
});













