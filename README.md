

# AI Crypto Chatbot

A simple Flask-based webhook for Dialogflow that provides real-time cryptocurrency recommendations using the **CoinGecko API**.

It suggests the top cryptocurrency based on user-selected criteria like market cap, volume, or popularity.

## Features

- Real-time data from CoinGecko API
- Dialogflow webhook integration
- Supports multiple recommendation criteria:
  - Market Cap
  - Trading Volume
  - Popularity / Interest
- Lightweight and easy to deploy

## Tech Stack

- Python 3
- Flask
- CoinGecko API

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-crypto-chatbot.git
cd ai-crypto-chatbot

2. Install Dependenciesbash

pip install flask requests

3. Run Locallybash

python app.py

The app will start at: http://127.0.0.1:5000API EndpointsGET /Simple health check / welcome message.POST /webhookDialogflow webhook endpoint.Example Request:json

{
  "queryResult": {
    "action": "crypto_recommendation",
    "parameters": {
      "crypto_criteria": "market_cap"
    }
  }
}

Supported Criteria:market_cap (default)
volume
popularity
growth

Usage Examples (Dialogflow)"Recommend me a cryptocurrency by market cap"
"Show top coin by volume"
"What is the most popular crypto right now?"

Note: Currently, the bot returns only the top 1 coin based on the selected criteria.Deployment (Google Cloud App Engine)Create an app.yaml file:yaml

runtime: python310
entrypoint: python app.py

instance_class: F2

Then deploy:bash

gcloud app deploy

Your app URL will be: https://YOUR_PROJECT_ID.uc.r.appspot.comLimitations (Current Version)Returns only one recommended coin
No limit parameter support yet
No advanced formatting or multiple suggestions
Basic error handling

Future ImprovementsReturn top 5–10 coins
Add price, 24h change, and market cap in response
Better natural language handling
Add more criteria (24h gainers, etc.)


