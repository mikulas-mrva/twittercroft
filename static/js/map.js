mapDiv = document.getElementById('map-div');

function unpack(rows, key) {
  return rows.map(function(row) { return row[key]; });
}

var data = [{
    type: 'choropleth',
    locationmode: 'country names',
    locations: unpack(rows, 'country'),
    z: unpack(rows, 'number_of_mentions'),
    text: unpack(rows, 'country'),
    autocolorscale: true
}];

var layout = {
  title: 'Countries mentioned in the tweets of Verisk Maplecroft',
  geo: {
      projection: {
          type: 'robinson'
      }
  }
};

Plotly.plot(mapDiv, data, layout, {showLink: false});

myPlot.on('plotly_hover', function(data){
    var infotext = data.points.map(function(d){
      return (d.data.name+': x= '+d.x+', y= '+d.y.toPrecision(3));
    });

    hoverInfo.innerHTML = infotext.join('');
})
 .on('plotly_unhover', function(data){
    hoverInfo.innerHTML = '';
});