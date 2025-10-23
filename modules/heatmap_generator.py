import folium
from folium.plugins import HeatMap
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_heatmaps(df, output_folder="data/output/"):
    """Folium tabanlı basit ve ağırlıklı ısı haritalarını kaydeder."""
    m1 = folium.Map(location=[-13, 34], zoom_start=6)
    heat_data_simple = df[['latitude', 'longitude']].values.tolist()
    HeatMap(heat_data_simple).add_to(m1)
    m1.save(f"{output_folder}/heatmap_simple.html")

    if 'value' in df.columns:
        m2 = folium.Map(location=[-13, 34], zoom_start=6)
        heat_data_weighted = df[['latitude', 'longitude', 'value']].values.tolist()
        HeatMap(heat_data_weighted, radius=15, max_zoom=13).add_to(m2)
        m2.save(f"{output_folder}/heatmap_weighted.html")

def add_temporal_fields(df):
    """Sentetik olay verisine rastgele zaman ve açıklama ekler."""
    start_time = datetime(2019, 6, 1)
    end_time = datetime(2019, 6, 30)
    descriptions = [
        "Road accident", "Vehicle collision", "Pedestrian hit", "Single vehicle crash",
        "Multiple vehicle accident", "Hit and run", "Roadside emergency", "Traffic jam due to accident"
    ]
    delta = (end_time - start_time).total_seconds()

    df = df.copy()
    df["datetime"] = [start_time + timedelta(seconds=random.randint(0, int(delta))) for _ in range(len(df))]
    df["description"] = [random.choice(descriptions) for _ in range(len(df))]
    return df

import folium
from folium.plugins import HeatMap

def generate_heatmaps_from_incidents(df, output_folder="data/output/"):
    """
    Kolonlar: latitude, longitude[, value]
    """
    m1 = folium.Map(location=[-13, 34], zoom_start=6)
    HeatMap(df[['latitude', 'longitude']].values.tolist()).add_to(m1)
    m1.save(f"{output_folder}/heatmap_simple.html")

    if 'value' in df.columns:
        m2 = folium.Map(location=[-13, 34], zoom_start=6)
        HeatMap(df[['latitude', 'longitude', 'value']].values.tolist(),
                radius=15, max_zoom=13).add_to(m2)
        m2.save(f"{output_folder}/heatmap_weighted.html")

def generate_heatmap_from_points(points_df, output_path="data/output/heatmap_clusters.html"):
    """
    Cluster/household noktaları için basic ısı haritası.
    Beklenen kolonlar: latitude, longitude
    """
    m = folium.Map(location=[-13, 34], zoom_start=6)
    HeatMap(points_df[['latitude','longitude']].values.tolist()).add_to(m)
    m.save(output_path)
