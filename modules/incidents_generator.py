import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_incidents(n=1000):
    """Kaza, yaralanma ve açıklama verileri üretir."""
    injury_types = {
        "Fatalities": (10, 300),
        "Serious Injury": (10, 400),
        "Moderate Injury": (50, 1500),
        "Minor Injury": (20, 1500)
    }
    causes = [
        "Pesticide poisoning", "Machinery malfunction", "Animal attack",
        "Crop fire", "Flood damage", "Drought impact",
        "Falling from tractor", "Chemical burn", "Snake bite", "Heavy equipment accident"
    ]

    latitudes = np.random.uniform(-16.78, -8.81, n)
    longitudes = np.random.uniform(31.71, 35.67, n)
    injuries = [random.choice(list(injury_types.keys())) for _ in range(n)]
    values = [random.randint(*injury_types[i]) for i in injuries]
    incident_causes = [random.choice(causes) for _ in range(n)]

    df = pd.DataFrame({
        "latitude": latitudes,
        "longitude": longitudes,
        "incident_cause": incident_causes,
        "injury_type": injuries,
        "value": values
    })

    # Tarih ve açıklama ekle
    start, end = datetime(2019, 6, 1), datetime(2019, 6, 30)
    descriptions = [
        "Road accident", "Vehicle collision", "Pedestrian hit",
        "Single vehicle crash", "Multiple vehicle accident",
        "Hit and run", "Roadside emergency", "Traffic jam due to accident"
    ]
    def random_date():
        delta = end - start
        return start + timedelta(seconds=random.randint(0, int(delta.total_seconds())))
    df["datetime"] = [random_date() for _ in range(n)]
    df["description"] = [random.choice(descriptions) for _ in range(n)]

    return df
