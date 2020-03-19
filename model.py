import urllib.request
from bs4 import BeautifulSoup

from datetime import datetime
from dateutil import tz
from pytz import timezone
import time

class Model:
  def getStockPrice(self, STOCK_NAME):
    STOCK_URL = "https://finance.yahoo.com/quote/" + STOCK_NAME
    STOCK_URL_PAGE = urllib.request.urlopen(STOCK_URL)
    html = BeautifulSoup(STOCK_URL_PAGE, 'html.parser')
    MAIN_ID = html.find(id="quote-header-info").descendants
    STOCK_INFO = [stock_info.text for stock_info in MAIN_ID if stock_info.name == "span"]
    stock_price = STOCK_INFO[1]
    return stock_price

  def getTime(self):
    utc = timezone('UTC')
    now = utc.localize(datetime.utcnow())
    est = timezone('US/Eastern')
    local_time = now.astimezone(est).strftime("%H:%M:%S")
    d = datetime.strptime(local_time, "%H:%M:%S").strftime("%I:%M:%S %p")
    return d

  def strategy1(self, STOCK_PRICE):
    MAX_BUY_PRICE = 108.71
    MAX_SELL_PRICE = 108.71
    msg = ""
    if STOCK_PRICE < MAX_BUY_PRICE:
      return "*BUY*"
    elif STOCK_PRICE > MAX_SELL_PRICE:
      return "*SELL*"
    else:
      return "NOTHING DONE"
