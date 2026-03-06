AI Crypto Chatbot
A Flask-based chatbot that provides cryptocurrency recommendations based on user input. It fetches real-time data from the CoinGecko API and suggests top-performing cryptocurrencies based on market cap, volume, and popularity.

Features
Real-time cryptocurrency data from the CoinGecko API

Dialogflow webhook integration

Customizable recommendation criteria (market cap, volume, popularity)

Easy to run locally using Flask

Installation
1. Clone the repository
bash
git clone https://github.com/<your-username>/ai-crypto-chatbot.git
cd ai-crypto-chatbot
2. Install dependencies
bash
pip install -r requirements.txt
3. Run the Flask app
bash
python app.py
Your app will be running at:
http://127.0.0.1:5000/

API Endpoints
/webhook
Dialogflow webhook endpoint for processing cryptocurrency recommendations.

Example POST request:

json
{
  "queryResult": {
    "action": "crypto_recommendation",
    "parameters": {
      "crypto_criteria": "market_cap"
    }
  }
}
Deployment (Google Cloud App Engine)
1. Create app.yaml
yaml
runtime: python310
entrypoint: gunicorn -b :$PORT app:app

instance_class: F2

env_variables:
  FLASK_ENV: "production"

handlers:
  - url: /favicon.ico
    static_files: favicon.ico
    upload: favicon.ico

  - url: /.*
    script: auto
2. Deploy the app
bash
gcloud app deploy
3. Access the deployed app
Code
https://<your-project-id>.uc.r.appspot.com/
Technologies Used
Python 3.x

Flask

CoinGecko API

Dialogflow

License
This project is licensed under the MIT License. See the LICENSE file for details.
