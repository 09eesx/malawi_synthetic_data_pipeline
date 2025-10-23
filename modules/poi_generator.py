import pandas as pd
import numpy as np

def generate_pois(df, poi_types=None):
    """Kümelere göre POI (okul, sağlık, gıda) üret."""
    if poi_types is None:
        poi_types = ["okul", "saglik", "gida"]

    pois = []
    for cluster_id in df["cluster"].unique():
        center = df[df["cluster"] == cluster_id][["latitude", "longitude"]].mean()
        for poi_type in poi_types:
            pois.append({
                "cluster_id": cluster_id,
                "poi_type": poi_type,
                "latitude": center["latitude"] + np.random.uniform(-0.01, 0.01),
                "longitude": center["longitude"] + np.random.uniform(-0.01, 0.01)
            })
    return pd.DataFrame(pois)
