📘 GLP-1 Market Landscape & Competitive Intelligence (2020–2025)

Ozempic · Wegovy · Rybelsus · Mounjaro · Zepbound · Dual & Triple Agonists Pipeline

This repository contains a full end-to-end Competitive Intelligence (CI) project built using real-world pharmaceutical data, clinical trial pipelines, market share analysis, and forecasting models focused on the rapidly expanding GLP-1 metabolic drug class.

The project captures the competitive dynamics between Novo Nordisk and Eli Lilly, including product sales (2020–2024), clinical development activity, and 2025–2030 future forecasting.

🏗️ Project Structure
glp1_ci_project_2020_2025/
│
├── data/
│   ├── raw/                    # PDFs of annual reports (ignored in Git)
│   └── processed/
│       ├── sales_summary.csv
│       ├── glp1_sales_clean.csv
│       ├── pipeline_raw.csv
│       └── pipeline_clean.csv
│
├── notebooks/
│   ├── 01_sales_data_preparation.ipynb
│   ├── 02_pipeline_data_preparation.ipynb
│   ├── 03_market_analysis.ipynb
│   ├── 04_competitive_landscape.ipynb
│   └── 05_forecasting_model.ipynb
│
├── scripts/
│   ├── extract_sales_data.py          # Automated PDF → table extraction
│   └── extract_pipeline_data.py       # ClinicalTrials.gov API scraper
│
├── reports/
│   └── figures/
│       ├── market_share_novo_vs_lilly_2020_2024.png
│       ├── ozempic_vs_mounjaro_trend_2020_2024.png
│       ├── ozempic_actual_vs_forecast_2020_2030.png
│       └── more visualizations...
│
├── .gitignore
└── README.md

📊 Key Deliverables
1. Sales Analysis (2020–2024)

Includes revenue trends for:

Novo Nordisk: Ozempic, Rybelsus, Wegovy

Eli Lilly: Mounjaro, Zepbound

Outputs:

Year-over-year growth

Novo vs Lilly GLP-1 market share

Product-level revenue trendlines

Publication-quality figures

2. Pipeline Analysis (GLP-1 / GIP / Dual / Triple Agonists)

Using ClinicalTrials.gov API, the project extracts and processes trials for:

Semaglutide

Tirzepatide

Retatrutide

Dual agonists

Triple agonists

Other next-gen metabolic drugs

Outputs:

Phase distribution (Phase 1 / 2 / 3 / 4)

Mechanism-of-action landscape

Sponsor leaderboard

Heatmaps & bar charts

3. Competitive Intelligence Insights

Includes real-world CI narrative:

Lilly’s acceleration vs Novo’s mature GLP-1 franchise

Obesity market expansion (Wegovy vs Zepbound)

Future dual-agonist and triple-agonist competition

Clinical risk signals

Market entry timing

4. Forecasting Model (2025–2030)

Forecasting includes:

Ozempic growth projection (CAGR model)

Long-term GLP-1 market outlook

Scenario models: Base / Optimistic / Conservative

Combined future share (Novo vs Lilly)

🔧 Technologies Used

Python

Pandas

Matplotlib / Seaborn

PDFPlumber

Requests (API calls)

Jupyter Notebook

Git/GitHub

🚀 How To Use

Clone the repository:

git clone https://github.com/pintuvarma445-PDV/glp1-competitive-intelligence-2020-2025.git


Install dependencies:

pip install -r requirements.txt


Run notebooks from the notebooks/ folder.

📩 Future Additions (Planned)

Scenario-based forecasting

Pricing pressure models

Competitor SWOT summaries

Obesity vs diabetes segmentation forecast

CI presentation (PowerPoint-ready deck)

👤 Author

Pintu Varma
Medicinal Chemistry + Data Science + Competitive Intelligence
LinkedIn: https://www.linkedin.com/in/pintu-varma-314750175
