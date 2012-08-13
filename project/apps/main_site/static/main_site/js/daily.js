
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
function calculateHours(hoursBlock) {
	var hours = 0;
	$("input", hoursBlock).each(function(){
		hours += parseFloat($(this).val(),10);
	});
	hours = Math.round(hours);
	// $(".total", hoursBlock).html(hours);
}