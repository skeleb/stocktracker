import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from stocktracker.finance_data_retriever import FinanceDataRetriever


bp = Blueprint('stocks', __name__, url_prefix='/stocks')
data_retriever = FinanceDataRetriever()

@bp.route("/")
def show_stockdata():
    stocks_list = ["AAPL", "QCOM", "KO", "V", "DIS"]
    stock_quotes = data_retriever.get_batch_stock_quotes(stocks_list)
    
    return render_template("stocks.j2", data=stock_quotes)
