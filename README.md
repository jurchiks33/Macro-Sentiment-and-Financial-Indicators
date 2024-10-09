Financial & Economic Analysis Toolkit

This project includes multiple financial and economic analysis tools:

    M2 Money Supply vs. Stock Market: Analyzes the relationship between the M2 money supply and the S&P 500 stock market index. It explores the correlation between changes in M2 and stock market performance and provides insights that could potentially be used for trading strategies.
    Interest Rate Yield Curve Analysis: Visualizes the yield curve spread between 10-year and 2-year US Treasury yields, a critical economic indicator used to assess the likelihood of recession or expansion.
    University of Michigan Consumer Sentiment Index (UMCSI): Fetches and visualizes the UMCSI data, showing key sentiment trends with important threshold markers.
    ISM Report Analysis: Scrapes and analyzes the ISM manufacturing data for key economic indicators.
    VIX Analysis: Analyzes the volatility index (VIX), also known as the "fear gauge," to understand market expectations for future volatility.

Project Overview
M2 Money Supply vs. Stock Market

This script retrieves historical M2 money supply data from the Federal Reserve Economic Data (FRED) and S&P 500 data from Yahoo Finance. It then:

    Merges the two datasets for monthly analysis.
    Visualizes the trends of M2 supply and S&P 500 stock prices.
    Performs correlation and regression analysis to quantify the relationship between M2 and the stock market.
    Generates a simple trading signal based on M2 trends.

Interest Rate Yield Curve Analysis

This script fetches US Treasury yields (10-year and 2-year) from FRED and calculates the yield curve spread (10-year yield minus 2-year yield). It visualizes the following:

    A normal yield curve (positive spread), indicating potential economic expansion.
    An inverted yield curve (negative spread), a potential signal of recession.
    A flat yield curve, signaling economic transitions.

University of Michigan Consumer Sentiment Index (UMCSI) Analysis

This script retrieves the University of Michigan Consumer Sentiment Index from FRED and provides a visual representation of consumer sentiment with key reference lines:

    Horizontal line at 75: Indicates lower levels of consumer sentiment, which could indicate weaker consumer confidence.
    Horizontal line at 95: Indicates higher levels of consumer sentiment, signaling stronger consumer confidence.

ISM Report Analysis

The script scrapes the ISM Report on Business data to provide key metrics, such as Manufacturing PMI, New Orders, and Production, and displays them in a clear, tabular format for easy analysis.

VIX (Volatility Index) Analysis

This script retrieves the VIX (Volatility Index) data to analyze and visualize the market's expectations for future volatility, often referred to as the "fear gauge."

Features:
M2 Money Supply vs. Stock Market

    Data Retrieval: Pulls M2 money supply data from FRED and S&P 500 data from Yahoo Finance.
    Correlation & Regression Analysis: Analyzes the relationship between M2 money supply and stock prices.
    Trading Signal: Generates a simple buy signal when M2 increases by more than 2% in a month.

Interest Rate Yield Curve Analysis

    Data Retrieval: Fetches the 10-year and 2-year US Treasury yields from FRED.
    Yield Curve Spread: Calculates and plots the difference between 10-year and 2-year yields.
    Economic Insight: Provides visual insights into economic phases, signaling potential expansion or recession.

University of Michigan Consumer Sentiment Index (UMCSI) Analysis

    Data Retrieval: Retrieves UMCSI data from FRED.
    Visual Insights: Displays UMCSI trends with horizontal reference lines at 75 and 95 to indicate key sentiment levels.

ISM Report Analysis

    Data Scraping: Scrapes the latest ISM report data from the web.
    Visual Representation: Displays ISM key economic metrics in a table for easy reference.

VIX Analysis

    Data Retrieval: Retrieves the VIX (Volatility Index) data from FRED or another financial data provider.
    Volatility Insights: Analyzes the market’s expectations for future volatility.

Installation

To run this project, you'll need to have Python installed, along with several libraries. Install the dependencies using pip:

bash

pip install yfinance pandas-datareader pandas matplotlib scipy beautifulsoup4 requests

How to Use

Clone the repository:

bash

git clone <https://github.com/jurchiks33/Macro-Sentiment-and-Financial-Indicators>
cd <your-repository-directory>

Run the M2 Money Supply vs. Stock Market script:

bash

python M2_Money_Supply.py

The script will retrieve the data, process it, and display the following outputs:

    A plot of M2 Money Supply vs. S&P 500.
    Correlation and regression analysis results.
    A basic trading signal based on M2 changes.

Run the Interest Rate Yield Curve script:

bash

python Benchmark_Yield_US.py

The script will retrieve US Treasury yields, calculate the 10-year minus 2-year yield spread, and display the yield curve. It will show whether the yield curve is normal, inverted, or flat, along with economic insights.
Run the University of Michigan Consumer Sentiment Index script:

bash

python umcsi_scrapper.py

The script will retrieve the UMCSI data and display a chart with horizontal lines at 75 and 95 to indicate key sentiment thresholds.
Run the ISM Report Analysis script:

bash

python ism_report_scraper.py

This script scrapes and displays key metrics from the latest ISM report, providing insight into the state of manufacturing and business activity.
Run the VIX Analysis script:

bash

python vix_analysis.py

This script analyzes the VIX, visualizing market expectations for volatility over the next 30 days.
Data Sources

    M2 Money Supply: Retrieved from the Federal Reserve Economic Data (FRED).
    S&P 500 Index: Retrieved from Yahoo Finance.
    US Treasury Yields: 10-year and 2-year yields retrieved from FRED.
    University of Michigan Consumer Sentiment Index: Retrieved from FRED.
    ISM Report Data: Scraped from the ISM official report page.
    VIX (Volatility Index): Retrieved from financial data sources like Yahoo Finance or FRED.

File Structure

    M2_Money_Supply.py: The Python script for M2 Money Supply vs. Stock Market analysis.
    Benchmark_Yield_US.py: The Python script for Interest Rate Yield Curve analysis.
    umcsi_scrapper.py: The Python script for University of Michigan Consumer Sentiment Index analysis.
    ism_report_scraper.py: The Python script for scraping and displaying ISM Report data.
    vix_analysis.py: The Python script for VIX (Volatility Index) analysis.
    README.md: This file, which provides an overview of the project.
    .gitignore: Specifies files and directories that Git should ignore.

License

This project is licensed under the MIT License.