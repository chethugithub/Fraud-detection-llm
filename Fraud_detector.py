from case_tracker import create_case

def analyze_fraud(complaint):
    """
    Simulates LLM-based fraud detection using predefined logic.
    """

    complaint_lower = complaint.lower()

    if "otp" in complaint_lower:
        fraud_type = "OTP Scam"
        risk_level = "High"
        actions = [
            "Block bank account immediately",
            "Report to bank fraud department",
            "File complaint on cybercrime portal"
        ]

    elif "link" in complaint_lower:
        fraud_type = "Phishing Attack"
        risk_level = "Medium"
        actions = [
            "Change passwords",
            "Scan device for malware",
            "Report phishing link"
        ]

    else:
        fraud_type = "Suspicious Activity"
        risk_level = "Low"
        actions = [
            "Monitor account activity",
            "Contact bank for verification"
        ]

    return fraud_type, risk_level, actions


def main():
    print("Fraud Detection System (LLM Powered)\n")

    complaint = input("Enter customer complaint: ")
    fraud_type, risk_level, actions = analyze_fraud(complaint)

    case_id = create_case(fraud_type, risk_level)

    print("\nFraud Analysis Result")
    print("----------------------")
    print(f"Fraud Type : {fraud_type}")
    print(f"Risk Level: {risk_level}")
    print(f"Case ID   : {case_id}")

    print("\nRecommended Actions:")
    for action in actions:
        print("-", action)


if __name__ == "__main__":
    main()
