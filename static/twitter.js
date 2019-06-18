$(document).ready(function() {
    // Toggle between user and topic
    $('select').change(function() {
        console.log($('select').val())
        if($('select').val() == "user") {
            $('#tweetTopic').hide();
            $('#tweetUser').show();
        }
        else {
            $('#tweetTopic').show();
            $('#tweetUser').hide();
        }
    });

    $('form').submit(function(e) {
        e.preventDefault();
        let key, value;
        if($('select').val() == "user") {
            key = "user";
            value = $('#tweetUser input').val();
        }
        else {
            key = "topic";
            value = $('#tweetTopic input').val();
        }

        // Validate Inputs
        $.get("/twitterValidate", {key: key, value: value}, function(data, status) {
            console.log(data)
            
            if(data.exists === 'F') {
                if(key === 'user') {
                    $('#userValidate').html('User not found');
                }
                else {
                    $('#topicValidate').html('No tweets in topic');
                }
            }
            // If valid, then analyse subreddit
            else {
                $('#userValidate').empty()
                $('#topicValidate').empty();

                let count = $('#numTweets').val();
                console.log(value, count)

                $.get("/twitterAnalyse", {key: key, value: value, count: count}, function(data, status) {
                    console.log(data);
                    drawGraph(data.polarity, data.subjectivity, "Tweets Sentiment");
                });
            }
        }, 'json'); 
    })
});