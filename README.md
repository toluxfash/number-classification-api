Number Classification API

This project is a Number Classification API that returns interesting mathematical properties of a number, along with a fun fact retrieved from the Numbers API. It is built with Python using Flask and deployed on an AWS EC2 instance.

🚀 Features

Classifies numbers as prime, perfect, Armstrong, even, or odd.
Calculates the sum of digits.
Fetches fun facts about the number using the Numbers API.
Returns JSON responses.
Handles CORS for cross-origin requests.
🛠️ Technology Stack
Programming Language: Python
Framework: Flask
Deployment: AWS EC2 (Ubuntu)
Version Control: GitHub

⚙️ Setup Instructions
Step 1: Install Required Packages
sudo apt update
sudo apt install python3-venv -y

Step 2: Create a Virtual Environment
python3 -m venv venv
#This creates a folder named venv where Python and pip work independently.

Step 3: Activate the Virtual Environment
source venv/bin/activate
#Your terminal should now show (venv) at the start of the line.

Step 4: Install Dependencies
pip install flask requests

Running the API
Run the API (Foreground Mode)
sudo venv/bin/python number_api.py
#This will keep the API running as long as the terminal session is active.
Run the API in Detached Mode (Background)
sudo nohup venv/bin/python number_api.py &
#This command ensures the API runs in the background even if you close the terminal. Logs are saved in nohup.out.

Stop the API
ps aux | grep number_api.py
sudo kill <process_id>

API Endpoint
URL: http://34.234.104.218/api/classify-number?number=371

Method: GET

✅ Success Response (200 OK)

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

http://34.234.104.218/api/classify-number?number=abc

❌ Error Response (400 Bad Request)

{
  "error": true,
  "number": "abc"
}

💡 Troubleshooting

Issue: Externally Managed Environment Error

This error happens because your Python environment is externally managed, restricting system-wide package installations using pip.
Solution:
Install virtual environment:
sudo apt update
sudo apt install python3-venv -y

Create and activate virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install flask requests

Issue: API Stops When Terminal Closes
#To prevent this, run the API using nohup so it stays active even if the terminal session ends:
sudo nohup venv/bin/python number_api.py &

