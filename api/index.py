from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Verification API Running"


@app.route("/api/check", methods=["GET"])
def check():

    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify({
            "success": False,
            "message": "user_id is required"
        }), 400

    return jsonify({
        "success": True,
        "verified": True,
        "user_id": user_id,
        "message": "Successfully Verified"
    })
