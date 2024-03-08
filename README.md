# SECTable

It examines annual reports on sec.gov, extracting financial statements from the most recent year. Subsequently, it stores the extracted data in a CSV file.

### Keywords

Electronic Data Gathering, Analysis, and Retrieval (EDGAR); Securities and Exchange Comission(SEC); Web Crawling 

### Required Python packages

- bs4 
- requets
- pandas

### Parameters
- URL of a firm’s annual report
  - E.g: https://www.sec.gov/Archives/edgar/data/0000320193/000032019323000106/aapl-20230930.htm 
![](images/Annual_Report.jpg)

### Output
1. Show data on the screen
![](images/Output_Screen.jpg)
2. Save them to a CSV file
![](images/CSV.png)

### To-do
1. Create a multi-year table
2. Use ticker instead of URL
3. Search multiple tickers simultaneously

