
var formSaveTimeout;
var saveFadeoutTimeout;
$(function(){
	$("input").change(queueFormSave)
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
	
	saveFadeoutTimeout = setTimeout(function(){$("#status").fadeOut();}, 2000);
}

function hoursChanged(e) {
	$ele = $(e.target);
	$hours = $ele.parents(".hours");
	calculateHours($hours);
}
function calculateHours(hoursBlock) {
	var hours = 0;
	$("input", hoursBlock).each(function(){
		hours += parseInt($(this).val(),10);
	});
	$(".total", hoursBlock).html(hours);	
}