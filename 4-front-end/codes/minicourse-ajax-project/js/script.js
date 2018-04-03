var api_key = 'AIzaSyDTXGv-LXkI-S8ZfHcqPjxyoV39gK2ZQQs';

function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview
    street = $("#street").val();
    city = $("#city").val();
    url = "https://maps.googleapis.com/maps/api/streetview?size=400x400&location=" + street + " " + city +
        "&fov=90&heading=235&pitch=10\n" + "&key=" + api_key;
    $body.append('<img class="bgimg" src="' + url + '">');

    // YOUR CODE GOES HERE!
    var url = "https://api.nytimes.com/svc/topstories/v2/home.json";
    url += '?' + $.param({
        'api-key': "22aee1631d704001922d2e124315d8b6"
    });
    $.ajax({
        url: url,
        method: 'GET',
    }).done(function (result) {
        $("#nytimes-header").text("New York Times Articles")
        posts = result.results;
        for (var i = 0; i < posts.length; i++) {
            $("#nytimes-articles").append(
                "<li class='article'>" +
                "<a href='" + posts[i].url + "'>" + posts[i].title + "</a>" +
                "<p>" + posts[i].abstract + "</p>" +
                "</li>")
        }
    }).fail(function (err) {
        $("#nytimes-header").text("New York Times Articles could not be loaded")
        $("#nytimes-articles").text("");
        throw err;
    });

    // Involve WikiPedia API
    $.ajax({
        url: 'https://en.wikipedia.org/w/api.php?action=opensearch&search=' + city + '&limit=10&namespace=0&format=json',
        dataType: 'jsonp',
        success: function (data) {
            var keywords = data[1];
            var urls = data[3];
            for (var i = 0; i < keywords.length; i++) {
                $("#wikipedia-links").append("" +
                    "<li>" +
                    "<a href='"+urls[i]+"'>"+keywords[i]+"</a>" +
                    "</li>")
            }
        }
    });

    return false;
};

$('#form-container').submit(loadData);
