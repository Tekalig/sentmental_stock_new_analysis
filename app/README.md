# Stock News Sentimental Analysis - Streamlit Dashboard

This folder contains the Streamlit dashboard `stock_news_dashboard.py` that visualizes stock news sentiment analysis. The dashboard allows you to interactively explore sentiment data for different stock tickers, view sentiment trends over time, and gain insights through advanced visualizations such as pie charts, bar plots, 3D scatter plots, polar plots, and more.

---

## Folder Structure

- **`stock_news_dashboard.py`**: The main Streamlit dashboard script. This file loads the sentiment data and visualizes it interactively using Plotly charts.

---

## How to Use the Streamlit Dashboard

1. **Prerequisites**:
    - You must have run the `stock_news_scraper.py` and `sentimental_analysis.py` scripts from the `scripts` folder to scrape and process the sentiment data. These scripts will generate the CSV file containing sentiment scores that will be used in this dashboard.

2. **Run the Scripts**:
    To generate the sentiment data used in the dashboard, run the following scripts from the `scripts` folder:
    
    - **Scraping Stock News**:  
      First, run `stock_news_scraper.py` to scrape the stock news data.
      ```bash
      python scripts/stock_news_scraper.py
      ```
    
    - **Sentiment Analysis**:  
      After scraping the news, run `sentimental_analysis.py` to calculate the sentiment scores and save them into a CSV file.
      ```bash
      python scripts/sentimental_analysis.py
      ```
    
    These scripts will create a CSV file containing sentiment scores for each stock, which is then loaded into the dashboard.

3. **Running the Streamlit Dashboard**:
    Once the sentiment data is ready, you can run the Streamlit dashboard by executing the following command from the `app` folder:

    ```bash
    streamlit run stock_news_dashboard.py
    ```

    This will start a local Streamlit server and open the dashboard in your default web browser.

4. **Interacting with the Dashboard**:
    - The sidebar contains a list of stock tickers. When you click on a ticker, the dashboard will display the sentiment analysis for that specific stock.
    - The dashboard will show various interactive visualizations, including:
      - **Overall Sentiment Pie Chart**: Displays the distribution of sentiment scores (positive, neutral, negative).
      - **Sentiment Breakdown by Date**: Shows a bar plot of sentiment scores over time.
      - **Sentiment Ratio**: Displays the ratio of positive, negative, and neutral sentiments.
      - **Advanced Visualizations**: Includes 3D scatter plots, polar plots, ternary plots, and more to offer deeper insights into the sentiment analysis.

5. **Dashboard Features**:
    - **Ranking of Tickers**: The dashboard defaults to showing a ranking of tickers based on their compound sentiment score, which is used to rank stocks based on overall sentiment.
    - **Interactive Plots**: Hover over the plots to get more detailed information and interact with the charts to explore different aspects of sentiment data.

6. **Data Input Format**:
    The CSV data used in the dashboard must contain the following columns:
    - `Ticker`: The stock ticker symbol.
    - `Time`: The time of the news article or sentiment data.
    - `Date`: The date of the news article or sentiment data.
    - `sentiment_positive_score`: The positive sentiment score for each article.
    - `sentiment_neutral_score`: The neutral sentiment score for each article.
    - `sentiment_negative_score`: The negative sentiment score for each article.
    - `sentiment_compound_score`: The compound sentiment score, which summarizes the overall sentiment of the article.

---

## Example Usage

After scraping the data and performing sentiment analysis, you can follow these steps to run the Streamlit dashboard:

1. **Generate Sentiment Data**:  
   Run the `stock_news_scraper.py` and `sentimental_analysis.py` scripts to generate the sentiment data in CSV format.

2. **Run the Streamlit Dashboard**:  
   In the `app` folder, run the following command:
   ```bash
   streamlit run app/app.py
