# Stock News Sentimental Analysis - Scripts

This folder contains the Python scripts for scraping stock news articles and performing sentiment analysis on them. The two main scripts in this folder handle data collection and sentiment analysis for stock-related news. These scripts are designed to be imported into other projects or run as modules.

## Folder Structure

- **`stock_news_scraper.py`**: This script provides functions to scrape stock news articles for a given list of stock tickers and save them into a structured format (CSV or database).
  
- **`sentimental_analysis.py`**: This script contains functions to analyze the sentiment of the scraped stock news articles using the VADER sentiment analysis tool from NLTK. It calculates sentiment scores (positive, neutral, negative, and compound) and prepares the data for further analysis or visualization.

---

## How to Use the Scripts

### `stock_news_scraper.py`

This script provides functions to scrape stock news articles for a specified stock ticker. You can import and use its functions to scrape news for any stock ticker and return the data as a pandas DataFrame.

1. **Key Functions**:
    - `scrape_news(ticker)`: Scrapes news articles for a specific stock ticker and returns a pandas DataFrame containing the article data.
    - `save_to_csv(data, filename)`: Saves the scraped data to a CSV file.

2. **Example Usage**:
    To scrape news for a specific stock ticker, you can use the following code:
    ```python
    from scripts.stock_news_scraper import scrape_news

    data = scrape_news("AAPL")  # Scrape news for Apple (AAPL)
    data.to_csv("AAPL_news.csv", index=False)  # Save the data to a CSV file
    ```

3. **Dependencies**:
    - `requests`: To fetch data from websites.
    - `BeautifulSoup`: For parsing HTML content and extracting news articles.
    - `pandas`: For handling data and saving it into CSV format.

### `sentimental_analysis.py`

This script provides functions to analyze the sentiment of stock news articles using VADER from NLTK. You can import its functions to process the scraped news data and return sentiment scores.

1. **Key Functions**:
    - `analyze_sentiment(text)`: Analyzes the sentiment of a given text using the VADER sentiment analysis tool. It returns sentiment scores for each article.
    - `process_data(input_file, output_file)`: Loads the scraped news data from a CSV file, performs sentiment analysis, and saves the results in a new file with sentiment scores.

2. **Example Usage**:
    After scraping the news with `stock_news_scraper.py`, you can use the following code to perform sentiment analysis:
    ```python
    from scripts.sentimental_analysis import process_data

    process_data("AAPL_news.csv", "AAPL_sentiment.csv")
    ```
    This will read the news data from `AAPL_news.csv`, analyze the sentiment of each article, and save the results in `AAPL_sentiment.csv`.

3. **Dependencies**:
    - `pandas`: For handling the scraped data.
    - `nltk`: Natural Language Toolkit for sentiment analysis.
    - `vaderSentiment`: VADER sentiment analyzer.

---

## How to Run the Scripts

You can import and run these scripts from another Python script or Jupyter notebook. For example:

1. **To scrape stock news:**
    ```python
    from scripts.stock_news_scraper import scrape_news
    data = scrape_news("AAPL")  # Replace with your desired ticker
    data.to_csv("AAPL_news.csv", index=False)  # Save the scraped data to a CSV file
    ```

2. **To perform sentiment analysis:**
    ```python
    from scripts.sentimental_analysis import process_data
    process_data("AAPL_news.csv", "AAPL_sentiment.csv")  # Provide your scraped CSV file and output file
    ```

---

## Requirements

Before running the scripts, ensure you have the necessary dependencies installed:

```bash
pip install requests beautifulsoup4 pandas nltk vaderSentiment
