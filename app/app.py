import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Verify the current working directory and check if the file exists
current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'data/stock_news_sentimental_analysis.csv')

# Load CSV file containing the sentiment data
df = pd.read_csv(file_path)


# Helper function to remove the borders of sidebar buttons
def style_sidebar_buttons():
    st.markdown(
        """
        <style>
        .css-1n76uvr {border: none;}
        .css-1n76uvr:hover {background-color: #eee;}
        </style>
        """, unsafe_allow_html=True)


# Function to display the ranking chart based on compound sentiment score
def plot_ticker_sentiment_ranking():
    sentiment_scores = df.groupby('Ticker')['sentiment_compound_score'].mean().sort_values(ascending=False)
    fig_rank = px.bar(sentiment_scores,
                      title="Sentiment Ranking of Tickers (by Compound Score)",
                      labels={'sentiment_compound_score': 'Compound Sentiment Score'},
                      color=sentiment_scores,
                      color_continuous_scale='Viridis')
    st.plotly_chart(fig_rank)


# Function to plot the sentiment scatter plot by compound score
def plot_sentiment_scatter(df_ticker, selected_ticker):
    fig_scatter = px.scatter(df_ticker, x='Date', y='sentiment_compound_score',
                             title=f'Sentiment Scatter Plot for {selected_ticker}',
                             labels={'sentiment_compound_score': 'Compound Sentiment Score'},
                             color='sentiment_compound_score',
                             color_continuous_scale='Viridis')
    st.plotly_chart(fig_scatter)


# Function to plot the sunburst chart for overall sentiment distribution
def plot_sentiment_sunburst(df_ticker, selected_ticker):
    overall_sentiment = df_ticker[
        ['sentiment_negative_score', 'sentiment_neutral_score', 'sentiment_positive_score']].mean()
    sentiment_labels = ['Negative', 'Neutral', 'Positive']
    sentiment_values = [overall_sentiment['sentiment_negative_score'],
                        overall_sentiment['sentiment_neutral_score'],
                        overall_sentiment['sentiment_positive_score']]
    fig_sunburst = go.Figure(go.Sunburst(
        labels=sentiment_labels,
        parents=[""] * 3,
        values=sentiment_values,
        branchvalues="total"
    ))
    fig_sunburst.update_layout(title=f'Overall Sentiment for {selected_ticker}')
    st.plotly_chart(fig_sunburst)


# Function to plot sentiment breakdown by date (bar plot)
def plot_sentiment_breakdown_by_date(df_ticker, selected_ticker):
    fig_line = px.line(df_ticker,
                       x='Date',
                       y=['sentiment_negative_score', 'sentiment_neutral_score', 'sentiment_positive_score',
                          'sentiment_compound_score'],
                       title=f'Sentiment Breakdown by Date for {selected_ticker}')
    st.plotly_chart(fig_line)


# Function to plot sentiment ratio (pie chart)
def plot_sentiment_ratio(df_ticker, selected_ticker):
    overall_sentiment = df_ticker[
        ['sentiment_negative_score', 'sentiment_neutral_score', 'sentiment_positive_score']].mean()
    positive_ratio = overall_sentiment['sentiment_positive_score'] / (
                overall_sentiment['sentiment_positive_score'] + overall_sentiment['sentiment_negative_score'] +
                overall_sentiment['sentiment_neutral_score'])
    negative_ratio = overall_sentiment['sentiment_negative_score'] / (
                overall_sentiment['sentiment_positive_score'] + overall_sentiment['sentiment_negative_score'] +
                overall_sentiment['sentiment_neutral_score'])
    neutral_ratio = overall_sentiment['sentiment_neutral_score'] / (
                overall_sentiment['sentiment_positive_score'] + overall_sentiment['sentiment_negative_score'] +
                overall_sentiment['sentiment_neutral_score'])

    labels_ratio = ['Positive', 'Negative', 'Neutral']
    values_ratio = [positive_ratio, negative_ratio, neutral_ratio]
    fig_ratio = go.Figure(data=[go.Pie(labels=labels_ratio, values=values_ratio, hole=0.3)])
    fig_ratio.update_layout(title=f'Sentiment Ratios for {selected_ticker}')
    st.plotly_chart(fig_ratio)


# Function to plot 3D scatter plot (advanced)
def plot_3d_scatter(df_ticker, selected_ticker):
    fig_3d = px.scatter_3d(df_ticker, x='sentiment_positive_score', y='sentiment_negative_score',
                           z='sentiment_compound_score',
                           color='sentiment_compound_score',
                           title=f'3D Scatter Plot for {selected_ticker}')
    st.plotly_chart(fig_3d)


# Function to plot Box plot (advanced)
def plot_box_plot(df_ticker, selected_ticker):
    fig_box = px.box(df_ticker, y=['sentiment_positive_score', 'sentiment_negative_score', 'sentiment_neutral_score'],
                     title=f'Sentiment Distribution Box Plot for {selected_ticker}')
    st.plotly_chart(fig_box)


# Function to plot Polar Plot
def plot_polar(df_ticker, selected_ticker):
    fig_polar = go.Figure(data=go.Scatterpolar(
        r=df_ticker['sentiment_compound_score'],
        theta=df_ticker['Date'],
        mode='lines',
        name=f'Sentiment for {selected_ticker}'
    ))
    fig_polar.update_layout(title=f'Polar Plot of Sentiment for {selected_ticker}',
                            polar=dict(radialaxis=dict(ticksuffix='%')))
    st.plotly_chart(fig_polar)


# Function to plot Ternary Plot
def plot_ternary(df_ticker, selected_ticker):
    fig_ternary = px.scatter_ternary(df_ticker, a='sentiment_positive_score', b='sentiment_neutral_score', c='sentiment_negative_score',
                                     color='sentiment_compound_score', title=f'Ternary Plot for {selected_ticker}')
    st.plotly_chart(fig_ternary)


# Streamlit Layout
def display_dashboard():
    st.title('Stock News Sentimental Analysis Dashboard')

    # Sidebar with ticker buttons (remove button border style)
    style_sidebar_buttons()
    tickers = df['Ticker'].unique()  # Get unique tickers from your data
    selected_ticker = None

    # Display buttons for each ticker
    for ticker in tickers:
        if st.sidebar.button(ticker, key=ticker):
            selected_ticker = ticker

    # Default Display: Ranking of tickers based on compound sentiment score
    if selected_ticker is None:
        st.subheader('Ticker Sentiment Ranking')
        plot_ticker_sentiment_ranking()

    else:
        st.sidebar.write(f"Displaying data for {selected_ticker}")

        # Filter data for the selected ticker
        df_ticker = df[df['Ticker'] == selected_ticker]

        # Display plots side by side
        col1, col2 = st.columns(2)

        # Plot sentiment scatter and sentiment breakdown over time in columns
        with col1:
            plot_sentiment_scatter(df_ticker, selected_ticker)
            plot_sentiment_ratio(df_ticker, selected_ticker)

        # Plot sentiment sunburst and line chart in columns
        with col2:
            plot_sentiment_sunburst(df_ticker, selected_ticker)
            plot_sentiment_breakdown_by_date(df_ticker, selected_ticker)

        # Display additional advanced charts
        st.subheader(f"Advanced Sentiment Visualizations for {selected_ticker}")
        plot_3d_scatter(df_ticker, selected_ticker)
        plot_box_plot(df_ticker, selected_ticker)

        # Display Polar and Ternary plots
        st.subheader(f"Additional Advanced Visualizations for {selected_ticker}")
        plot_polar(df_ticker, selected_ticker)
        plot_ternary(df_ticker, selected_ticker)


if __name__ == '__main__':
    display_dashboard()
