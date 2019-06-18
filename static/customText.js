$(document).ready(function() {
    $('form').submit(function(e) {
        e.preventDefault();
        let text = $('textarea').val();
        console.log('1');
        $.get("/customTextAnalyse", {text: text}, function(data, status) {
            console.log(data, text);
            drawGraph(data.polarity, data.subjectivity, "Text Sentiment");
        });
    });
});