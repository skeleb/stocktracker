import unittest

from stocktracker.finance_data_retriever import FinanceDataRetriever


class TestFinanceDataRetriever(unittest.TestCase):
    def setUp(self):
        self.data_retriever = FinanceDataRetriever()
    
    def test_get_batch_stock_quotes(self):
        tickers = ["AAPL", "MSFT", "V"]
        expected_data = [1, 2, 3]
        actual_data = self.data_retriever.get_batch_stock_quotes(tickers)

        return "moi"
        