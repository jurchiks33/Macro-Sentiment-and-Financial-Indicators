
# M2 Money Supply vs. Stock Market Analysis

This project analyzes the relationship between the M2 money supply and the S&P 500 stock market index. 
It aims to explore the correlation between changes in M2 and stock market performance and provide insights that could potentially be used for trading strategies.

## Project Overview

The script retrieves historical M2 money supply data from the Federal Reserve Economic Data (FRED) and S&P 500 data from Yahoo Finance. It then:
- Merges the two datasets for monthly analysis.
- Visualizes the trends of M2 supply and S&P 500 stock prices.
- Performs correlation and regression analysis to quantify the relationship between M2 and the stock market.
- Generates a simple trading signal based on M2 trends.

### Features:
- **Data Retrieval**: Pulls M2 money supply data from FRED and S&P 500 data from Yahoo Finance.
- **Correlation & Regression Analysis**: Analyzes the relationship between M2 money supply and stock prices.
- **Trading Signal**: Generates a simple buy signal when M2 increases by more than 2% in a month.

## Installation

To run this project, you'll need to have Python installed, along with several libraries. Install the dependencies using pip:

```bash
pip install yfinance pandas-datareader pandas matplotlib scipy

How to Use

    Clone the repository:

    bash

git clone <https://github.com/jurchiks33/M2-Money-supply-vs-Stock-Market>
cd <yor-repository-directory>

Run the script:

bash

    python analysis.py

    The script will retrieve the data, process it, and display the following outputs:
        A plot of M2 Money Supply vs. S&P 500.
        Correlation and regression analysis results.
        A basic trading signal based on M2 changes.

Data Sources

    M2 Money Supply: Retrieved from the Federal Reserve Economic Data (FRED).
    S&P 500 Index: Retrieved from Yahoo Finance.

File Structure

    analysis.py: The main Python script for the analysis.
    README.md: This file, which provides an overview of the project.
    .gitignore: Specifies files and directories that Git should ignore.

License

This project is licensed under the MIT License. See the LICENSE file for more information.