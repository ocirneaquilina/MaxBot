import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import urllib
from urllib.request import urlopen, Request
import datetime as dt
import common.config as cfg
from common.http import request

class CoinGecko:
    def __init__(self):
        self.req = request.MyRequest()
        # self.headers = { 'X-CMC_PRO_API_KEY': cfg.settings['X-CMC_PRO_API_KEY1']}
        # self.headers2 = { 'X-CMC_PRO_API_KEY': cfg.settings['X-CMC_PRO_API_KEY2']}
        # self.compute_financials()

    def build_model(self, assetsUSD, assetsBTC):
        pass
        # self.assets = []

        # for idx, asset in enumerate(assetsUSD):
        #     self.assets.append(
        #         {
        #             'name':                 asset['name'],
        #             'symbol':               asset['symbol'],
        #             'financials': {
        #                 'USD': {
        #                     'price':                asset['quote']['USD']['price'],
        #                     'volume_24h':           asset['quote']['USD']['volume_24h'],
        #                     'percent_change_1h':    asset['quote']['USD']['percent_change_1h'],
        #                     'percent_change_24h':   asset['quote']['USD']['percent_change_24h'],
        #                     'percent_change_7d':    asset['quote']['USD']['percent_change_7d'],
        #                     'market_cap':           asset['quote']['USD']['market_cap'],
        #                 },
        #                 'BTC': {
        #                     'price':                assetsBTC[idx]['quote']['BTC']['price'],
        #                     'volume_24h':           assetsBTC[idx]['quote']['BTC']['volume_24h'],
        #                     'percent_change_1h':    assetsBTC[idx]['quote']['BTC']['percent_change_1h'],
        #                     'percent_change_24h':   assetsBTC[idx]['quote']['BTC']['percent_change_24h'],
        #                     'percent_change_7d':    assetsBTC[idx]['quote']['BTC']['percent_change_7d'],
        #                     'market_cap':           assetsBTC[idx]['quote']['BTC']['market_cap'],
        #                 },
        #                 'created_date': dt.datetime.now()
        #             },
        #         }
        #     )

    def compute_financials(self):
        pass
        # assetsUSD = self.req.get_data(cfg.settings['COINMARKETCAP_LISTINGS'], self.headers, cfg.settings['params']['USD'])
        # assetsBTC = self.req.get_data(cfg.settings['COINMARKETCAP_LISTINGS'], self.headers2, cfg.settings['params']['BTC'])

        # self.build_model(assetsUSD, assetsBTC)

    def trim_financials(self, token):
        pass
        # financials = dict(self.assets[
        #         self.assets.index(list(filter(lambda n: n.get('symbol').lower() == token.lower(), self.assets))[0])])
        # try:
        #     del financials["name"]
        #     del financials["symbol"]
        # except KeyError:
        #     print("Key 'name'/'symbol' not found")
        
        # return financials['financials']

    def get_asset(self, token):
        pass
        # if list(filter(lambda n: n.get('symbol').lower() == token.lower(), self.assets)):
        #     return self.trim_financials(token)

    def get_financials(self, token):
        pass
        # asset_financials = self.get_asset(token)
        # return asset_financials if asset_financials else None