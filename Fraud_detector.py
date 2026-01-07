def analyze_fraud(complaint):
    prompt = f"""
    You are a fraud detection assistant.
    Analyze the complaint below and return:
    1. Fraud type
    2. Risk level
    3. Recommended actions

    Complaint:
    {complaint}
    """

    # Simulated LLM response (since API key is not shared)
    response = {
        "fraud_type": "OTP Scam",
        "risk_level": "High",
        "actions": [
            "Block bank account",
            "Report to bank",
            "File complaint on cybercrime portal"
        ]
    }

    return response
  // This shows LLM logic even if API is mocked 
