const fs = require('fs')

//create a series-like structure using an object
const series = {
    'Dune: Part Two' : 9.0,
    'Poor Things' : 8.2,
    'Dune' : 8.0,
    'Avatar : The Last Airbender' : 7.4,
    'Oppenheimer' : 8.4,
}

//convert the object to a JSON string
const seriesJSON = JSON.stringify(series, null, 2)

//write a JSON string to a file
fs.writeFile('series.json', seriesJSON, (err) => {
    if (err) {
        console.error('There was an error writting this file', err);  //print out the error message
    } else {
        console.log('Successfully wrote the series to file');
    }
})

//define the logic for objectToCSV()
function objectToCSV(object) {
    const csvRows = []

    //get the headers/columns
    csvRows.push('Index, Value')

    //Loop over the object/dictionary
    for (const [key,value] of Object.entries(object)) {
        csvRows.push(`${key}, ${value}`)  //push the values to their corresponding headers, key goes to index and value goes to Value column
    }

    // Form final string CSV
    return csvRows.join("\n");
}

//Function to convert an object to a CSV string --> a function that accepts an object as a parameter
const seriesCSV = objectToCSV(series);

//Write a CSV string to a file
fs.writeFile('series.csv', seriesCSV, (err) => {
    if (err) {
        console.error('There was an error writting to the CSV file:', err);
    } else {
        console.log("Successfully wrote the series to the CSV file");
    }
});



//run on terminal: node createSeries.js

