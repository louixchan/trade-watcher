import requests
import json
import hmac
import hashlib
import base64
import time
from Crypto.Cipher import AES

class BittrexClient(object):

	__API_KEY__ = ''
	__SECRET_KEY__ = ''
	__BASE_LINK__ = 'https://bittrex.com/api/v1.1/'

	def __init__(self, API_KEY, SECRET_KEY):

		self.__API_KEY__ = API_KEY
		self.__SECRET_KEY__ = SECRET_KEY

	def getResponse(self, link, data=None):

		s = requests.session()

		req = requests.Request('GET', url=link, data=data)

		prep = req.prepare()

		resp = json.loads(s.send(prep).text)

		if resp['success']:

			return resp['message'], resp['result']

		else:

			return resp['message'], None

	# ===========
	# ACCOUNT API
	# ===========
	def getBalances(self):

		if self.__API_KEY__ == '':

			return 'Please initialise with your API Key first.', None

		return self.getResponse(self.__BASE_LINK__ + 'account/getbalances?apikey=' + self.__API_KEY__)



	def getBalance(self, currency):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'account/getbalance'

		data = {
			'apikey': self.__API_KEY__,
			'currency': currency
		}

		return self.getResponse(link=link, data=data)

	def getDepositAddress(self, currency):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'account/getdepositaddress'

		data = {
			'apikey': self.__API_KEY__,
			'currency': currency,
			'nonce': time.time()
		}

		return self.getResponse(link=link, data=data)

	def withdrawal(self, currency, quantity, address, paymentid):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'account/withdrawal'

		data = {
			'apikey': self.__API_KEY__,
			'currency': currency,
			'quantity': quantity,
			'address': address
		}

		if paymentid is not None:

			data['paymentid'] = paymentid

		return self.getResponse(link=link, data=data)

	def getOrder(self, uuid):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'account/getorder'

		data = {
			'apikey': self.__API_KEY__,
			'uuid': uuid
		}

		return self.getResponse(link=link, data=data)

	def getOrderHistory(self, market):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'account/getorderhistory'

		data = {
			'apikey': self.__API_KEY__,
			'market': market
		}

		return self.getResponse(link=link, data=data)

	def getWithdrawalHistory(self, currency):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'account/getwithdrawalhistory'

		data = {
			'apikey': self.__API_KEY__,
			'currency': currency
		}

		return self.getResponse(link=link, data=data)

	def getDepositHistory(self, currency):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'account/getdeposithistory'

		data = {
			'apikey': self.__API_KEY__,
			'currency': currency
		}

		return self.getResponse(link=link, data=data)

	# ==========
	# PUBLIC API
	# ==========

	def getMarkets(self):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'public/getmarkets'

		data = {
			'apikey': self.__API_KEY__
		}

		return self.getResponse(link=link, data=data)

	def getCurrencies(self):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'public/getcurrencies'

		data = {
			'apikey': self.__API_KEY__
		}

		return self.getResponse(link=link, data=data)

	def getTicker(self, market):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'public/getticker'

		data = {
			'apikey': self.__API_KEY__,
			'market': market
		}

		return self.getResponse(link=link, data=data)

	def getMarketSummaries(self):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'public/getmarketsummaries'

		data = {
			'apikey': self.__API_KEY__
		}

		return self.getResponse(link=link, data=data)

	def getMarketSummary(self, market):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'public/getmarketsummary'

		data = {
			'apikey': self.__API_KEY__,
			'market': market
		}

		return self.getResponse(link=link, data=data)

	def getOrderBook(self, market, type='both'):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'public/getorderbook'

		data = {
			'apikey': self.__API_KEY__,
			'market': market,
			'type': type
		}

		return self.getResponse(link=link, data=data)

	def getMarketHistory(self, market):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'public/getmarkethistory'

		data = {
			'apikey': self.__API_KEY__,
			'market': market
		}

		return self.getResponse(link=link, data=data)

	# ==========
	# MARKET API
	# ==========

	def buyLimit(self, market, quantity=0.0, rate=0.0):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'public/buylimit'

		data = {
			'apikey': self.__API_KEY__,
			'market': market,
			'quantity': quantity,
			'rate': rate
		}

		return self.getResponse(link=link, data=data)

	def sellLimit(self, market, quantity=0.0, rate=0.0):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'public/buylimit'

		data = {
			'apikey': self.__API_KEY__,
			'market': market,
			'quantity': quantity,
			'rate': rate
		}

		return self.getResponse(link=link, data=data)

	def cancel(self, uuid):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'public/cancel'

		data = {
			'apikey': self.__API_KEY__,
			'uuid': uuid
		}

		return self.getResponse(link=link, data=data)

	def getOpenOrders(self, market):

		if self.__API_KEY__ == '':
			return 'Please initialise with your API Key first.', None

		link = self.__BASE_LINK__ + 'public/getopenorders'

		data = {
			'apikey': self.__API_KEY__,
			'market': market
		}

		return self.getResponse(link=link, data=data)

