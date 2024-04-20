from flask import Flask, request, jsonify
from analyze_loan import Loan
from flask import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')
@app.route('/analyze_loan', methods = ['POST'])
def calculate_loan():
    data = request.json
    rate = data.get('rate')
    term = data.get('term')
    loan_amount = data.get('loan_amount')
    
    #calculate details
    loan = Loan(rate, term, loan_amount)
    summary = loan.summary()

    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)