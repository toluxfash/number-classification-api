# Paste the code here, then press CTRL+X, Y, Enter to save
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    num_str = str(abs(n))  # Use absolute value for Armstrong check
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

# Function to check if a number is perfect
def is_perfect(n):
    if n < 1:
        return False
    return n == sum(i for i in range(1, n) if n % i == 0)

# Function to get a fun fact from Numbers API
def get_fun_fact(number):
    try:
        response = requests.get(f'http://numbersapi.com/{number}/math?json')
        if response.status_code == 200:
            return response.json().get('text')
    except:
        return "No fun fact available."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Input validation
    try:
        number = int(number)
    except (ValueError, TypeError):
        return jsonify({"number": number, "error": True}), 400

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")

    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(number))),  # Handle negative numbers
        "fun_fact": get_fun_fact(number)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Make the API publicly accessible

