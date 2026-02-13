# AI Crypto Chatbot

## Description

A Flask-based chatbot that provides cryptocurrency recommendations based on user input. The bot fetches real-time data using the CoinGecko API and suggests top-performing cryptocurrencies based on various criteria like **market cap**, **volume**, and **popularity**.

## Features
- Real-time cryptocurrency data fetched from the CoinGecko API.
- Webhook integration with Dialogflow.
- Customizable criteria for coin recommendations (e.g., market cap, volume, popularity).
- Simple to run locally with Flask.

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/<your-username>/ai-crypto-chatbot.git
cd ai-crypto-chatbot

### 2. Install the dependencies:
pip install -r requirements.txt

### 3. Run the Flask app:
python app.py


Your app will be running at http://127.0.0.1:5000/.

API Endpoints

/webhook: The Dialogflow webhook endpoint for processing cryptocurrency recommendations.

Example of POST request (via Postman or cURL):
{
  "queryResult": {
    "action": "crypto_recommendation",
    "parameters": {
      "crypto_criteria": "market_cap"
    }
  }
}

Deployment
Google Cloud App Engine (Deployment Steps Coming Soon)

The app can be deployed to Google Cloud for public access. The deployment steps are still pending due to permission and bucket configuration issues.

Technologies Used:

Python 3.x

Flask for web framework

CoinGecko API for fetching cryptocurrency data

Dialogflow for chatbot integration (webhook)

License

This project is licensed under the MIT License. See the LICENSE
 file for details.

Acknowledgments

CoinGecko for providing the free crypto data API.

Dialogflow for enabling chatbot integration.