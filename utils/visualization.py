# utils/visualization.py
import matplotlib.pyplot as plt
import io
import base64
from typing import List

def create_enhanced_charts(ticker: str, prices: List[float], volumes: List[float], 
                         ma20: List[float], ma50: List[float], dates: List[str]) -> str:
    """Create enhanced subplot charts for price, moving averages, and volume"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), height_ratios=[2, 1], sharex=True)
    
    # Price plot with moving averages
    sample_rate = max(1, len(dates) // 50)  # Optimize for readability
    ax1.plot(dates[::sample_rate], prices[::sample_rate], label="Price", color="blue")
    ax1.plot(dates[::sample_rate], ma20[::sample_rate], label="20-day MA", color="orange", linestyle="--")
    ax1.plot(dates[::sample_rate], ma50[::sample_rate], label="50-day MA", color="green", linestyle="--")
    ax1.set_title(f"{ticker} Price History with Moving Averages")
    ax1.set_ylabel("Price ($)")
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Volume plot
    ax2.bar(dates[::sample_rate], volumes[::sample_rate], color="gray", alpha=0.7)
    ax2.set_title(f"{ticker} Trading Volume")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Volume")
    ax2.tick_params(axis="x", rotation=45)
    
    # Optimize layout
    plt.tight_layout()
    
    # Convert to base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", dpi=100, bbox_inches="tight")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    plt.close()
    
    return f"data:image/png;base64,{image_base64}"