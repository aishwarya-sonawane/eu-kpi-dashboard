# 📊 EU Economic Performance Dashboard

An interactive dashboard tracking key economic indicators across 10 EU countries from 2019–2025. Built with Python, Streamlit, and Plotly.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red)
![License](https://img.shields.io/badge/License-MIT-green)

## What It Does

Tracks 4 key economic indicators across major EU economies:

- **GDP Growth** — annual % change with heatmap visualization
- **Unemployment Rate** — trend analysis and cross-country comparison
- **Inflation (HICP)** — consumer price tracking post-pandemic
- **Trade Balance** — export/import dynamics in €B

Interactive filters let you select countries, time ranges, and switch between metrics. The dashboard updates all charts in real-time.

## Views

- **KPI cards + line chart:** filter by country, year range and metric; cards show year-over-year change.
- **Heatmap + scatter:** the GDP heatmap shows post-COVID recovery patterns; the scatter plots GDP growth against unemployment.

## Why I Built This

I work on delivery dashboards and analytics reports in my day job (at smart Europe and previously at SKF India). This project demonstrates the same skills — data wrangling, KPI design, visual storytelling — using publicly available EU economic data instead of proprietary company data.

The dashboard answers questions like:
- Which EU economies recovered fastest after COVID?
- How does Germany's GDP growth compare to Southern EU?
- Is there a correlation between unemployment and trade balance?

## Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Data processing and app logic |
| **Streamlit** | Web app framework |
| **Plotly** | Interactive charts (line, bar, heatmap, scatter) |
| **Pandas** | Data manipulation and aggregation |

## Data Source

All data is from **Eurostat**, the statistical office of the European Union. Indicators used:
- `nama_10_gdp` — GDP and main components
- `une_rt_m` — Unemployment rate
- `prc_hicp_aind` — HICP inflation
- `bop_gdp6_q` — Balance of payments

## Run Locally

```bash
git clone https://github.com/aishwarya-sonawane/eu-kpi-dashboard.git
cd eu-kpi-dashboard
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Cloud (Free)

1. Push this repo to your GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub and select this repo
4. Set `app.py` as the main file
5. Click Deploy — you'll get a public URL in ~2 minutes

## Project Structure

```
eu-kpi-dashboard/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Author

**Aishwarya Sonawane** — M.Eng. student, Technology & Innovation Management  
[Portfolio](https://aishwarya-sonawane.vercel.app) · [LinkedIn](https://www.linkedin.com/in/aishwarya-s18) · [GitHub](https://github.com/aishwarya-sonawane)

## License

MIT — use it however you want.
