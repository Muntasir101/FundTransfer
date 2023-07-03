from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/transfer', methods=['POST'])
def transfer():
    # Retrieve form data
    transfer_amount = float(request.form['transfer_amount'])
    transfer_type = request.form['transfer_type']
    account_type = request.form['account_type']

    # Perform necessary calculations based on transfer type and account type
    fee = 0
    if transfer_type == 'standard':
        fee = 2
        if transfer_amount >= 1000:
            fee += transfer_amount * 0.01
    elif transfer_type == 'express':
        fee = 5
        if transfer_amount < 1000:
            fee += transfer_amount * 0.02
        if transfer_amount >= 1000:
            fee += transfer_amount * 0.03
    elif transfer_type == 'international':
        fee = 10

    # Check transfer limits based on account type
    transfer_limit = 0
    if account_type == 'savings':
        transfer_limit = 5000
    elif account_type == 'current':
        transfer_limit = 10000

    # Validate transfer amount against transfer limit
    if transfer_amount > transfer_limit:
        #return render_template('result.html', error='Transfer amount exceeds transfer limit.')
        return render_template('error.html')

    # Calculate total amount
    total_amount = transfer_amount + fee

    return render_template('result.html', transfer_amount=transfer_amount, fee=fee, total_amount=total_amount)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
