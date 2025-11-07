# proxy/proxy.py
import requests
from flask import Flask, request, jsonify
app = Flask(__name__)
MODEL_SERVER = "http://model_server:8080/infer"

def rule_check(text):
    if "dropdb" in text.lower() or "exec:" in text.lower():
        return False, "rule: dangerous substring"
    return True, ""

@app.route("/infer", methods=["POST"])
def proxy_infer():
    data = request.json
    text = data.get("text","")
    ok, reason = rule_check(text)
    if not ok:
        return jsonify({"blocked": True, "reason": reason}), 403
    # forward to model server
    r = requests.post(MODEL_SERVER, json={"text": text}, timeout=5)
    resp = r.json()
    # TODO: call anomaly detector (ML) here synchronously or async
    return jsonify({"blocked": False, "model": resp})