Python 示意程式（模擬）
python
複製
編輯
# price_fetcher.py
import requests

def get_binance_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    res = requests.get(url).json()
    return float(res['price'])
python
複製
編輯
# strategy.py
def should_enter_trade(current_price, high_price_last_10min):
    return current_price > high_price_last_10min

def calculate_take_profit(entry_price, target=0.10):
    return round(entry_price * (1 + target), 2)
python
複製
編輯
# main.py
import time
from price_fetcher import get_binance_price
from strategy import should_enter_trade, calculate_take_profit

# 模擬 10 分鐘價格紀錄
price_history = []

while True:
    price = get_binance_price()
    print(f"[Price] {price}")
    price_history.append(price)

    if len(price_history) >= 10:
        high_last_10 = max(price_history[-10:])
        if should_enter_trade(price, high_last_10):
            print("🚀 進場：價格突破")
            take_profit = calculate_take_profit(price)
            print(f"🎯 目標獲利價：{take_profit}")
            # 這裡可以放實際下單或模擬單
            time.sleep(600)  # 模擬等待10分鐘再平倉
            print(f"💰 出場，模擬獲利：+10%")
        else:
            print("🔍 無交易機會")

    time.sleep(60)  # 每分鐘抓一次價格
