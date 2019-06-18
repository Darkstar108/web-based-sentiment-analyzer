$(document).ready(function() {

    $('form').submit(function(e) {
        e.preventDefault();
        let subreddit = $('input').val();

        // Validate Inputs
        $.get("/redditValidate", {subreddit: subreddit}, function(data, status) {
            console.log(data)
            
            if(data.exists === 'F') {
                $('#subredditValidate').html('Subreddit not found');
            }
            // If valid, then analyse subreddit
            else {
                $('#subredditValidate').empty();
                let timeframe = $('select').val();

                $.get("/redditAnalyse", {subreddit: subreddit, timeframe: timeframe}, function(data, status) {
                    console.log(data);
                    drawGraph(data.polarity, data.subjectivity, "Subreddit Sentiment");
                });
            }
        }, 'json'); 
    })
});