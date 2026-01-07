//CASE MANAGEMENT 
import json
import uuid
from datetime import datetime

CASE_FILE = "cases.json"

def load_cases():
    try:
        with open(CASE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_cases(cases):
    with open(CASE_FILE, "w") as file:
        json.dump(cases, file, indent=4)

def create_case(fraud_type, risk_level):
    cases = load_cases()
    case_id = str(uuid.uuid4())[:8]

    cases[case_id] = {
        "fraud_type": fraud_type,
        "risk_level": risk_level,
        "status": "Submitted",
        "created_at": datetime.now().isoformat()
    }

    save_cases(cases)
    return case_id
