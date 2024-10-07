# M2 Money Supply vs. Stock Market & Interest Rate Yield Curve Analysis

This project explores two key financial analyses:

1. **M2 Money Supply vs. Stock Market**: Analyzes the relationship between the M2 money supply and the S&P 500 stock market index. It aims to explore the correlation between changes in M2 and stock market performance and provide insights that could potentially be used for trading strategies.
2. **Interest Rate Yield Curve Analysis**: Visualizes the yield curve spread between 10-year and 2-year US Treasury yields, a critical economic indicator used to assess the likelihood of recession or expansion.

## Project Overview

### M2 Money Supply vs. Stock Market

The script retrieves historical M2 money supply data from the Federal Reserve Economic Data (FRED) and S&P 500 data from Yahoo Finance. It then:

- Merges the two datasets for monthly analysis.
- Visualizes the trends of M2 supply and S&P 500 stock prices.
- Performs correlation and regression analysis to quantify the relationship between M2 and the stock market.
- Generates a simple trading signal based on M2 trends.

### Interest Rate Yield Curve Analysis

This script fetches US Treasury yields (10-year and 2-year) from FRED and calculates the yield curve spread (10-year yield minus 2-year yield). It visualizes the following:

- A **normal yield curve** (positive spread), indicating potential economic expansion.
- An **inverted yield curve** (negative spread), a potential signal of recession.
- A **flat yield curve**, signaling economic transitions.

## Features:

### M2 Money Supply vs. Stock Market

- **Data Retrieval**: Pulls M2 money supply data from FRED and S&P 500 data from Yahoo Finance.
- **Correlation & Regression Analysis**: Analyzes the relationship between M2 money supply and stock prices.
- **Trading Signal**: Generates a simple buy signal when M2 increases by more than 2% in a month.

### Interest Rate Yield Curve Analysis

- **Data Retrieval**: Fetches the 10-year and 2-year US Treasury yields from FRED.
- **Yield Curve Spread**: Calculates and plots the difference between 10-year and 2-year yields.
- **Economic Insight**: Provides visual insights into economic phases, signaling potential expansion or recession.

## Installation

To run this project, you'll need to have Python installed, along with several libraries. Install the dependencies using pip:

```bash
pip install yfinance pandas-datareader pandas matplotlib scipy

How to Use
Clone the repository:

bash

git clone <https://github.com/jurchiks33/M2-Money-supply-vs-Stock-Market>
cd <your-repository-directory>

Run the M2 Money Supply vs. Stock Market script:

bash

python analysis.py

    The script will retrieve the data, process it, and display the following outputs:
        A plot of M2 Money Supply vs. S&P 500.
        Correlation and regression analysis results.
        A basic trading signal based on M2 changes.

Run the Interest Rate Yield Curve script:

bash

python interest_yield_curve.py

    The script will retrieve US Treasury yields, calculate the 10-year minus 2-year yield spread, and display the yield curve. It will show whether the yield curve is normal, inverted, or flat, along with economic insights.

Data Sources

    M2 Money Supply: Retrieved from the Federal Reserve Economic Data (FRED).
    S&P 500 Index: Retrieved from Yahoo Finance.
    US Treasury Yields: 10-year and 2-year yields retrieved from FRED.

File Structure

    analysis.py: The Python script for M2 Money Supply vs. Stock Market analysis.
    interest_yield_curve.py: The Python script for Interest Rate Yield Curve analysis.
    README.md: This file, which provides an overview of the project.
    .gitignore: Specifies files and directories that Git should ignore.

License

This project is licensed under the MIT License. See the LICENSE file for more information.

### Updates Made:
- Added a new section for **Interest Rate Yield Curve Analysis**.
- Updated features, usage instructions, and file structure to reflect the addition of the new `interest_yield_curve.py` script.
