import pandas as pd
from urllib.request import urlopen, Request
from datetime import datetime
from bs4 import BeautifulSoup


class StockNewsScraper:
    def __init__(self, tickers):
        self.finviz_url = 'https://finviz.com/quote.ashx?t='
        self.tickers = tickers
        self.all_news_data = []

    # Function to fetch and parse the HTML for a given ticker
    def fetch_ticker_data(self, ticker):
        full_url = self.finviz_url + ticker
        req = Request(url=full_url, headers={'user-agent': 'my-app'})
        res = urlopen(req)
        soup = BeautifulSoup(res, 'html.parser')
        return soup

    # Function to extract news data from the table
    def extract_news_data(self, soup, ticker):
        parse_data = []
        table = soup.find(id='news-table')

        for row in table.findAll('tr'):
            title = row.a.get_text()
            date_data = row.td.text.strip().split(' ')

            if len(date_data) == 1:
                time = date_data[0]
                date = datetime.now().strftime('%b-%d-%Y')  # Use current date if only time is present
            else:
                date = date_data[0] if date_data[0] != 'Today' else datetime.now().strftime('%b-%d-%Y')
                time = date_data[1]

            parse_data.append([ticker, date, time, title])

        return parse_data

    # Function to process each ticker and collect news data
    def process_tickers(self):
        for ticker in self.tickers:
            print(f"Processing {ticker}...")
            soup = self.fetch_ticker_data(ticker)
            ticker_news_data = self.extract_news_data(soup, ticker)
            self.all_news_data.extend(ticker_news_data)  # Collect all data into one list

    # Function to save the collected data to a CSV file
    def save_to_csv(self, filename='stock_news.csv'):
        df = pd.DataFrame(self.all_news_data, columns=['Ticker', 'Date', 'Time', 'Headline'])
        df.to_csv(filename, index=False, encoding='utf-8')
