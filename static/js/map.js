mapDiv = document.getElementById('map-div');

function unpack(rows, key) {
  return rows.map(function(row) { return row[key]; });
}

var tweets = [{
    type: 'choropleth',
    locationmode: 'country names',
    locations: unpack(rows, 'country'),
    z: unpack(rows, 'number_of_mentions'),
    text: unpack(rows, 'country'),
    hoverinfo: 'text'
}];

var layout = {
  title: 'Countries mentioned in the tweets of Verisk Maplecroft',
  geo: {
      projection: {
          type: 'robinson'
      }
  }
};

Plotly.plot(mapDiv, tweets, layout, {showLink: false});

Plotly.d3.select("#feed-containter").selectAll(".tweet")
    .on('mouseover', function() {
        var tweetDiv = Plotly.d3.select(this);
        tweetDiv.classed("highlighted", true);
        triggerSVGEvent(tweetDiv, 'mouseover');
    })
    .on("mouseout", function () {
        var tweetDiv = Plotly.d3.select(this);
        tweetDiv.classed("highlighted", false);
        triggerSVGEvent(tweetDiv, 'mouseout');
});

function triggerSVGEvent(tweetDiv, eventName) {
    // This function is used for displaying and hiding tooltips over countries
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
