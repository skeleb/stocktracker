from iexfinance.stocks import Stock


class FinanceDataRetriever:
    # def __init__(self):
    #    pass
    
    def get_batch_stock_quotes(self, tickers):
        data = Stock(tickers)
        stock_quotes = data.get_quote(displayPercent=True)
        
        return stock_quotes

