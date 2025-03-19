from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
app = Flask(__name__)

role = None  # Global variable to store the selected role

@app.route("/")
def index():
    return render_template("index.html", role=role)  # Pass role to frontend

@app.route('/role', methods=['POST'])
def upload_role():
    global role
    data = request.get_json()
    role = data.get("role")  

    print(f"Selected Role: {role}")  # Debugging

    if not role:
        return jsonify({"msg": False}), 400

    return jsonify({"flag": True})  # Respond to frontend

if __name__ == "__main__":
    app.run(debug=True)
