
$(function(){

	// basic usage
	$('a.normalTip').aToolTip();

	
	// List of all paramaters and their default values:
	$('a').aToolTip({

		toolTipClass: 'aToolTip',			// Set custom class for tooltip
		xOffset: 3,							// x Position
		yOffset: 3							// y position
	});
	
});


$(document).ready(function() {

	$("#topnav li").hover(function() { //Hover over event on list item
		$(this).css({ 'background' : '#1376c9 url(topnav_active.gif) repeat-x'}); //Add background color and image on hovered list item
		/*$(this).find("span").show(); //Show the subnav*/
	} , function() { //on hover out...
		$(this).css({ 'background' : 'none'}); //Ditch the background
		/*$(this).find("span").hide(); //Hide the subnav*/
	});

});

$(function () {
	$('form').submit(function () {
		$('input[type="submit"]', this).replaceWith('<p><strong>Processing...Please wait</strong></p>'); 
		});
	});
	
	
$(document).ready(function () {
            $('.vote').hover(
            function () {
                $(this).animate({
                    fontSize: '16pt'
                }, "fast");
            },
            function () {
                $(this).animate({
                    fontSize: '8pt'
                }, "fast");
            });
            
    });