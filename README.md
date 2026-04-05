

# AI Crypto Chatbot

A simple Flask webhook for Google Dialogflow that recommends the top cryptocurrency using the CoinGecko API.

## Features

- Real-time data from CoinGecko API
- Dialogflow webhook integration
- Supports criteria: `market_cap`, `volume`, `popularity`, `growth`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-crypto-chatbot.git
   cd ai-crypto-chatbot

Install dependencies:bash

pip install flask requests

Run the application:bash

python app.py

The app will be available at: http://127.0.0.1:5000Webhook EndpointPOST /webhookExample request:json

{
  "queryResult": {
    "action": "crypto_recommendation",
    "parameters": {
      "crypto_criteria": "market_cap"
    }
  }
}

Deployment (Google App Engine)Create app.yaml:yaml

runtime: python310
entrypoint: gunicorn -b :$PORT app:app

Deploy:bash

gcloud app deploy

LicenseMIT License

---

Would you like me to make it even shorter, or add anything else? Just copy the whole thing above into your `README.md` file.

