mapDiv = document.getElementById('map-div');

function unpack(rows, key) {
  return rows.map(function(row) { return row[key]; });
}

var tweets = [{
    type: 'choropleth',
    locationmode: 'country names',
    locations: unpack(rows, 'country'),
    z: unpack(rows, 'number_of_mentions'),
    text: unpack(rows, 'country')
}];

var layout = {
  title: 'Countries mentioned in the tweets of Verisk Maplecroft',
  geo: {
      projection: {
          type: 'robinson'
      }
  },
    xaxis: {domain: [0, 0.45]}
};

Plotly.plot(mapDiv, tweets, layout, {showLink: false});

function triggerEvent(tweetDiv, eventName) {
    var tweetId = tweetDiv.attr('data-tweet-id');

    var countries = Plotly.d3.select('#map-div').selectAll('.choroplethlocation')[0];

    var countryNumber;
    rows.forEach(function(row, n) {
        row.tweets.forEach(function (tweet) {
            if (tweet.id == tweetId) {
                countryNumber = n;
            }
        });
    });
    if (undefined !== countryNumber) {
        var event = document.createEvent('SVGEvents');
        event.initEvent(eventName,true,true);
        countries[countryNumber].dispatchEvent(event);
    }
}

Plotly.d3.select("#feed-containter").selectAll(".tweet")
    .on('mouseover', function() {
        var tweetDiv = Plotly.d3.select(this);
        tweetDiv.classed("highlighted", true);
        triggerEvent(tweetDiv, 'mouseover');
    })
    .on("mouseout", function () {
        var tweetDiv = Plotly.d3.select(this);
        tweetDiv.classed("highlighted", false);
        triggerEvent(tweetDiv, 'mouseout');
});
