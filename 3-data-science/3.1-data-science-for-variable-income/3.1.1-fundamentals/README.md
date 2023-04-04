# Project Name: Stock Market Analysis

This project aims to practice data analysis on a variable income database of stocks. The project will use indicators of fundamental analysis of stocks, such as price, liquidity, P/E, and DY, and will be implemented using Python.

## Teaching Objectives

This project aims to practice the following concepts covered in the Module:

- Working with a brazillian variable income database of stocks
- Working with indicators of fundamental analysis of stocks (Price, Liquidity, P/E, DY)
- Performing exploratory analysis of variable income data
- Practicing some basic Python commands for data analysis and graphing.

## Data Source

The data for this project will be obtained from https://statusinvest.com.br/, using the Advanced Search menu and without filters. This will provide us with an updated database of stocks, which we will use for the exploratory data analysis.

## Tools Used

We will be using the following tools for this project:

1. Python: For data cleaning, exploratory analysis, and visualization.
2. Jupyter Notebook: For organizing and presenting the analysis in an interactive format.

## Project Steps

1. Data Collection:
   
   - Obtain the data from https://statusinvest.com.br/ using the Advanced Search menu and without filters.
   - Save the downloaded file into [./data/raw](./data/raw/) folder
   - Read the downloaded CSV file

2. Descriptive Analysis:
   
   - First values: Viewing the first few rows of the dataset to get a quick glimpse of the data and understand its structure.
   - Last values: Viewing the last few rows of the dataset to see if there are any patterns or issues in the data.
   - Rows and columns count: Counting the number of rows and columns to get a sense of the size of the dataset.
   - List of columns: Listing all the columns in the dataset to see what kind of data is available.
   - Columns types: Identifying the data type of each column in the dataset.
   - Convert columns to appropriate types: Converting columns to their appropriate data types to make them more usable for analysis.
   - Statistical summary for numerical columns: Calculating basic statistical measures (mean, median, standard deviation, etc.) for numerical columns to understand their distribution and variation.
   - Number of missing values in each column: Identifying how many missing values are present in each column of the dataset.
   - Number of unique values: Counting the number of unique values in each column to understand the level of variation and potential grouping.
   - Memory usage: Calculating the amount of memory each column uses in bytes to assess the size of the dataset.
   
3. Data Cleaning and Transformation:

   - Fill in the empty spaces with 0
   - Delete rows (filter and clear) asset prices outside the standard (Price above R$ 1,000.00 and price = R$ 0.00)

4. Analysing data:

   - Find the name of the asset with the highest price
   - Find the 10 highest and 10 lowest asset prices
   - Find the sum and average of the Average Daily Liquidity
   - Find the names of assets with P/E greater than 0
   - Find assets with DY above 0
   - List the PN preferred shares (code 4)

5. Sharing Results:
   - Present the 10 stocks with the highest Average Daily Liquidity and show the result in a column chart, with the X axis being the asset names and the Y axis being the Average Daily Liquidity value.

## Project Requirements
To complete this project, you will need the following:

1. Access to the internet to obtain the data from https://statusinvest.com.br/
2. Python and relevant libraries for data analysis and visualization (e.g., Pandas, NumPy, Matplotlib)
3. Jupyter Notebook

## Conclusion
This project will provide a hands-on opportunity to practice data analysis on a variable income database of stocks. By using Python and Jupyter Notebook, you will gain experience working with tools commonly used in data science, and will develop a better understanding of the fundamental analysis of stocks.

## Contributing

If you'd like to contribute to this project, feel free to fork this repository and submit a pull request with your changes.

## License

This repository is licensed under the MIT License. See the [LICENSE](../../../LICENSE) file for more information.