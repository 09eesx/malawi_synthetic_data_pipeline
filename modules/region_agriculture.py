import pandas as pd
import numpy as np

def generate_region_agriculture(years=None, start_area=450_000, growth_rate=0.12):
    """Yıllara ve bölgelere göre ekili alan üretimi."""
    if years is None:
        years = list(range(2013, 2025))
    regions = ["North", "Central", "South"]

    # Her yıl için ekili alan büyümesi hesapla
    areas = [start_area * (1 + growth_rate)**i for i in range(len(years))]

    # Ülke toplam ekili alan DataFrame’i oluştur
    df_planted = pd.DataFrame({'Year': years, 'Planted_Area_m2': areas})

    # Bölgelere rastgele paylaştır
    sentetik = []
    for year in years:
        total = df_planted.loc[df_planted["Year"] == year, "Planted_Area_m2"].values[0]
        shares = np.random.dirichlet(np.ones(len(regions)))  # toplam = 1
        for region, share in zip(regions, shares):
            sentetik.append({
                "Year": year,
                "Region": region,
                "Planted_Area_m2": total * share
            })

    return pd.DataFrame(sentetik)
