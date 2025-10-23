import pandas as pd
import numpy as np

def generate_flood_features(clusters):
    """Sel riskiyle ilişkili çevresel özellikleri üretir."""
    data = []
    np.random.seed(42)
    for c in clusters:
        rainfall = np.random.normal(100, 30)
        gw_level = np.random.normal(0.8, 0.3)
        infra = np.random.uniform(0.3, 1.0)
        pop_density = np.random.randint(1000, 5000)
        flood_events = np.random.randint(0, 4)
        year = np.random.choice(range(2010, 2024))

        risk_score = rainfall * 0.4 - gw_level * 20 - infra * 30 + flood_events * 10
        flood = int(risk_score > 50)
        damage = int(flood and pop_density > 3000)

        data.append({
            'cluster': c,
            'avg_rainfall_mm': rainfall,
            'ground_water_level_m': gw_level,
            'infrastructure_density': infra,
            'population_density': pop_density,
            'historical_flood_events': flood_events,
            'year': year,
            'flood_occurred': flood,
            'damage_occurred': damage
        })
    return pd.DataFrame(data)
