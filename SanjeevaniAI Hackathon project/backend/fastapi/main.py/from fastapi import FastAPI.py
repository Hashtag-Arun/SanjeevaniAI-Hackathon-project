from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from collections import Counter

app = FastAPI()

donors = [
    {"name": "Arun", "blood_group": "A+", "last_donation": 30, "donations": 4},
    {"name": "Varun", "blood_group": "B+", "last_donation": 60, "donations": 2},
    {"name": "Liya", "blood_group": "O-", "last_donation": 15, "donations": 5},
    {"name": "Ramiya", "blood_group": "AB+", "last_donation": 10, "donations": 3},
    {"name": "Soniya", "blood_group": "A-", "last_donation": 80, "donations": 6},
    {"name": "Praddep", "blood_group": "B-", "last_donation": 90, "donations": 1},
    {"name": "Duptha", "blood_group": "O+", "last_donation": 20, "donations": 7}
]

class PredictRequest(BaseModel):
    name: str

class ChatRequest(BaseModel):
    message: str

class HealthCheckRequest(BaseModel):
    hemoglobin_level: float
    has_fever: bool
    recent_surgery: bool

@app.post("/predict")
def predict_availability(data: PredictRequest):
    donor = next((d for d in donors if d['name'].lower() == data.name.lower()), None)
    if not donor:
        return {"error": "Donor not found"}
    return {
        "name": donor["name"],
        "next_eligible_in_days": max(0, 90 - donor["last_donation"])
    }

@app.post("/chat")
def chat(data: ChatRequest):
    msg = data.message.lower()
    if "donate" in msg:
        return {"response": "Healthy individuals can donate every 90 days."}
    elif "thalassemia" in msg:
        return {"response": "Thalassemia is a blood disorder needing regular transfusion."}
    else:
        return {"response": "I'm here to help. Ask me about blood donation or care."}

@app.post("/check-eligibility")
def check_eligibility(data: HealthCheckRequest):
    eligible = data.hemoglobin_level >= 12.5 and not data.has_fever and not data.recent_surgery
    return {
        "eligible": eligible,
        "safety_score": int(data.hemoglobin_level * 7) if eligible else 40,
        "reason": "All conditions good." if eligible else "Health indicators not suitable."
    }

@app.get("/blood-stats")
def blood_stats():
    stats = Counter(d["blood_group"] for d in donors)
    critical = [bg for bg, count in stats.items() if count <= 1]
    most_common = stats.most_common(1)[0][0]
    return {
        "summary": stats,
        "prediction": {
            "most_common": most_common,
            "critical": critical
        }
    }

@app.get("/donor-trust/{name}")
def donor_trust(name: str):
    donor = next((d for d in donors if d['name'].lower() == name.lower()), None)
    if not donor:
        return {"error": "Donor not found"}
    trust = min(100, donor["donations"] * 20 - donor["last_donation"] // 10)
    return {
        "name": donor["name"],
        "donations": donor["donations"],
        "last_donation_days_ago": donor["last_donation"],
        "trust_score": trust,
        "status": "Highly Trusted" if trust >= 75 else "Moderate"
    }
