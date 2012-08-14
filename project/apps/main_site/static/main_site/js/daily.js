
var formSaveTimeout;
var saveFadeoutTimeout;
var firstSave = true;
$(function(){
	$(".sleep_field input").timeEntry({
		'spinnerImage':'',
		'defaultTime': '10:00AM'
	});
	$(".sleep_field input").each(function(){
		$ele = $(this);
		$ele.focus().blur();
	});
	
	$("input, textarea").change(queueFormSave)
	$(".hours input").change(hoursChanged)
	$('form').ajaxForm({
		success: saveSuccess,
	});
	$(".hours").each(function(){
		calculateHours($(this));
	});
	
	
});

function queueFormSave(e) {
	// saving...
	clearTimeout(formSaveTimeout);
	var $ele = $(e.target);
	var $form = $ele.parents("form");
	formSaveTimeout = setTimeout(function(){saveForm($form);}, 1500);
}
function saveForm(form) {
	clearTimeout(formSaveTimeout);
	clearTimeout(saveFadeoutTimeout);
	$("#status").stop().show().html(ich.saving())
	form.submit();
}

function saveSuccess(json) {

	if (json.success) {
		$("#status").html(ich.saved());	
	} else {
		$("#status").html(ich.errored());	
	}
	updateSleepHours();
	
	saveFadeoutTimeout = setTimeout(function(){$("#status").fadeOut();}, 2000);
}

function updateSleepHours() {
	$(".section.hours").each(function(){
		$section = $(this);
		$.ajax({
			url: $(".sleep", $section).attr("update_url"),
			success: function(json){
				$("#gb_" + json.id + " .sleep .number").html(json.sleep_hrs);
			}
		})
	})
}

function hoursChanged(e) {
	$ele = $(e.target);
	$hours = $ele.parents(".hours");
	calculateHours($hours);
}
function roundNumberWithDec(num, dec) {
	return Math.round( Math.round( num * Math.pow( 10, dec + 1 ) ) / Math.pow( 10, 1 ) ) / Math.pow(10,dec);
}
function roundPretty(num) {
	var roundLen = 1;
	var rem = (num % 1) * 100;
	if (rem == 25 || rem == 75) {
		roundLen = 2;
	}
	if (rem == 0) {
		roundLen = 0;
	}
	return roundNumberWithDec(num,roundLen)
}
function calculateHours(hoursBlock) {
	var hours = 0;
	$(".day_hours input", hoursBlock).each(function(){
		hours += parseFloat($(this).val(),10);
	});
	hours = roundPretty(hours);
	var fell_asleep_time = $(".fell_asleep input", hoursBlock).val();
	var woke_up_time =  $(".woke_up input", hoursBlock).val();
	
	fell_asleep_math_time = parseFloat(fell_asleep_time.substr(0,2)) + (parseInt(fell_asleep_time.substr(3,2))/60)
	if (fell_asleep_time.substr(5,2) == "PM") {
		fell_asleep_math_time += 12;
	}
		

	woke_up_math_time = parseFloat(woke_up_time.substr(0,2)) + (parseInt(woke_up_time.substr(3,2))/60)
	if (woke_up_time.substr(5,2) == "PM") {
		woke_up_math_time += 12;
	}

	if (fell_asleep_math_time < woke_up_math_time) {
		fell_asleep_math_time += 24;	
	}
	

	total_hours_awake = roundPretty(fell_asleep_math_time - woke_up_math_time);
	$(".total", hoursBlock).html(hours + "/" + total_hours_awake);
}