from flask import Flask, redirect, url_for


app = Flask(__name__)
paypalURL = 'https://www.sandbox.paypal.com/cgi-bin/webscr' 
#Test PayPal API URL

paypalID = 'kmaliseller@gmail.com'
#Business Email



amount='200'
uid='25'
pname='car'
@app.route("/")
def index():
	return ("""
    <img src="{{ url_for('static', filename='images/home_images/score-board.png')}}   height='100' width='200'/>
    <br>
    Name:'Kuldeep Mali'
    <br>
    Price:200
    <form action='"""+paypalURL+"""' method="get">
        <!-- Identify your business so that you can collect the payments. -->
        <input type="hidden" name="business" value='"""+paypalID+"""'>
        
        <!-- Specify a Buy Now button. -->
        <input type="hidden" name="cmd" value="_xclick">
        
        <!-- Specify details about the item that buyers will purchase. -->
        <input type="hidden" name="pid" value='12'>
        <input type="hidden" name="item_name" value='"""+pname+"""'>
        <input type="hidden" name="item_number" value="1">
        <input type="hidden" name="amount" value='"""+amount+"""'>
        <input type="hidden" name="currency_code" value="USD">
        
        <!-- Specify URLs -->
        <input type='hidden' name='cancel_return' value='/cancelpage'>
        <input type='hidden' name='return' value='/successpay?pid="""+pid+"""&uid="""+uid+"""&amount="""+amount+"""'>
        
        <!-- Display the payment button. -->
        <input type="image" name="submit" border="0"
        src="https://www.paypalobjects.com/en_US/i/btn/btn_buynow_LG.gif" alt="PayPal - The safer, easier way to pay online">
        <img alt="" border="0" width="1" height="1" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" >
    </form>
""")
if __name__ == '__main__':
    app.run()