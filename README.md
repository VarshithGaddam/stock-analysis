# Stock Analysis Project

A multi-agent system built with AutoGen to fetch, analyze, and visualize stock data using the `yfinance` API and Google Gemini API for AI-powered insights.

## Overview

This project demonstrates a basic agentic framework that:
- Fetches real-time stock data.
- Calculates financial metrics (e.g., returns, volatility, moving averages).
- Generates enhanced visualizations (price trends and volume).
- Provides professional analysis and investment recommendations.

Built as part of a task to explore agentic frameworks, this implementation uses AutoGen with a custom `yfinance`-based tool, enhanced for practical use.

## Features

- **Data Fetching**: Retrieves stock price history, volume, and metadata via `yfinance`.
- **Performance Metrics**: Calculates total return, volatility, and trend direction.
- **Visualization**: Plots price with 20/50-day moving averages and trading volume in a single figure.
- **AI Analysis**: Uses Google Gemini API (`gemini-1.5-flash`) for financial analysis and reporting.
- **Output**: Generates a markdown-formatted report with key metrics and recommendations.

## Prerequisites

- Python 3.10 or higher
- Git installed
- A Google Gemini API key (free tier available at [ai.google.dev](https://ai.google.dev/))

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/VarshithGaddam/stock-analysis.git
   cd stock-analysis


   # Stock Analysis Project

## Installation

### Install Dependencies:
Run the following command to install the required dependencies:

```bash
pip install -r requirements.txt
```

### Requirements include:
- `autogen>=0.2.0`
- `yfinance>=0.2.40`
- `matplotlib>=3.8.0`
- `openai>=1.66.3`
- `numpy==1.26.4`
- `pandas==2.2.2`

## Configuration

### Configure API Key:
Open `config/config.py` and ensure the Gemini API key is set:

```python
config_list = [
    {
        "model": "gemini-1.5-flash",
        "api_key": "your-gemini-api-key-here",
        "base_url": "https://generativelanguage.googleapis.com/v1beta/"
    }
]
```

Replace `"your-gemini-api-key-here"` with your key from [Google AI Studio](https://aistudio.google.com/).

## Usage

### Run the Script:
Execute the script using:

```bash
python main.py
```

### Input a Ticker:
- Enter a stock ticker symbol (e.g., `AAPL` for Apple) when prompted.
- Press **Enter** for the default (`AAPL`).
- Type `q` to quit.

### Output:
The script generates a detailed report with:
- A table of key metrics.
- A stock analysis summary.
- A **base64-encoded chart** for visualization.

### Example Output:

#### **AAPL Stock Report**

| Metric        | Value          |
|--------------|----------------|
| Current Price | $225.45        |
| Total Return  | 25.8%          |
| Volatility    | 28.4%          |

**Recommendation**: Buy

#### **Price and Volume Charts**

`[Base64 image data]`

## Project Structure

```
stock_analysis_project/
├── agents/
│   ├── financial_analyzer.py  # Data fetching and metrics
│   └── stock_agents.py       # Multi-agent system
├── config/
│   └── config.py            # API configuration
├── utils/
│   └── visualization.py     # Enhanced plotting
├── main.py                  # Entry point
└── requirements.txt         # Dependencies
```

## Enhancements

- Multi-subplot charts for price and volume.
- Volatility and trend analysis.
- Optimized data sampling for efficient visualization.
- Markdown-formatted reports for readability.

## Limitations

- Requires an internet connection for API calls.
- Gemini API free tier has rate limits (**15 RPM, 1500 RPD**).
- Base64 charts are text-based; consider saving as files for easier viewing.

## Contributing

Feel free to fork this repository, submit pull requests, or open issues for suggestions!

## License

This project is **unlicensed**—free to use and modify as you see fit.
