import plotly.express as px
import pandas as pd
from pathlib import Path
import json

# =========================================================
# Base Directory Setup (Professional Method)
# =========================================================
BASE_DIR = Path(__file__).resolve().parent
DATA_FOLDER = BASE_DIR / "data"


# =========================================================
# Utility: Load CSV Safely
# =========================================================
def load_data(filename: str, required_columns: set = None) -> pd.DataFrame:
    """
    Loads a CSV file safely and validates required columns.
    """

    file_path = DATA_FOLDER / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"❌ File not found: {file_path}\n"
            f"Make sure the file exists inside the 'data' folder."
        )

    df = pd.read_csv(file_path)

    if required_columns:
        missing = required_columns - set(df.columns)
        if missing:
            raise ValueError(
                f"❌ Missing columns in {filename}: {missing}"
            )

    return df


# =========================================================
# Revenue Chart (State Performance)
# =========================================================
def revenue_chart():

    df = load_data(
        "CLEAN_State_Performance.csv",
        required_columns={"state", "revenue"}
    )

    # Sort by revenue descending
    df = df.sort_values("revenue", ascending=False)

    fig = px.bar(
        df,
        x="state",
        y="revenue",
        color="revenue",
        text="revenue",
        color_continuous_scale="Blues",
        title="State Revenue Performance"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="State",
        yaxis_title="Revenue",
        showlegend=False
    )

    fig.update_traces(textposition="outside")

    return json.loads(fig.to_json())


# =========================================================
# Seasonal Chart (Tourism Trends)
# =========================================================
def seasonal_chart():

    df = load_data(
        "CLEAN_Seasonal_Trends.csv",   # ✔ fixed filename
        required_columns={"month", "hotel_occupancy_pct", "region"}
    )

    fig = px.line(
        df,
        x="month",
        y="hotel_occupancy_pct",
        color="region",
        markers=True,
        title="Seasonal Visitor Trends"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Month",
        yaxis_title="Hotel Occupancy (%)"
    )
    return json.loads(fig.to_json())


# =========================================================
# KPI Metrics (Optional Upgrade)
# =========================================================
def get_kpis():
    """
    Returns KPI metrics for dashboard cards.
    """

    df = load_data(
        "CLEAN_State_Performance.csv",
        required_columns={"revenue"}
    )

    total_revenue = df["revenue"].sum()
    avg_revenue = df["revenue"].mean()

    return {
        "total_revenue": round(total_revenue, 2),
        "avg_revenue": round(avg_revenue, 2),
    }
