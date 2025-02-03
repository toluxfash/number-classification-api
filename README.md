Number Classification API

This Number Classification API is a Python-based application that classifies numbers by calculating their mathematical properties, such as whether they are prime, perfect, Armstrong, even, or odd. The API also retrieves a fun fact about the number from the Numbers API. It is built using the Flask framework and deployed on an AWS EC2 instance for public access.
🚀 Features

    Classifies numbers as prime, perfect, Armstrong, even, or odd.
    Calculates the sum of digits of a given number.
    Fetches fun facts about the number using the Numbers API.
    Returns JSON responses that can be easily integrated with other services.
    Handles CORS for cross-origin requests, making it suitable for web and mobile apps.

🛠️ Technology Stack

    Programming Language: Python
    Framework: Flask
    Deployment: AWS EC2 (Ubuntu)
    Version Control: GitHub
    API Hosting: Publicly accessible through EC2's public IP.

⚙️ Setup Instructions
Step 1: Install Required Packages

Before setting up the application, you need to install some required packages.

sudo apt update
sudo apt install python3-venv -y

Step 2: Create a Virtual Environment

Next, create a virtual environment to isolate the project dependencies.

python3 -m venv venv

This will create a folder named venv, where Python and pip will work independently.
Step 3: Activate the Virtual Environment

Activate the virtual environment using the following command:

source venv/bin/activate

Once activated, your terminal should show (venv) at the start of the line, indicating you're in the virtual environment.
Step 4: Install Dependencies

Now, install the necessary dependencies for the project.

pip install flask requests

⚡ Running the API

Once the setup is complete, you can run the API.
Running the API in Foreground Mode

Run the API in the terminal as follows:

sudo venv/bin/python number_api.py

This will keep the API running as long as the terminal session is active.
Running the API in Detached Mode (Background)

To ensure the API keeps running even if the terminal is closed, you can run it in the background:

sudo nohup venv/bin/python number_api.py &

Logs are saved in the nohup.out file.
Stopping the API

If you need to stop the API, you can do so by finding the process ID and killing it:

ps aux | grep number_api.py
sudo kill <process_id>

📡 API Endpoint

Once the API is running, you can make a request to the endpoint:

URL: http://<EC2-Public-IP>/api/classify-number?number=371

Method: GET
✅ Success Response (200 OK)

When a valid number is provided, the API returns a JSON response with the mathematical properties and a fun fact about the number:

{
  "digit_sum": 11,
  "fun_fact": "371 is a narcissistic number.",
  "is_perfect": false,
  "is_prime": false,
  "number": 371,
  "properties": [
    "armstrong",
    "odd"
  ]
}

❌ Error Response (400 Bad Request)

If an invalid number is passed, the API will return an error message:

{
  "error": true,
  "number": "abc"
}

💡 Troubleshooting
Issue: Externally Managed Environment Error

Problem: This error occurs because your Python environment is externally managed, which restricts system-wide package installations using pip.

Solution:

    Install the virtual environment:

sudo apt update
sudo apt install python3-venv -y

Create and activate the virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

    pip install flask requests

Issue: API Stops When Terminal Closes

Problem: By default, the API stops when the terminal session is closed.

Solution: To prevent this, run the API using nohup so it stays active even after the terminal session ends:

sudo nohup venv/bin/python number_api.py &

💻 Code Explanation

The code for the API is structured as follows:
Flask Setup

    Flask is a lightweight Python micro-framework that simplifies the process of building APIs.

Helper Functions

    is_prime(n): Checks if a number is prime.
    is_armstrong(n): Checks if the number is an Armstrong (narcissistic) number.
    is_perfect(n): Checks if the number is a perfect number.
    get_fun_fact(number): Fetches a fun fact from the Numbers API for a given number.

API Endpoint

    The API listens for GET requests at /api/classify-number?number=371.
    The endpoint validates the input, checks the properties of the number, and returns a JSON response with the classification, sum of digits, and a fun fact.

Deployment Setup

    host='0.0.0.0' makes the API publicly accessible, allowing it to be accessed from any IP.
    port=80 runs the API on the default HTTP port (80).

📁 Code

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

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
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

# Function to check if a number is perfect
def is_perfect(n):
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
    if not number or not number.isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")

    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(number)),
        "fun_fact": get_fun_fact(number)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Make the API publicly accessible

