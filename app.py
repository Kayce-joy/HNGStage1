from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Number Classifier API! Use /api/classify-number?number=YOUR_NUMBER"

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    digits = [int(digit) for digit in str(abs(n))]  # Handle negative numbers
    power = len(digits)
    return sum(digit ** power for digit in digits) == abs(n)

def is_perfect(n):
    if n <= 0:
        return False
    return sum([i for i in range(1, n) if n % i == 0]) == n

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    num = request.args.get("number")
    
    # Return error if the number is not provided
    if not num: 
        return jsonify({"number": "null", "error": True}), 400

    # Validate that the input is numeric or a valid negative number
    if not num.isdigit() and not (num.startswith('-') and num[1:].isdigit()):
        return jsonify({"number": num, "error": True}), 400
    
    num = int(num)
    properties = []
    
    # Classify number properties
    if num >= 0:
        if is_armstrong(num):
            properties.append("armstrong")
        
        if is_prime(num):
            properties.append("prime")
        
        if is_perfect(num):
            properties.append("perfect")
    
    properties.append("odd" if num % 2 else "even")
    
    # Retrieve fun fact from numbersapi
    response = requests.get(f'http://numbersapi.com/{abs(num)}/math?json=true')
    if response.status_code == 200:
        fun_fact = response.json().get('text', 'No fun fact found.')  
    else:
        fun_fact = "No fun fact found."

    return jsonify({
        "number": num,
        "is_prime": is_prime(num) if num >= 0 else False,
        "is_perfect": is_perfect(num) if num >= 0 else False,
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(num))),  
        "fun_fact": fun_fact
    })

if __name__ == '__main__':
    app.run(debug=True)
