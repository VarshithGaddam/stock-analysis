# main.py
from agents.stock_agents import StockAnalysisAgents

def main():
    stock_analyzer = StockAnalysisAgents()
    while True:
        ticker = input("Enter stock ticker (or 'q' to quit, default AAPL): ").strip() or "AAPL"
        if ticker.lower() == "q":
            break
        print(f"Analyzing stock: {ticker}\n")
        try:
            result = stock_analyzer.analyze_stock(ticker)
            print(result)
            # Save chart to file (optional)
            with open(f"{ticker}_chart.png", "wb") as f:
                import base64
                chart_data = result.split("data:image/png;base64,")[-1]
                f.write(base64.b64decode(chart_data))
            print(f"Chart saved as {ticker}_chart.png")
        except Exception as e:
            print(f"Error analyzing {ticker}: {str(e)}")
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()