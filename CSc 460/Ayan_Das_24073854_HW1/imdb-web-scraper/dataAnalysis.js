const fs = require('fs');

function convert_currency(value) {
    if (value.includes('M')) {
        return parseFloat(value.replace('M', '').replace('$', '')) * 1e6;
    } else if (value.includes('K')) {
        return parseFloat(value.replace('K', '').replace('$', '')) * 1e3;
    } else {
        return parseFloat(value.replace('$', ''));
    }
}

// Read the JSON file content and then parse it
fs.readFile('movies.json', 'utf8', function(err, data) {
    if (err) throw err;
    
    var df = JSON.parse(data);

    df.forEach(function(row) {
        row.weekendGross = convert_currency(row.weekendGross);
        row.totalGross = convert_currency(row.totalGross);
        row.weeksReleased = Number(row.weeksReleased);
        var ratingMatch = row.rating.match(/(\d+\.\d+|\d+)/);
        row.rating = ratingMatch ? parseFloat(ratingMatch[0]) : null;
    });

    console.log("Descriptive Summary:");
    // You would need to implement your own logic to describe the data,
    // since JavaScript does not have a built-in method like pandas' describe.
    // You can calculate mean, median, min, max, etc. manually.

    var highGrossingMoviesDf = df.filter(function(row) {
        return row.totalGross > 40000000;
    });
    console.log("\nTitles with Total Gross greater than $40M:");
    highGrossingMoviesDf.forEach(function(row) {
        console.log(row.title);
    });
});


