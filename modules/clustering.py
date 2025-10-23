import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt

def perform_clustering(df, n_clusters=6, random_state=42):
    """KMeans + RandomForest ile feature önem sıralaması ve kümeleme."""
    # KMeans kümeleme
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    df["cluster"] = kmeans.fit_predict(df.select_dtypes(include=["float", "int"]))

    # Feature importance
    drop_cols = [c for c in ["cluster", "Unnamed: 0", "ea_id", "Unnamed: 0.1", "hid"] if c in df.columns]
    features = df.drop(columns=drop_cols, errors="ignore").columns

    rf = RandomForestClassifier(n_estimators=150, random_state=random_state)
    rf.fit(df[features], df["cluster"])

    importances = pd.DataFrame({
        "feature": features,
        "importance": rf.feature_importances_
    }).sort_values(by="importance", ascending=False)

    return df, importances

def plot_feature_importance(importance_df, save_path=None, top_n=20):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=importance_df.head(top_n),
        x="importance", y="feature",
        hue="feature", legend=False  # palette uyarısını keser
    )
    plt.title("Random Forest Feature Importance")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    plt.close()

