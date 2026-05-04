import random

def predict_defects(git_history_mock):
    """
    Analyzes code churn, complexity, and historical bugs to predict 
    high-risk files for the next release.
    """
    print(f"--- AI Defect Predictor ---")
    
    files = [
        {"name": "auth_service.py", "churn": 85, "complexity": 12, "history": "3 bugs"},
        {"name": "payment_gateway.js", "churn": 92, "complexity": 15, "history": "5 bugs"},
        {"name": "ui_layout.css", "churn": 10, "complexity": 2, "history": "0 bugs"},
        {"name": "db_config.yml", "churn": 5, "complexity": 1, "history": "0 bugs"},
    ]
    
    predictions = []
    for f in files:
        # Simple risk score logic
        risk_score = (f['churn'] * 0.5) + (f['complexity'] * 0.3) + (int(f['history'].split()[0]) * 0.2)
        predictions.append({
            "file": f['name'],
            "risk_score": risk_score,
            "status": "High Risk" if risk_score > 50 else "Stable"
        })
    
    # Sort by risk score
    predictions.sort(key=lambda x: x['risk_score'], reverse=True)
    
    print("\n[Risk Analysis Report]")
    print("-" * 50)
    print(f"{'File Name':<25} | {'Score':<10} | {'Status':<10}")
    print("-" * 50)
    for p in predictions:
        print(f"{p['file']:<25} | {p['risk_score']:<10.1f} | {p['status']:<10}")
    print("-" * 50)
    
    return predictions

if __name__ == "__main__":
    print("Analyzing Git history and code complexity...")
    predict_defects(None)
