from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Root route for testing
@app.route("/")
def home():
    return "Welcome to the Crypto Recommendation API!"

# Webhook route to handle Dialogflow requests
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        req = request.get_json(force=True)
        print("Received JSON:", req)  

        action = req["queryResult"]["action"]

        if action == "crypto_recommendation":
            criteria = req["queryResult"]["parameters"].get("crypto_criteria", "market_cap")
            response = get_crypto_data(criteria)
            return jsonify({"fulfillmentText": response})

        return jsonify({"fulfillmentText": "Sorry, I didn't understand your request."})

    except Exception as e:
        return jsonify({"fulfillmentText": f"Error processing request: {str(e)}"})

# Function to fetch real-time crypto data based on criteria
def get_crypto_data(criteria):
    try:
        # Map user-friendly criteria to CoinGecko-supported values
        order_map = {
            "growth": "market_cap_desc",
            "market_cap": "market_cap_desc",
            "volume": "volume_desc",
            "popularity": "public_interest_desc"
        }

        # Default to market cap if unknown
        order_value = order_map.get(criteria.lower(), "market_cap_desc")

        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": order_value,
            "per_page": 10,
            "page": 1
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        if not data:
            return f"Sorry, I couldn't find data for {criteria}."

        recommended_coin = data[0]["name"]
        return f"Based on {criteria}, I recommend looking into {recommended_coin}."

    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Handle favicon requests (optional)
@app.route("/favicon.ico")
def favicon():
    return "", 204

if __name__ == "__main__":
    app.run(debug=False, port=5000)