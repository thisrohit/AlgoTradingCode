import kiteAPI
import kiteconnect
from flask import Flask, request

app = Flask(__name__)

@app.route('/callback')
def callback():
    # Extract the authorization code from the query parameters
    auth_code = request.args.get('code')

    if auth_code:
        # If an authorization code is present, you can proceed to exchange it for an access token
        # Include your code here to exchange the auth_code for an access token with Zerodha

        # Placeholder for the actual logic
        # Replace the following lines with the actual code to exchange the auth_code for an access token
        access_token = 'your_access_token'
        token_type = 'Bearer'

        # Your application logic with the obtained access_token
        return f'Callback received! Access Token: {access_token}, Token Type: {token_type}'

    else:
        # Handle the case where there is no authorization code
        return 'Error: No authorization code received in the callback.'

#connecting to zerodha server
kite = kiteconnect.KiteConnect(api_key='my_API_Key', api_secret='my_api_secret')

stock_tick = 'RELIANCE'
ticker = kite.ticker_data([stock_tick])
current_price = ticker[stock_tick]['last_price']

#uptill here building connection

#calcuating the moving average
short_term_avg = sum(current_price[-10:])/10
long_term_avg = sum(current_price[-20:])/20

#generate trading signal
if short_term_avg > long_term_avg:
    signal = 'BUY'
elif short_term_avg < long_term_avg:
    signal = 'SELL'
else:
    signal = 'HOLD'
    
#execute the trade based on signal
if signal == 'BUY':
    order_param = {
        'exchange': kite.EXCHANGE_NSE,
        'tradingsymbol': stock_tick,
        'qty': 100,
        'order_type':kite.ORDER_TYPE_MARKET,
        'side':kite.ORDER_SIDE_BUY
    }
    kite.place_order(order_param)
elif signal == 'SELL':
    order_param = {
        'exchange': kite.EXCHANGE_NSE,
        'tradingsymbol': stock_tick,
        'qty': 100,
        'order_type':kite.ORDER_TYPE_MARKET,
        'side':kite.ORDER_SIDE_SELL
    }
    kite.place_order(order_param)
    
    