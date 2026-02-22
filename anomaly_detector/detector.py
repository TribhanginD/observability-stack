import time
import requests
import numpy as np
import os

PROMETHEUS_URL = os.getenv("PROMETHEUS_URL", "http://prometheus:9090")

def get_metric(query):
    try:
        response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={'query': query})
        results = response.json()['data']['result']
        if results:
            return float(results[0]['value'][1])
    except Exception as e:
        print(f"Error querying Prometheus: {e}")
    return None

def detect_anomalies():
    history = []
    print("Anomaly detector started. Monitoring 'request_latency'...")
    
    while True:
        val = get_metric('request_latency_current') # Custom metric from simulated stream
        if val is not None:
            history.append(val)
            if len(history) > 30:
                history.pop(0)
                
                mean = np.mean(history)
                std = np.std(history)
                
                if std > 0:
                    z_score = (val - mean) / std
                    if abs(z_score) > 3:
                        print(f"🚨 ANOMALY DETECTED: Latency spike! Value={val:.2f}, Z-Score={z_score:.2f}")
        
        time.sleep(5)

if __name__ == "__main__":
    detect_anomalies()
