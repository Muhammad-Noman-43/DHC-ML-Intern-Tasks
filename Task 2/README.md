# Stock Price Predictor

## Overview

This notebook implements a machine learning model to predict the next day's closing price of Apple (AAPL) stock based on historical stock data.

## Methodology

### Data Source

- Historical stock data retrieved from Yahoo Finance using `yfinance`
- Time period: 5 years of historical data
- Features: Open, High, Low, Close, Volume

### Data Processing

- Features used: Open, High, Low, Volume
- Target variable: Next day's closing price
- Data split: 80% training, 20% testing
- Missing values removed after creating the target variable

### Model

- **Algorithm**: Linear Regression
- **Framework**: scikit-learn
- **Input features**: 4 (Open, High, Low, Volume)
- **Output**: Predicted next day closing price

## Performance Metrics

The model is evaluated using:

- **Mean Squared Error (MSE)**: Measures average prediction error magnitude
- **R² Score**: Explains proportion of variance in closing prices

## Usage

Run the notebook cells in order:

- Load and fetch stock data
- Preprocess and clean data
- Split into training/testing sets
- Train the model
- Evaluate with metrics
- Visualize results

## Output

- Console output showing MSE and R² score metrics
- Matplotlib figure comparing actual vs predicted prices
