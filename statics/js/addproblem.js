/**
 * Created by hooman on 19-Nov-15.
 */

var radio = false, radioAnswers = 0, innerRadioAnswer = 0, ids = [], radioStat = {};
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
$(document).on('click', 'a.radio-answer', function () {
    initradioAnswers();
    var parent = ids[2 * radioAnswers], child = ids[2 * innerRadioAnswer + 1];
    temp = `<li class="radio-answer" id="` + parent + `">
				<input class="addproblem radio-title" id="` + parent + `" placeholder="متن سوال">
				<ul class="radio-answer-` + parent + `">
					<li class="radio-inner-answer" id="` + child + `">
					<input class="addproblem radio-answer" line="` + child + `" parent="` + parent + `" type="text" placeholder="متن گزینه">
					</li>
				</ul>
				<a class="label label-danger pak-radio-answer hide" id="` + parent + `">حذف سوال</a>
				<hr>
			</li>`;
    $(temp).clone().hide().appendTo('ol.radio-answers').slideDown('fast');
    radioStat[parent] = {};
    radioStat[parent][child] = false;
    ++radioAnswers;
    ++innerRadioAnswer;
});
$('a.radio-answer').trigger("click");
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
    else if (!$(this).val() && radioStat[$(this).attr('parent')][$(this).attr('line')] == true) {
        $('li.radio-inner-answer#' + $(this).attr('line')).slideUp('fast', function () {
            $(this).remove();
        });
    }
    else {
        radioStat[$(this).attr('parent')][$(this).attr('line')] = true;
    }
});
var short = false, shortAnswers = 0;
function initShortAnswer() {
    if (!short) {
        $('<ol class="short-answers"></ol>').clone().hide().prependTo('div.short-answers').slideDown('fast');
        short = true;
    }
}
$('a.short-answer').click(function () {
    initShortAnswer();
    var parent = ids[2 * shortAnswers];
    temp = `<li class="short-answer" id="` + parent + `">
				<input class="addproblem short-title" id="` + parent + `" placeholder="متن سوال">
				<a class="label label-danger pak-short-answer" id="` + parent + `">حذف سوال</a>
				<hr>
			</li>`;
    $(temp).clone().hide().appendTo('ol.short-answers').slideDown('fast');
    ++shortAnswers;
});
$(document).on('click', 'a.pak-short-answer', function () {
    $('li.short-answer#' + $(this).attr('id')).slideUp('fast', function () {
        $(this).remove();
    });
});
var long = false, longAnswers = 0;
function initLongAnswer() {
    if (!long) {
        $('<ol class="long-answers"></ol>').clone().hide().prependTo('div.long-answers').slideDown('fast');
        long = true;
    }
}
$('a.long-answer').click(function () {
    initLongAnswer();
    var parent = ids[2 * longAnswers];
    temp = `<li class="long-answer" id="` + parent + `">
				<input class="addproblem long-title" id="` + parent + `" placeholder="متن سوال">
				<a class="label label-danger pak-long-answer" id="` + parent + `">حذف سوال</a>
				<hr>
			</li>`;
    $(temp).clone().hide().appendTo('ol.long-answers').slideDown('fast');
    ++longAnswers;
});
$(document).on('click', 'a.pak-long-answer', function () {
    $('li.long-answer#' + $(this).attr('id')).slideUp('fast', function () {
        $(this).remove();
    });
});
$('#clean').click(function () {
    CKEDITOR.instances['problem'].setData('');
    $('div.radio-answers').slideUp('fast', function () {
        $(this).html('');
        $(this).slideDown('fast');
    });
    $('a.radio-answer').trigger("click");
});
$('button#submit').click(function () {
    var ans = '';
    $('input.radio-answer').each(function (){
        if ($(this).val() != '')
            ans += $(this).val() + '|';
    });
    $.ajax({
        type: "post",
        url: "",
        data: {final: true, index: state, text: CKEDITOR.instances['problem'].getData(),
                question: $('input.radio-title').val(), answers: ans, csrftoken: $.cookie("csrftoken"),
                csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val()},
        success: function (data, textStatus, jqXHR) {
            console.log('asd');
            console.log(data);
                if (data == "ok") {
                    alert("سوال ثبت شد");
                    window.location.assign('/profile/');
                }
                else
                    alert("خطا در ایجاد سوال");
                change_contest(1);
            }
    });
});
$(document).ready(function () {
    window.CKEDITOR_BASEPATH = '/statics/ckeditor/ckeditor/';
    $.getScript('/statics/ckeditor/ckeditor/ckeditor.js', function () {
        CKEDITOR.replace('problem');
    });
});
