from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# CONFIGURATION
ACTUAL_BASE_URL = "https://crazy-mushroom.pikapod.net"
BUDGET_ID = "My-Finances-960d1a8"
PASSWORD = "Asm@5632"

def get_actual_data(endpoint):
    url = f"{ACTUAL_BASE_URL}/api/v1/budget/{BUDGET_ID}/{endpoint}"
    response = requests.get(url, auth=("user", PASSWORD))
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed with status {response.status_code}"}

@app.route("/monthly-summary")
def monthly_summary():
    month = request.args.get("month")
    return jsonify(get_actual_data(f"month/{month}/categories"))

@app.route("/transactions")
def transactions():
    month = request.args.get("month")
    return jsonify(get_actual_data(f"month/{month}/transactions"))

@app.route("/net-worth")
def net_worth():
    return jsonify(get_actual_data("net-worth"))

@app.route("/balances")
def balances():
    return jsonify(get_actual_data("balances"))

@app.route("/accounts")
def accounts():
    return jsonify(get_actual_data("accounts"))

@app.route("/budget-vs-actual")
def budget_vs_actual():
    month = request.args.get("month")
    return jsonify(get_actual_data(f"month/{month}/budget-vs-actual"))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
