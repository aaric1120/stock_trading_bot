import alpaca_trade_api as trade_api

API_ENDPOINT = "https://paper-api.alpaca.markets"
API_KEY_ID = 'PKERBDG0NJ9A3XAMW0Q9'
API_SECRET_KEY = 'XuTnT3qpoYZxyL22JaU75oM2mIJT7FqC9iNmuD9g'

api = trade_api.REST(API_KEY_ID, API_SECRET_KEY,API_ENDPOINT, api_version='v2')
account = api.get_account()
print(api.list_positions())
print(api.list_orders())