import pandas as pd
import numpy as np

def generate_land_projects_and_births():
    np.random.seed(42)

    # 🔹 Arazi fiyatları
    df_land_prices = pd.DataFrame({
        'Year': [2024]*7,
        'Service_EN': ['Number of land plots according to the main use']*7,
        'Contract Category_EN': [
            'Residential use', 'Commercial use', 'Agricultural use',
            'Multi-use', 'Recreational use', 'Residential use', 'Agricultural use'
        ],
        'Region': [
            'Mbeya Region', 'Mbeya Region', 'Sanga-Lago Region',
            'Munggari and Surrounding Area', 'Furancungo Area',
            'Lake Chiwa Vicinity', 'North Luangwa National Park Vicinity'
        ],
        'Number of land plots': [3200, 500, 1500, 700, 150, 900, 400],
        'Average_Price_USD_per_m2': [18, 35, 10, 12, 25, 16, 14],
        'Currency': ['USD']*7
    })

    # 🔹 Doğum verileri (sentetik)
    np.random.seed(2025)
    regions = {
        'Mbeya Region': {'lat': -13.0, 'lon': 34.5, 'births': 1500},
        'Sanga-Lago Region': {'lat': -12.0, 'lon': 34.0, 'births': 1200},
        'Furancungo Area': {'lat': -11.5, 'lon': 34.8, 'births': 1000},
        'Munggari Surroundings': {'lat': -12.5, 'lon': 34.3, 'births': 800},
        'Lake Chiwa Vicinity': {'lat': -13.5, 'lon': 34.7, 'births': 600},
        'North Luangwa NP Vicinity': {'lat': -14.0, 'lon': 34.2, 'births': 400}
    }
    nationalities = ['Citizen', 'Expat']
    genders = ['Male', 'Female']
    age_groups = ['0-7 days', '8-28 days']
    records = []

    for region, info in regions.items():
        for nat in nationalities:
            births_nat = int(info['births'] * (0.85 if nat == 'Citizen' else 0.15))
            for gender in genders:
                for age in age_groups:
                    base = np.random.uniform(1.5, 5.0) if age == '0-7 days' else np.random.uniform(0.5, 2.0)
                    rate = base * (1.1 if gender == 'Male' else 1.0)
                    cases = int((rate / 100) * births_nat)
                    lat = np.random.normal(info['lat'], 0.3)
                    lon = np.random.normal(info['lon'], 0.3)
                    records.append({
                        'Year': 2011,
                        'Region_EN': region,
                        'Latitude': round(lat, 5),
                        'Longitude': round(lon, 5),
                        'Nationality_Group_En': nat,
                        'Gender_En': gender,
                        'Age_Group': age,
                        'Cases': cases,
                        'Rate (%)': round(rate, 2)
                    })
    df_births = pd.DataFrame(records)

    # 🔹 Bakanlık projeleri
    ministries = ['Education', 'Health', 'Infrastructure', 'Agriculture', 'Energy', 'Environment']
    projects = []
    for region in regions:
        for ministry in ministries:
            count = np.random.poisson(lam=5)
            cost = int(np.random.uniform(50000, 300000) * count)
            projects.append({'Year': 2015, 'Region': region, 'Ministry': ministry, 'Projects': count, 'Cost_MWK': cost})
    df_projects = pd.DataFrame(projects)

    # 🔹 Sağlık merkezleri
    years = list(range(2010, 2022))
    areas = ['Malawi', 'Lilongwe', 'Blantyre', 'Mzuzu', 'Zomba']
    data = []
    for year in years:
        for area in areas:
            beds = int(np.random.normal(1500, 300)) + 50 * (year - 2010)
            clinics = np.random.poisson(250) + 10*(year - 2010)
            data.append({'Year': year, 'Area': area, 'Beds': beds, 'Clinics': clinics})
    df_health = pd.DataFrame(data)

    return df_land_prices, df_births, df_projects, df_health
