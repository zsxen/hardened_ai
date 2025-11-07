from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/infer", methods=["POST"])
def infer():
    text = request.json.get("text","")
    # VERY simple heuristic classifier for demo
    if "password" in text.lower() or "exec:" in text.lower():
        label = "malicious"
    else:
        label = "normal"
    return jsonify({"label": label, "text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)