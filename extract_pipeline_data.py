import requests
import pandas as pd

# List of keywords to match GLP-1 drugs
KEYWORDS = [
    "GLP-1", "Semaglutide", "Tirzepatide", "Liraglutide",
    "Dulaglutide", "Exenatide", "GIP", "dual agonist",
    "triple agonist", "retatrutide"
]

# ClinicalTrials.gov API URL
BASE_URL = "https://clinicaltrials.gov/api/v2/studies"

def search_trials(keyword):
    params = {
        "query.term": keyword,
        "pageSize": 200,
        "format": "json"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

records = []

for drug in KEYWORDS:
    print(f"🔍 Searching trials for: {drug}")
    data = search_trials(drug)

    if "studies" not in data:
        continue

    for study in data["studies"]:
        record = {
            "nct_id": study.get("protocolSection", {}).get("identificationModule", {}).get("nctId", ""),
            "study_title": study.get("protocolSection", {}).get("identificationModule", {}).get("briefTitle", ""),
            "phase": study.get("protocolSection", {}).get("designModule", {}).get("phases", ""),
            "status": study.get("protocolSection", {}).get("statusModule", {}).get("overallStatus", ""),
            "intervention_name": "",
            "intervention_type": "",
            "mechanism_class": drug,
            "sponsor": study.get("protocolSection", {}).get("sponsorCollaboratorsModule", {}).get("leadSponsor", {}).get("name", ""),
            "conditions": study.get("protocolSection", {}).get("conditionsModule", {}).get("conditions", ""),
            "start_date": study.get("protocolSection", {}).get("statusModule", {}).get("startDateStruct", {}).get("date", ""),
            "primary_completion_date": study.get("protocolSection", {}).get("statusModule", {}).get("primaryCompletionDateStruct", {}).get("date", ""),
            "locations": "",
            "source_link": f"https://clinicaltrials.gov/study/{study.get('protocolSection', {}).get('identificationModule', {}).get('nctId','')}",
            "notes": ""
        }

        # Extract intervention names
        interventions = study.get("protocolSection", {}).get("armsInterventionsModule", {}).get("interventions", [])
        if interventions:
            record["intervention_name"] = ", ".join([i.get("name", "") for i in interventions])
            record["intervention_type"] = ", ".join([i.get("type", "") for i in interventions])

        records.append(record)

# Save file
df = pd.DataFrame(records)
df.drop_duplicates(subset=["nct_id"], inplace=True)

output_path = r"D:\Project\glp1_ci_project_2020_2025\data\processed\pipeline_raw.csv"
df.to_csv(output_path, index=False)

print(f"\n✅ Pipeline extraction complete: {output_path}")
