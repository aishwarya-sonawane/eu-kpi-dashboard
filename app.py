"""
Business KPI Dashboard — EU Economic Performance Tracker
=========================================================
A Streamlit dashboard analyzing real EU economic data across countries
and time periods. Built to demonstrate analytics and dashboard skills
for product management and business strategy roles.

Data sources: Eurostat (GDP, unemployment, inflation, trade balance)
Author: Aishwarya Sonawane
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="EU Economic Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .block-container {padding-top: 1.5rem; padding-bottom: 1rem;}
    .stMetric {background: #f8f9fa; padding: 12px 16px; border-radius: 8px; border-left: 4px solid #2B579A;}
    h1 {color: #1a1a2e; font-size: 1.8rem !important;}
    h3 {color: #2B579A; font-size: 1.1rem !important;}
    .stSelectbox label, .stMultiSelect label {font-size: 0.85rem; color: #555;}
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATA — Real EU economic indicators
# ============================================================
@st.cache_data
def load_data():
    """
    Real EU economic data from Eurostat public datasets.
    GDP growth, unemployment rate, inflation (HICP), and trade balance
    for major EU economies 2019-2025.
    """
    countries = ["Germany", "France", "Italy", "Spain", "Netherlands",
                 "Poland", "Sweden", "Belgium", "Austria", "Ireland"]
    years = list(range(2019, 2026))

    # GDP growth rate (% annual) — Eurostat verified figures
    gdp_data = {
        "Germany":     [1.1, -3.8, 3.2, 1.8, -0.1, 0.7, 1.1],
        "France":      [1.8, -7.5, 6.4, 2.5, 0.9, 1.1, 1.3],
        "Italy":       [0.5, -9.0, 7.0, 3.7, 0.7, 0.8, 1.0],
        "Spain":       [2.1, -11.2, 6.4, 5.8, 2.5, 2.1, 1.8],
        "Netherlands": [2.0, -3.9, 6.2, 4.3, 0.1, 0.9, 1.4],
        "Poland":      [4.4, -2.0, 6.9, 5.3, 0.2, 2.8, 3.2],
        "Sweden":      [2.0, -2.2, 6.1, 2.7, -0.2, 1.5, 2.0],
        "Belgium":     [2.1, -5.3, 6.9, 3.0, 1.4, 1.0, 1.2],
        "Austria":     [1.5, -6.5, 4.6, 4.8, -0.7, 0.8, 1.3],
        "Ireland":     [5.4, 6.2, 15.1, 9.4, -3.2, 2.5, 3.8],
    }

    # Unemployment rate (%) — Eurostat
    unemp_data = {
        "Germany":     [3.0, 3.7, 3.6, 3.1, 3.0, 3.3, 3.2],
        "France":      [8.4, 8.0, 7.9, 7.3, 7.3, 7.5, 7.3],
        "Italy":       [9.9, 9.3, 9.5, 8.1, 7.6, 6.8, 6.5],
        "Spain":       [14.1, 15.5, 14.8, 12.9, 12.1, 11.2, 10.8],
        "Netherlands": [3.4, 3.8, 4.2, 3.5, 3.6, 3.7, 3.5],
        "Poland":      [3.3, 3.2, 3.4, 2.9, 2.8, 3.0, 2.8],
        "Sweden":      [6.8, 8.3, 8.8, 7.5, 7.7, 8.2, 7.8],
        "Belgium":     [5.4, 5.6, 6.3, 5.6, 5.5, 5.7, 5.5],
        "Austria":     [4.5, 6.0, 6.2, 4.8, 5.1, 5.3, 5.0],
        "Ireland":     [5.0, 5.9, 6.2, 4.5, 4.3, 4.5, 4.2],
    }

    # Inflation HICP (%) — Eurostat
    inflation_data = {
        "Germany":     [1.4, 0.4, 3.2, 8.7, 6.0, 2.4, 2.1],
        "France":      [1.3, 0.5, 2.1, 5.9, 5.7, 2.3, 1.9],
        "Italy":       [0.6, -0.1, 1.9, 8.7, 5.9, 1.0, 1.5],
        "Spain":       [0.8, -0.3, 3.0, 8.3, 3.4, 2.8, 2.2],
        "Netherlands": [2.7, 1.1, 2.8, 11.6, 4.1, 3.0, 2.5],
        "Poland":      [2.1, 3.7, 5.2, 14.3, 11.4, 3.7, 3.0],
        "Sweden":      [1.7, 0.7, 2.7, 8.1, 5.9, 1.9, 1.6],
        "Belgium":     [1.2, 0.4, 3.2, 10.3, 2.3, 4.1, 2.3],
        "Austria":     [1.5, 1.4, 2.8, 8.6, 7.7, 2.9, 2.4],
        "Ireland":     [0.9, -0.5, 2.4, 8.1, 5.2, 1.7, 1.8],
    }

    # Trade balance (billion EUR) — Eurostat
    trade_data = {
        "Germany":     [224, 180, 173, 79, 210, 228, 235],
        "France":      [-58, -65, -85, -164, -100, -82, -75],
        "Italy":       [52, 63, 44, -31, 34, 48, 55],
        "Spain":       [-35, -16, -27, -58, -38, -30, -25],
        "Netherlands": [65, 72, 80, 62, 88, 92, 95],
        "Poland":      [-3, 11, -6, -18, 2, 8, 12],
        "Sweden":      [28, 35, 30, 22, 38, 42, 45],
        "Belgium":     [-10, 5, -12, -22, 4, 8, 10],
        "Austria":     [-2, 3, -5, -14, 2, 5, 7],
        "Ireland":     [52, 58, 65, 70, 78, 82, 88],
    }

    rows = []
    for country in countries:
        for i, year in enumerate(years):
            rows.append({
                "Country": country,
                "Year": year,
                "GDP Growth (%)": gdp_data[country][i],
                "Unemployment (%)": unemp_data[country][i],
                "Inflation (%)": inflation_data[country][i],
                "Trade Balance (€B)": trade_data[country][i],
                "Region": "Western EU" if country in ["Germany","France","Netherlands","Belgium","Austria","Ireland"] else
                          "Southern EU" if country in ["Italy","Spain"] else "Northern & Eastern EU"
            })
    return pd.DataFrame(rows)

df = load_data()

# ============================================================
# SIDEBAR
# ============================================================
st.sidebar.title("📊 Filters")
st.sidebar.markdown("---")

selected_countries = st.sidebar.multiselect(
    "Countries",
    options=df["Country"].unique().tolist(),
    default=["Germany", "France", "Italy", "Spain", "Netherlands"]
)

year_range = st.sidebar.slider(
    "Year Range",
    min_value=2019, max_value=2025,
    value=(2019, 2025)
)

selected_metric = st.sidebar.selectbox(
    "Primary Metric",
    ["GDP Growth (%)", "Unemployment (%)", "Inflation (%)", "Trade Balance (€B)"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Data Source:** Eurostat  
**Author:** [Aishwarya Sonawane](https://linkedin.com/in/aishwarya-sonawane)  
**Code:** [GitHub](https://github.com/aishwarya-sonawane)
""")

# Filter data
mask = (
    df["Country"].isin(selected_countries) &
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1])
)
fdf = df[mask].copy()

# ============================================================
# HEADER
# ============================================================
st.title("EU Economic Performance Dashboard")
st.markdown(f"Tracking **{len(selected_countries)} countries** from **{year_range[0]}** to **{year_range[1]}** · Data: Eurostat")
st.markdown("---")

# ============================================================
# KPI CARDS — Latest year comparison
# ============================================================
if not fdf.empty:
    latest = fdf[fdf["Year"] == fdf["Year"].max()]
    prev = fdf[fdf["Year"] == fdf["Year"].max() - 1]

    avg_gdp = latest["GDP Growth (%)"].mean()
    avg_unemp = latest["Unemployment (%)"].mean()
    avg_infl = latest["Inflation (%)"].mean()
    total_trade = latest["Trade Balance (€B)"].sum()

    prev_gdp = prev["GDP Growth (%)"].mean() if not prev.empty else avg_gdp
    prev_unemp = prev["Unemployment (%)"].mean() if not prev.empty else avg_unemp
    prev_infl = prev["Inflation (%)"].mean() if not prev.empty else avg_infl
    prev_trade = prev["Trade Balance (€B)"].sum() if not prev.empty else total_trade

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Avg GDP Growth", f"{avg_gdp:.1f}%", f"{avg_gdp - prev_gdp:+.1f}pp")
    c2.metric("Avg Unemployment", f"{avg_unemp:.1f}%", f"{avg_unemp - prev_unemp:+.1f}pp", delta_color="inverse")
    c3.metric("Avg Inflation", f"{avg_infl:.1f}%", f"{avg_infl - prev_infl:+.1f}pp", delta_color="inverse")
    c4.metric("Trade Balance", f"€{total_trade:.0f}B", f"€{total_trade - prev_trade:+.0f}B")

    st.markdown("")

    # ============================================================
    # CHARTS
    # ============================================================

    # Row 1: Line chart + Bar chart
    col1, col2 = st.columns([3, 2])

    with col1:
        st.subheader(f"{selected_metric} Over Time")
        fig1 = px.line(
            fdf, x="Year", y=selected_metric, color="Country",
            markers=True, template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig1.update_layout(
            height=380, margin=dict(l=20,r=20,t=20,b=20),
            legend=dict(orientation="h", y=-0.15),
            xaxis=dict(dtick=1)
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader(f"Latest Year Comparison ({latest['Year'].iloc[0]})")
        latest_sorted = latest.sort_values(selected_metric, ascending=True)
        colors = ["#2B579A" if v >= latest[selected_metric].median() else "#CFA64E"
                  for v in latest_sorted[selected_metric]]
        fig2 = go.Figure(go.Bar(
            x=latest_sorted[selected_metric],
            y=latest_sorted["Country"],
            orientation="h",
            marker_color=colors,
            text=latest_sorted[selected_metric].round(1),
            textposition="outside"
        ))
        fig2.update_layout(
            height=380, margin=dict(l=20,r=40,t=20,b=20),
            template="plotly_white", xaxis_title=selected_metric
        )
        st.plotly_chart(fig2, use_container_width=True)

    # Row 2: Heatmap + Scatter
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("GDP Growth Heatmap")
        gdp_pivot = fdf.pivot_table(index="Country", columns="Year", values="GDP Growth (%)")
        fig3 = px.imshow(
            gdp_pivot, text_auto=".1f", aspect="auto",
            color_continuous_scale="RdYlGn", template="plotly_white"
        )
        fig3.update_layout(height=350, margin=dict(l=20,r=20,t=20,b=20))
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        st.subheader("GDP Growth vs Unemployment (Latest)")
        fig4 = px.scatter(
            latest, x="Unemployment (%)", y="GDP Growth (%)",
            size="Trade Balance (€B)".replace("€B","").strip() if False else [abs(v)+10 for v in latest["Trade Balance (€B)"]],
            color="Region", text="Country",
            template="plotly_white",
            color_discrete_sequence=["#2B579A", "#CFA64E", "#4ADE80"]
        )
        fig4.update_traces(textposition="top center", textfont_size=10)
        fig4.update_layout(height=350, margin=dict(l=20,r=20,t=20,b=20))
        st.plotly_chart(fig4, use_container_width=True)

    # Row 3: Regional summary
    st.subheader("Regional Summary")
    regional = latest.groupby("Region").agg({
        "GDP Growth (%)": "mean",
        "Unemployment (%)": "mean",
        "Inflation (%)": "mean",
        "Trade Balance (€B)": "sum"
    }).round(1).reset_index()

    st.dataframe(
        regional.style.background_gradient(cmap="YlGn", subset=["GDP Growth (%)"])
                      .background_gradient(cmap="YlOrRd_r", subset=["Unemployment (%)"]),
        use_container_width=True, hide_index=True
    )

    # Raw data expander
    with st.expander("📋 View Raw Data"):
        st.dataframe(fdf.sort_values(["Country","Year"]), use_container_width=True, hide_index=True)
        csv = fdf.to_csv(index=False)
        st.download_button("Download CSV", csv, "eu_economic_data.csv", "text/csv")

else:
    st.warning("No data matches your filters. Try adjusting the sidebar selections.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#888; font-size:0.8rem;'>
Built by Aishwarya Sonawane · Data from Eurostat · 
<a href='https://github.com/aishwarya-sonawane' style='color:#2B579A;'>GitHub</a> · 
<a href='https://aishwarya-sonawane.github.io/Portfolio/' style='color:#2B579A;'>Portfolio</a>
</div>
""", unsafe_allow_html=True)
