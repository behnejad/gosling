/**
 * Created by hooman on 19-Nov-15.
 */

var radioAnswers = 0, radio = false, innerRadioAnswer = 0, ids = [], radioStat = {};
for (var i = 65; i <= 90; ++i) {
	ids.push(String.fromCharCode(i));
	ids.push(String.fromCharCode(i + 32));
}
function initradioAnswers() {
	if (!radio) {
		$('<ol class="radio-answers"></ol>').clone().hide().prependTo('div.radio-answers').slideDown('fast');
		radio = true;
	}
}
$('a.radio-answer').click(function () {
	initradioAnswers();
	var parent = ids[2 * radioAnswers], child = ids[2 * innerRadioAnswer + 1];
	temp = `<li class="radio-answer" id="` + parent + `">
				<input class="addproblem radio-title" id="` + parent + `" placeholder="متن صورت سوال">
				<ul class="radio-answer-` + parent + `">
					<li class="radio-inner-answer" id="` + child + `">
					<input class="addproblem radio-answer" line="` + child + `" parent="` + parent + `" type="text" placeholder="متن گزینه">
					</li>
				</ul>
				<a class="label label-danger pak-radio-answer" id="` + parent + `">حذف سوال</a>
				<hr>
			</li>`;
	$(temp).clone().hide().appendTo('ol.radio-answers').slideDown('fast');
    radioStat[parent] = {};
    radioStat[parent][child] = false;
	++radioAnswers;
	++innerRadioAnswer;
});
$(document).on('click', 'a.pak-radio-answer', function () {
	$('li.radio-answer#' + $(this).attr('id')).slideUp('fast', function () {
		$(this).remove();
	});
});
$(document).on('change', 'input.addproblem', function () {
	if ($(this).val() && radioStat[$(this).attr('parent')][$(this).attr('line')] == false) {
		$(`<li class="radio-inner-answer" id="` + ids[2 * innerRadioAnswer + 1] + `">
	        <input class="addproblem radio-answer" line="` + ids[2 * innerRadioAnswer + 1] +
			`" parent="` + $(this).attr('parent') + `" type="text" placeholder="متن گزینه"></li>`)
			.clone().hide().appendTo('ul.radio-answer-' + $(this).attr('parent')).slideDown('fast');
        radioStat[$(this).attr('parent')][$(this).attr('line')] = true;
		radioStat[$(this).attr('parent')][ids[2 * innerRadioAnswer + 1]] = false;
        ++innerRadioAnswer;
	}
    else if (!$(this).val() && radioStat[$(this).attr('parent')][$(this).attr('line')] == true){
        $('li.radio-inner-answer#' + $(this).attr('line')).slideUp('fast', function () {
			$(this).remove();
		});
    }
    else {
        radioStat[$(this).attr('parent')][$(this).attr('line')] = true;
    }
});
$(document).ready(function () {
	window.CKEDITOR_BASEPATH = '/statics/ckeditor/ckeditor/';
	$.getScript('/statics/ckeditor/ckeditor/ckeditor.js', function () {
		CKEDITOR.replace('problem');
	});
});
