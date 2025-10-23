import pandas as pd
import numpy as np

from modules.clustering import perform_clustering, plot_feature_importance
from modules.poi_generator import generate_pois
from modules.flood_env_generator import generate_flood_features
from modules.region_agriculture import generate_region_agriculture
from modules.incidents_generator import generate_incidents
from modules.health_air_quality import generate_health_and_air_quality
from modules.social_behavior import generate_behavior
from modules.land_price_birth_project import generate_land_projects_and_births
from modules.population_density import (
    generate_area_green_agri_by_ea,
    compute_cluster_population_density
)
from modules.incidents_generator import generate_incidents
from modules.heatmap_generator import (
    generate_heatmaps,
    add_temporal_fields,
    generate_heatmaps_from_incidents,
    generate_heatmap_from_points
)



if __name__ == "__main__":
    print("🚀 Sentetik veri üretim pipeline başlatıldı...")

    # --- 1️⃣ Ana veri kümesi ---
    df = pd.read_csv(r"C:\sosyal_yardim\data\raw\df_final_merged_MWI.csv")

    # --- 2️⃣ Kümeleme ve feature importance ---
    df, importance_df = perform_clustering(df)
    plot_feature_importance(
        importance_df,
        save_path=r"C:\sosyal_yardim\data\output\feature_importance.png"
    )

    # --- 3️⃣ Coğrafi koordinatlar ---
    df["latitude"] = df["cluster"].apply(lambda x: -17 + (x + 1) * 1.2 + np.random.normal(0, 0.1))
    df["longitude"] = df["cluster"].apply(lambda x: 32 + (x + 1) * 0.6 + np.random.normal(0, 0.1))

    # --- 4️⃣ Sentetik alt veri kümeleri ---
    generate_pois(df).to_csv("data/output/sentetik_poi.csv", index=False)
    generate_flood_features(df["cluster"].unique()).to_csv("data/output/sentetik_flood_data.csv", index=False)
    generate_region_agriculture().to_csv("data/output/sentetik_agriculture.csv", index=False)
    generate_incidents().to_csv("data/output/sentetik_incidents.csv", index=False)

    h, a = generate_health_and_air_quality()
    h.to_csv("data/output/sentetik_health.csv", index=False)
    a.to_csv("data/output/sentetik_air.csv", index=False)

    generate_behavior(df).to_csv("data/output/sentetik_merged_data.csv", index=False)

    # --- 5️⃣ Yeni veri üretimi (arazi, doğum, projeler, sağlık) ---
    df_land, df_births, df_projects, df_health = generate_land_projects_and_births()
    df_land.to_csv("data/output/df_land_prices.csv", index=False)
    df_births.to_csv("data/output/child_death_synthetic.csv", index=False)
    df_projects.to_csv("data/output/df_projects.csv", index=False)
    df_health.to_csv("data/output/df_health_centers.csv", index=False)

    # --- 6️⃣ Isı haritaları ---
    df_with_time = add_temporal_fields(df)
    generate_heatmaps(df_with_time)

    # EA bazında alan/ratio verisi
    ea_area_df = generate_area_green_agri_by_ea(df)
    ea_area_df.to_csv("data/output/sentetik_bolge_verisi.csv", index=False)

    # Cluster bazında nüfus yoğunluğu (alan sözlüğü örneği)
    area_dict = {0: 50, 1: 30, 2: 40, 3: 20, 4: 25, 5: 35}
    pop_counts = compute_cluster_population_density(df, area_dict)
    pop_counts.to_csv("data/output/pop_counts.csv", index=False)

    # Incidents verisi + zaman alanları + ısı haritası
    inc = generate_incidents()
    inc_with_time = add_temporal_fields(inc)
    inc_with_time.to_csv("data/output/df_time_extended.csv", index=False)  # uzantı düzeltildi
    generate_heatmaps_from_incidents(inc_with_time)

    # Cluster noktalarından ayrı bir ısı haritası
    generate_heatmap_from_points(df[['latitude','longitude']], "data/output/heatmap_clusters.html")



    print("✅ Tüm sentetik veriler başarıyla oluşturuldu ve data/output klasörüne kaydedildi.")
    