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
    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    return sum(digit ** power for digit in digits) == n

def is_perfect(n):
    if n <= 0:  
        return False
    return sum([i for i in range(1, n) if n % i == 0]) == n

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    num = request.args.get("number")
    
    if not num or not num.isdigit():
        return jsonify({"number": num, "error": True}), 400
    
    num = int(num)
    properties = []
    
    if is_armstrong(num):
        properties.append("armstrong")
    
    properties.append("odd" if num % 2 else "even")
    
    # Fetch fun fact with updated URL format

    response = requests.get(f'http://numbersapi.com/{int(num)}/math?json=true')
    if response.status_code == 200:
        fun_fact = response.json().get('text', 'No fun fact found.')  
    
    return jsonify({
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(num)),
        "fun_fact": fun_fact
    })

if __name__ == '__main__':
    app.run(debug=True)
