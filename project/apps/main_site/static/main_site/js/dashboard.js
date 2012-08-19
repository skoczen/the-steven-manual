$(function(){

	$(".measurement.gauge").each(function(){
		$ele = $(this);
		var opts = {
		  lines: 12, // The number of lines to draw
		  angle: 0.15, // The length of each line
		  lineWidth: 0.44, // The line thickness
		  pointer: {
		    length: 0.9, // The radius of the inner circle
		    strokeWidth: 0.035, // The rotation offset
		    color: '#000000' // Fill color
		  },
		  colorStart: '#6FADCF',   // Colors
		  colorStop: '#8FC0DA',    // just experiment with them
		  strokeColor: '#E0E0E0',   // to see which ones work best for you
		  generateGradient: true
		};
		
		var target = document.getElementById($ele.attr("linked_canvas")); // your canvas element
		var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
		gauge.maxValue = 10; // set max gauge value
		gauge.animationSpeed = 32; // set animation speed (32 is default value)
		gauge.set(parseFloat($ele.attr("value"))); // set actual value
	});

// presence_trend
// happiness_trend
// creativity_trend
// morning_mood_trend
// sleep_health
// work_health
// alone_health
// friend_health
// public_health
// relationship_health
// meditated_status
// off_status
// worked_out_status
// left_the_house_status
// nature_time_status
});