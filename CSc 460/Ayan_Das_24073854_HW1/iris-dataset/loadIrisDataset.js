const fs = require('fs');
const Papa = require('papaparse');
const dfd = require('danfojs-node');
// Read the CSV file
const fileContent = fs.readFileSync('dataset-iris.csv', 'utf8');

// Parse the CSV content
Papa.parse(fileContent, {
    header: true,
    complete: (results) => {
        const data = results.data;

        // Headers
        const headers = results.meta.fields;

        // Count of Data Object (Number of Rows)
        const countOfDataObjects = data.length;

        // Count of Data Categories (Unique Classes)
        const uniqueClasses = [...new Set(data.map(item => item.class))];
        const countOfDataCategories = uniqueClasses.length;

        // Count of Each Category
        const countOfEachCategory = uniqueClasses.map((cls) => ({
            [cls]: data.filter((item) => item.class === cls).length
        }));

        // Series Data Types
        // This is more complex in JavaScript because all CSV fields are read as strings.
        // You would need to write a function to determine types manually, usually in JS we keep it as is.

        console.log("Headers:", headers);
        console.log("Count of Data Objects:", countOfDataObjects);
        console.log("Count of Data Categories:", countOfDataCategories);
        console.log("Count of Each Category:", countOfEachCategory);
        // Data types not shown due to the manual nature of determination
    }
});

dfd.readCSV('dataset-iris.csv').then(df => {
    // Add new columns
    df.addColumn('Petal Ratio', df['petal length'].div(df['petal width']), { inplace: true });
    df.addColumn('Sepal Ratio', df['sepal length'].div(df['sepal width']), { inplace: true });

    // Convert DataFrame to a JSON object
    const jsonObj = dfd.toJSON(df);

    // Stringify the JSON object
    const jsonStr = JSON.stringify(jsonObj);

    // Write the stringified JSON to a file
    fs.writeFileSync('updated_dataset-iris.json', jsonStr);
    console.log("Saved updated DataFrame to 'updated_dataset-iris.json'");

    // Group by the 'class' column and aggregate
    let groupedDf = df.groupby(['class']).agg({
        'sepal length': ['mean', 'std', 'min', 'max'],
        'sepal width': ['mean', 'std', 'min', 'max'],
        'petal length': ['mean', 'std', 'min', 'max'],
        'petal width': ['mean', 'std', 'min', 'max'],
        'Petal Ratio': ['mean', 'std', 'min', 'max'],
        'Sepal Ratio': ['mean', 'std', 'min', 'max'],
    });

    console.log("Descriptive Statistics by Category:");
    groupedDf.print();

    // Optionally, save the aggregated DataFrame to a new CSV file
    dfd.toCSV(groupedDf, {filePath: "descriptive_stats_by_category.csv"})
    /*
    .then(() => {
        console.log("Saved descriptive statistics by category to 'descriptive_stats_by_category.csv'");
    }).catch(err => {
        console.error("Error saving CSV: ", err);
    }); */
}).catch(err => {
    console.error("Error processing data: ", err);
});




