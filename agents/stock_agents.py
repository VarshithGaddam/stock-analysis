# agents/stock_agents.py
import autogen
from config.config import config_list
from agents.financial_analyzer import FinancialAnalyzer
from utils.visualization import create_enhanced_charts

class StockAnalysisAgents:
    """Manages stock analysis agents and their interactions"""
    
    def __init__(self):
        self.financial_tool = FinancialAnalyzer()
        
        self.analyst = autogen.AssistantAgent(
            name="FinancialAnalyst",
            llm_config={"config_list": config_list},
            system_message="""
            You are a financial analyst. Analyze stock data including:
            - Price trends and moving averages
            - Performance metrics (return, volatility)
            - Valuation ratios
            Provide a concise, professional analysis and recommendation.
            """
        )
        
        self.reporter = autogen.AssistantAgent(
            name="ReportGenerator",
            llm_config={"config_list": config_list},
            system_message="""
            You are a report generator. Create a professional report:
            1. Summarize key metrics in a table-like format
            2. Include analyst insights
            3. Provide a clear investment recommendation
            Use markdown formatting for clarity.
            """
        )
        
        self.user_proxy = autogen.UserProxyAgent(
            name="UserProxy",
            human_input_mode="NEVER",
            max_consecutive_auto_reply=5,
            code_execution_config={"work_dir": "coding", "use_docker": False}
        )

    def analyze_stock(self, ticker: str) -> str:
        """Execute enhanced stock analysis workflow"""
        stock_data = self.financial_tool.get_stock_data(ticker)
        
        if not stock_data.get("success"):
            return f"Error: {stock_data.get('error', 'Unknown error')}"
            
        performance = self.financial_tool.calculate_performance(stock_data["price_history"])
        chart = create_enhanced_charts(
            ticker, stock_data["price_history"], stock_data["volume"],
            stock_data["ma20"], stock_data["ma50"], stock_data["dates"]
        )
        
        analysis_prompt = f"""
        Analyze {ticker} with this data:
        - Current Price: ${stock_data['current_price']:.2f}
        - Market Cap: ${stock_data['market_cap']:,}
        - P/E Ratio: {stock_data['pe_ratio'] or 'N/A'}
        - Dividend Yield: {stock_data['dividend_yield'] or 'N/A'}
        - Performance Metrics: {performance}
        - 20-day MA (last): ${stock_data['ma20'][-1]:.2f}
        - 50-day MA (last): ${stock_data['ma50'][-1]:.2f}
        Provide a professional analysis and recommendation.
        """
        
        try:
            analysis = self.analyst.generate_reply(messages=[{"content": analysis_prompt, "role": "user"}])
        except Exception as e:
            analysis = f"Analysis failed: {str(e)}"
        
        report_prompt = f"""
        Create a detailed report for {ticker}:
        - Stock Data: {stock_data}
        - Performance: {performance}
        - Analyst Analysis: {analysis}
        Format as markdown with a table of key metrics and a recommendation.
        """
        
        try:
            report = self.reporter.generate_reply(messages=[{"content": report_prompt, "role": "user"}])
        except Exception as e:
            report = f"Report generation failed: {str(e)}"
        
        return f"{report}\n\n### Price and Volume Charts\n{chart}"