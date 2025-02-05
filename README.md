Number Classification API
This is a simple API that classifies numbers based on their mathematical properties and provides a fun fact about them.

Features:
1. Checks if a number is prime, perfect, or Armstrong
2. Determines if the number is odd or even
3. Calculates the sum of digits
4. Fetches a fun fact about the number using Numbers API

API Documentation
Endpoint URL: GET /api/classify-number?number=<your_number>

Request/Response Format:
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

How to run:
1.  Clone the Repository:
git clone https://github.com/Kayce-joy/HNGStage1.git
cd HNGStage1
2.  Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
pip install -r requirements.txt
3. Run the Flask App
python app.py
The API will run at: https://your-app.onrender.com/api/classify-number?number=371

