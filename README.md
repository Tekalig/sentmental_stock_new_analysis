# Sentimental Stock News Analysis

## Project Description
This project performs sentiment analysis on stock news articles to assess whether the sentiment of news articles can help predict stock price movements. The project uses Natural Language Processing (NLP) to analyze the sentiment of the articles, leveraging machine learning models for prediction. The analysis is performed using various Python libraries, including `pandas`, `numpy`, `matplotlib`, `seaborn`, `nltk`, and `vaderSentiment`.

## Technologies
This project uses Python 3.7 and the following libraries:

- **[pandas](https://pandas.pydata.org/docs)**: For data manipulation and analysis.
- **[numpy](https://numpy.org)**: For numerical operations.
- **[matplotlib](https://matplotlib.org)**: For creating visualizations.
- **[seaborn](https://seaborn.pydata.org)**: For creating statistical visualizations.
- **[nltk](https://www.nltk.org)**: For natural language processing.
- **[vaderSentiment](https://github.com/cjhutto/vaderSentiment)**: For sentiment analysis on text.

## Installation Guide
To set up the project, you need to install the following dependencies. You can install them using `pip`:
```bash
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install nltk
pip install vaderSentiment
```

### Additional Setup for NLTK:
To run the sentiment analysis, you need to download the necessary NLTK data:
```python
import nltk
nltk.download('vader_lexicon')
```

## Usage
1. **Clone the Repository**:
   Clone the repository to your local machine using:
   ```bash
   git clone <repository-url>
   ```

2. **Run the Jupyter Notebook**:
   You can run the `stock_news_sentimental_analysis.ipynb` notebook to perform the analysis and visualize the results. Start JupyterLab by running:
   ```bash
   jupyter lab
   ```

3. **Running the Streamlit Dashboard**:
   Alternatively, you can run the Streamlit dashboard (`app/app.py`) for more interactive visualization of the stock sentiment data. To do this, navigate to the `app` folder and run:
   ```bash
   streamlit run app/app.py
   ```

## Project Structure

- **`scripts/`**: Contains Python scripts for scraping stock news data (`stock_news_scraper.py`) and performing sentiment analysis (`sentimental_analysis.py`).
- **` notebooks/`**: Contains Jupyter Notebooks for running data analysis and visualizing sentiment scores (`stock_news_sentimental_analysis.ipynb`).
- **`app/`**: Contains the Streamlit app for interactive visualizations of stock sentiment analysis (`stock_sentiment_dashboard.py`).
- **`data/`**: Contains datasets used for stock news sentiment analysis (CSV files).

## Contributors
This project is developed by the **ET Home Loans** team.

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
```

### Key Modifications:
1. Updated the installation guide for NLTK to include the `vader_lexicon` download.
2. Added usage instructions for running the **Streamlit** dashboard.
3. Clarified the repository structure and provided details on the scripts, notebooks, and app folder contents.
4. Added a project structure section to help users understand the layout of the project. 

This structure should provide clear guidance to anyone setting up or using your project!
