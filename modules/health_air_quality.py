import pandas as pd
import numpy as np

def generate_health_and_air_quality():
    """Sağlık tesisleri ve hava kalitesi verileri üretir."""
    np.random.seed(42)

    # Sağlık merkezleri
    years = list(range(2010, 2022))
    areas = ['Malawi', 'Lilongwe', 'Blantyre', 'Mzuzu', 'Zomba', 'Karonga']
    measures = ['Hospitals', 'Beds', 'Clinics and Health Centres']
    data = []

    for year in years:
        for area in areas:
            for measure in measures:
                if measure == 'Hospitals':
                    gov = np.random.poisson(10) + (year - 2010)
                    priv = np.random.poisson(5) + (year - 2010)//2
                elif measure == 'Beds':
                    gov = int(np.random.normal(1500, 300)) + 50*(year - 2010)
                    priv = int(np.random.normal(500, 150)) + 25*(year - 2010)
                    gov, priv = max(gov, 200), max(priv, 50)
                else:
                    gov = np.random.poisson(250) + 10*(year - 2010)
                    priv = np.random.poisson(100) + 5*(year - 2010)
                total = gov + priv
                data.extend([
                    {'Year': year, 'Area': area, 'Measure': measure, 'Sector': 'Government', 'Value': gov},
                    {'Year': year, 'Area': area, 'Measure': measure, 'Sector': 'Private', 'Value': priv},
                    {'Year': year, 'Area': area, 'Measure': measure, 'Sector': 'Total', 'Value': total},
                ])
    health_df = pd.DataFrame(data)

    # Hava kalitesi
    regions_stations = {
        "Lilongwe": ["Area 1", "City Center"],
        "Blantyre": ["Main Market", "Ndirande"],
        "Mzuzu": ["Central", "Ekwendeni"]
    }
    pollutants = {
        "SO2": (3.0, 8.0),
        "NO2": (8.0, 15.0),
        "O3": (30.0, 55.0),
        "PM10": (40.0, 90.0)
    }
    air_data = []
    for region, stations in regions_stations.items():
        for station in stations:
            lat, lon = np.random.uniform(-16.7, -9.0), np.random.uniform(31.7, 35.6)
            for pol, (low, high) in pollutants.items():
                val = np.nan if (pol == "O3" and np.random.rand() < 0.1) else np.round(np.random.uniform(low, high), 1)
                air_data.append({
                    "Year": 2016, "Region": region, "Station": station,
                    "Pollutant": pol, "Units": "µg/m³",
                    "Value": val, "Latitude": lat, "Longitude": lon
                })
    air_df = pd.DataFrame(air_data)

    return health_df, air_df
