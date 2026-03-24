"""
🤖 بوت تحليل العملات الرقمية - تليقرام
نظرية داون + المدرسة الكلاسيكية + تحليل الفيوتشر
Binance Futures | BTC, ETH + عملات رئيسية
الفريمات: 15 دقيقة و 1 ساعة
"""

import os
import asyncio
import logging
from datetime import datetime
import ccxt
import pandas as pd
import pandas_ta as ta
from telegram import Bot
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
import schedule
import time
from threading import Thread

TELEGRAM_TOKEN   = os.environ.get("TELEGRAM_TOKEN", "YOUR_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID")
BINANCE_API_KEY  = os.environ.get("BINANCE_API_KEY", "")
BINANCE_SECRET   = os.environ.get("BINANCE_SECRET", "")

SYMBOLS = ["BTC/USDT","ETH/USDT","BNB/USDT","SOL/USDT","XRP/USDT","ADA/USDT","AVAX/USDT","DOGE/USDT"]
TIMEFRAMES = ["15m", "1h"]
RISK_PERCENT = 1.5
LEVERAGE = 10

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

def get_exchange():
    return ccxt.binance({"enableRateLimit": True, "options": {"defaultType": "future"}})

def fetch_ohlcv(symbol, timeframe, limit=200):
    try:
        df = pd.DataFrame(get_exchange().fetch_ohlcv(symbol, timeframe, limit=limit),
                          columns=["timestamp","open","high","low","close","volume"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df.set_index("timestamp")
    except Exception as e:
        logger.error(f"خطأ {symbol} {​​​​​​​​​​​​​​​​
