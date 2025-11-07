# ml/train_detector.py (sketch)
import json, numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

def load_windows(path):
    X=[]; y=[]
    for line in open(path):
        obj=json.loads(line)
        X.append(obj["features"])
        y.append(1 if obj.get("label","normal")!="normal" else 0)
    return np.array(X), np.array(y)

X,y = load_windows("windows.jsonl")
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X,y)
joblib.dump(clf, "detector.pkl")
print("Trained. classification report:")
print(classification_report(y, clf.predict(X)))