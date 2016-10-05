mapDiv = document.getElementById('map-div');

function unpack(rows, key) {
  return rows.map(function(row) { return row[key]; });
}

var data = [{
    type: 'choropleth',
    locationmode: 'country names',
    locations: unpack(rows, 'location'),
    z: unpack(rows, 'number_of_mentions'),
    text: unpack(rows, 'location'),
    autocolorscale: true
}];

var layout = {
  title: 'Countries mentioned in the tweets of Verisk Maplecrofts',
  geo: {
      projection: {
          type: 'robinson'
      }
  }
};

Plotly.plot(mapDiv, data, layout, {showLink: false});
