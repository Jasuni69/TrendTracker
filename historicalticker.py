
import yfinance as yf



class HistoricalTicker:
    def __init__(self, ticker_symbol: str):
        self.ticker_symbol = ticker_symbol
        self.ticker = yf.Ticker(ticker_symbol)
        


    def get_historical(self, period:str):
            return self.ticker.history(period=period)