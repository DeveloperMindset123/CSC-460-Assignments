//root file to handle web scraping
/**
 * import cheerio and axios
 */

/**
 * 
 * The below code is the data we are interested in the most
 * 
 */

//import { loadDataAndAnalyze } from './dataAnalysis';


const cheerio = require('cheerio');
const axios = require('axios');
const fs = require('fs');
const { Parser } = require('json2csv');
const dfd = require("danfojs-node");
//const loadDataAndAnalyze = require('./dataAnalysis');

//initialize the data structure
//this will contain the scraped data
const industries = []

//scraping the 
//use Axios to connect to target website with the following lines of code
/**
 * Downloading target web page
 * by performing an HTTP GET request in Axios
 */

async function performScraping() {
    const axiosResponse = await axios.request({
        method: "GET",
        url: "https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht",
        headers: {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
    })

    //parsing the html source of the target web page with cheerio
    const $ = cheerio.load(axiosResponse.data)  //The Cheerio load() method accepts HTML content in string form

    // Selecting the list items containing each title and its metadata
    $('ul.ipc-metadata-list li.ipc-metadata-list-summary-item').each((i, element) => {
        const title = $(element).find('h3.ipc-title__text').text().trim();
        const weekendGross = $(element).find('ul[data-testid="title-metadata-box-office-data-container"] li').first().find('span.elpuzG').text().trim();
        const totalGross = $(element).find('ul[data-testid="title-metadata-box-office-data-container"] li').eq(1).find('span.elpuzG').text().trim();
        const weeksReleased = $(element).find('ul[data-testid="title-metadata-box-office-data-container"] li').eq(2).find('span.elpuzG').text().trim();
        const rating = $(element).find('div[data-testid="ratingGroup--container"] span.ipc-rating-star--imdb').text().trim();

        // Create an object and push it to the industries array
        industries.push({ title, weekendGross, totalGross, weeksReleased, rating });
    //console.log(industries);

    //save to json
    // Save to JSON
    fs.writeFileSync('movies.json', JSON.stringify(industries, null, 2));

    // Save to CSV
    const json2csvParser = new Parser();
    const csv = json2csvParser.parse(industries);
    fs.writeFileSync('industries.csv', csv);

    // Reading CSV into DataFrame
    let df = new dfd.DataFrame(industries);

    // Ensure all numeric data is in a numeric format
    // Convert strings to numbers
    /* --> TO DO: Fix it, this part of the code causes error
    df['weekendGross'] = df['weekendGross'].map(value => parseFloat(value.replace(/\$|M/g, '')) * 1e6);
    df['totalGross'] = df['totalGross'].map(value => parseFloat(value.replace(/\$|M/g, '')) * 1e6);
    df['weeksReleased'] = df['weeksReleased'].map(value => parseInt(value));
    df['rating'] = df['rating'].map(value => {
    const matches = value.match(/(\d+.\d+|\d+)/);
    return matches ? parseFloat(matches[0]) : NaN;
    });*/

// Descriptive summary of numerical series
//console.log(df.describe());

    // Find all the titles with total gross greater than $40M
    //const filteredDf = df.loc({ rows: df['totalGross'].gt(40000000) });
    console.log("Raw Data:\n", df.toString());
    //console.log("Filtered Data: ", filteredDf.data);

    //console.log(axiosResponse);
    //console.log("\n The Data is:", axiosResponse.data)  //constains the html source code
    return df.toString();
})};

//call on the function and save the result
result = performScraping()
console.log(result)
//loadDataAndAnalyze()
//console.log(industries) --> no point printing out the same thing twice

//test to see if file is working, delete afterwards
//console.log("This is a test!");