import os
import pdfplumber
import pandas as pd
import re

# ----------------------------------------------------
# CONFIG
# ----------------------------------------------------
BASE_PATH = r"D:\Project\glp1_ci_project_2020_2025\data\raw"
OUTPUT_PATH = r"D:\Project\glp1_ci_project_2020_2025\data\processed\glp1_sales_extracted.csv"

PRODUCT_KEYWORDS = {
    "Ozempic": ["ozempic"],
    "Rybelsus": ["rybelsus"],
    "Wegovy": ["wegovy"],
    "Mounjaro": ["mounjaro"],
    "Zepbound": ["zepbound"]
}

NUMBER_REGEX = r"([0-9]{1,3}(?:[,\.][0-9]{3})+)"  # matches numbers like 34,205 or 120.450

records = []

# ----------------------------------------------------
# CLEAN NUMBER
# ----------------------------------------------------
def clean_number(num_str):
    return int(num_str.replace(",", "").replace(".", ""))

# ----------------------------------------------------
# EXTRACT FROM SINGLE PDF
# ----------------------------------------------------
def extract_from_pdf(pdf_path, company, year):
    print(f"\n📄 Reading: {pdf_path}")

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()
                if not text:
                    continue

                lines = text.split("\n")

                for product, keywords in PRODUCT_KEYWORDS.items():
                    for line in lines:
                        if any(k in line.lower() for k in keywords):
                            num_match = re.search(NUMBER_REGEX, line)
                            if num_match:
                                value = clean_number(num_match.group())

                                print(f"➡ Found {product} ({year}) = {value} on page {page_number}")

                                records.append({
                                    "company": company,
                                    "product": product,
                                    "year": year,
                                    "value_dkk_or_usd_mn": value,
                                    "page": page_number,
                                    "source_file": os.path.basename(pdf_path),
                                    "raw_line": line.strip()
                                })

    except Exception as e:
        print(f"❌ ERROR reading {pdf_path}: {e}")


# ----------------------------------------------------
# WALK THROUGH ALL PDF FOLDERS
# ----------------------------------------------------
def scan_pdfs():
    # Novo Nordisk
    novo_path = os.path.join(BASE_PATH, "novo_nordisk")
    for year in os.listdir(novo_path):
        year_folder = os.path.join(novo_path, year)
        if os.path.isdir(year_folder):
            for file in os.listdir(year_folder):
                if file.endswith(".pdf"):
                    extract_from_pdf(
                        pdf_path=os.path.join(year_folder, file),
                        company="Novo Nordisk",
                        year=year
                    )

    # Eli Lilly
    lilly_path = os.path.join(BASE_PATH, "eli_lilly")
    for year in os.listdir(lilly_path):
        year_folder = os.path.join(lilly_path, year)
        if os.path.isdir(year_folder):
            for file in os.listdir(year_folder):
                if file.endswith(".pdf"):
                    extract_from_pdf(
                        pdf_path=os.path.join(year_folder, file),
                        company="Eli Lilly",
                        year=year
                    )


# ----------------------------------------------------
# MAIN
# ----------------------------------------------------
if __name__ == "__main__":
    print("🚀 Starting GLP-1 Sales Extraction Automation...\n")

    scan_pdfs()

    df = pd.DataFrame(records)

    df.to_csv(OUTPUT_PATH, index=False)

    print(f"\n✅ Extraction complete!")
    print(f"📁 Results saved to: {OUTPUT_PATH}")
