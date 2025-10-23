import pandas as pd
import numpy as np

def generate_area_green_agri_by_ea(df: pd.DataFrame, seed: int = 123) -> pd.DataFrame:
    """
    EA (enumeration area) bazında sentetik toplam alan, tarım & yeşillik oranları üretir.
    Çıktı: sentetik_bolge_verisi.csv
    """
    rng = np.random.default_rng(seed)
    bölgeler = df['ea_id'].dropna().unique()
    n = len(bölgeler)

    area_km2 = rng.uniform(50, 150, size=n)
    total_area_m2 = area_km2 * 1_000_000
    tarim_ratio = rng.uniform(0.10, 0.50, size=n)
    yesillik_ratio = rng.uniform(0.05, 0.30, size=n)

    out = pd.DataFrame({
        'ea_id': bölgeler,
        'area_km2': area_km2,
        'total_area_m2': total_area_m2,
        'tarim_area_m2': total_area_m2 * tarim_ratio,
        'yesillik_area_m2': total_area_m2 * yesillik_ratio,
        'tarim_ratio': tarim_ratio,
        'yesillik_ratio': yesillik_ratio
    })
    return out

def compute_cluster_population_density(df: pd.DataFrame, area_km2_by_cluster: dict) -> pd.DataFrame:
    """
    Cluster başına nüfus sayımı ve verilen alan sözlüğüyle yoğunluk hesaplar.
    Çıktı: pop_counts.csv
    """
    pop_counts = df.groupby('cluster').size().reset_index(name='population')
    pop_counts['area_km2'] = pop_counts['cluster'].map(area_km2_by_cluster)
    pop_counts['pop_density'] = pop_counts['population'] / pop_counts['area_km2']
    return pop_counts
