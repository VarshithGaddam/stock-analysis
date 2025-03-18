# agents/financial_analyzer.py
import yfinance as yf
from typing import Dict, List
import numpy as np

class FinancialAnalyzer:
    """Tool for fetching and analyzing financial data"""
    
    def get_stock_data(self, ticker: str, period: str = "1y") -> Dict:
        """Fetch stock data using yfinance"""
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period=period)
            info = stock.info
            
            # Calculate moving averages
            hist['MA20'] = hist['Close'].rolling(window=20).mean()
            hist['MA50'] = hist['Close'].rolling(window=50).mean()
            
            return {
                "success": True,
                "ticker": ticker,
                "current_price": float(hist['Close'][-1]),
                "price_history": hist['Close'].tolist(),
                "dates": hist.index.strftime('%Y-%m-%d').tolist(),
                "volume": hist['Volume'].tolist(),
                "ma20": hist['MA20'].tolist(),
                "ma50": hist['MA50'].tolist(),
                "market_cap": info.get('marketCap', 0),
                "pe_ratio": info.get('trailingPE', None),
                "dividend_yield": info.get('dividendYield', None)
            }
        except Exception as e:
            return {"success": False, "error": f"Failed to fetch data for {ticker}: {str(e)}"}

    def calculate_performance(self, price_history: List[float]) -> Dict:
        """Calculate enhanced performance metrics"""
        if not price_history or len(price_history) < 2:
            return {"error": "Insufficient data"}
            
        prices = np.array(price_history)
        initial_price = prices[0]
        final_price = prices[-1]
        
        # Calculate volatility (standard deviation of daily returns)
        daily_returns = np.diff(prices) / prices[:-1]
        volatility = np.std(daily_returns) * np.sqrt(252)  # Annualized volatility
        
        return {
            "total_return": ((final_price - initial_price) / initial_price) * 100,
            "highest_price": float(max(prices)),
            "lowest_price": float(min(prices)),
            "average_price": float(np.mean(prices)),
            "volatility": float(volatility * 100),  # As percentage
            "trend": "Up" if final_price > initial_price else "Down"
        }