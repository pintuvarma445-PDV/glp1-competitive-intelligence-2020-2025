import pandas as pd

# Load extracted raw CSV
RAW_FILE = r"D:\Project\glp1_ci_project_2020_2025\data\processed\glp1_sales_extracted.csv"
OUTPUT_CLEAN = r"D:\Project\glp1_ci_project_2020_2025\data\processed\glp1_sales_clean.csv"
OUTPUT_VERIFY = r"D:\Project\glp1_ci_project_2020_2025\data\processed\glp1_sales_verification_table.csv"

df = pd.read_csv(RAW_FILE)

# --------------------------------------------
# PRODUCT LAUNCH YEAR CONSTRAINTS
# --------------------------------------------
launch_year = {
    "Ozempic": 2018,
    "Rybelsus": 2019,
    "Wegovy": 2021,
    "Mounjaro": 2022,
    "Zepbound": 2023
}

# Remove values before product launch
df = df[df.apply(lambda row: int(row["year"]) >= launch_year[row["product"]], axis=1)]

# --------------------------------------------
# VALUE RANGE FILTERING (remove junk)
# --------------------------------------------
df = df[(df["value_dkk_or_usd_mn"] >= 1000) & (df["value_dkk_or_usd_mn"] <= 300000)]

# --------------------------------------------
# Remove obvious GLP-1 category totals
# (if value repeated for 3+ products on same page)
# --------------------------------------------
df["duplicate_page_flag"] = df.groupby(["year", "page"])["value_dkk_or_usd_mn"].transform("count")
df = df[df["duplicate_page_flag"] < 3]  # removes lines like 250,316 appearing for all products

# --------------------------------------------
# Keep only highest value per product per year
# --------------------------------------------
df_clean = df.sort_values("value_dkk_or_usd_mn", ascending=False).groupby(
    ["product", "year"], as_index=False
).first()

# --------------------------------------------
# Create a verification table (shortlist)
# --------------------------------------------
df_verify = df.sort_values(["product", "year", "value_dkk_or_usd_mn"], ascending=False)

# --------------------------------------------
# Save outputs
# --------------------------------------------
df_clean.to_csv(OUTPUT_CLEAN, index=False)
df_verify.to_csv(OUTPUT_VERIFY, index=False)

print("✅ Cleaning complete!")
print(f"Clean file saved → {OUTPUT_CLEAN}")
print(f"Verification table saved → {OUTPUT_VERIFY}")
