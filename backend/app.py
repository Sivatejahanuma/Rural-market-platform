from flask import Flask, jsonify, request
from flask_cors import CORS
from oracle_connection import get_connection
from price_ai_model import get_price_advice

app = Flask(__name__)
CORS(app)   # allow frontend calls

@app.route("/")
def home():
    return "AI Rural Market Platform Backend Running"

# ---------------- Fetch Market Prices From Oracle DB ------------------
@app.route("/api/prices", methods=["GET"])
def get_prices():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # IMPORTANT: Access fully qualified table in SYSTEM schema
        query = "SELECT crop_name, market_price FROM SYSTEM.CROP_PRICES"

        cursor.execute(query)

        rows = cursor.fetchall()
        result = [{"crop": r[0], "price": r[1]} for r in rows]

        cursor.close()
        conn.close()

        return jsonify(result)
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

# ---------------- Local AI Recommendation ------------------
@app.route("/api/advice", methods=["POST"])
def advice():
    data = request.json
    crop_name = data.get("crop")

    result = get_price_advice(crop_name)
    return jsonify({"advice": result})

if __name__ == "__main__":
    app.run(debug=True)
