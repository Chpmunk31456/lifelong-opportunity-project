from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Remove the duplicated Guide 18 English package mistakenly stored under worksheets.
for rel in [
    "18-legal-administrative-assistant-and-legal-office-coordinator/worksheets/english/docx/Lifelong_Opportunity_Legal_Administrative_Assistant_and_Legal_Office_Coordinator_Guide_English_v1.0.docx",
    "18-legal-administrative-assistant-and-legal-office-coordinator/worksheets/english/pdf/Lifelong_Opportunity_Legal_Administrative_Assistant_and_Legal_Office_Coordinator_Guide_English_v1.0.pdf",
]:
    path = ROOT / rel
    if path.exists():
        path.unlink()

renames = {
    "29-hvac-technician-and-refrigeration-mechanic/english/docx/Lifelong_Opportunity_HVAC_Guide_English_v1.0.docx":
        "29-hvac-technician-and-refrigeration-mechanic/english/docx/Lifelong_Opportunity_HVAC_Technician_and_Refrigeration_Mechanic_Guide_English_v1.0.docx",
    "29-hvac-technician-and-refrigeration-mechanic/english/pdf/Lifelong_Opportunity_HVAC_Guide_English_v1.0.pdf":
        "29-hvac-technician-and-refrigeration-mechanic/english/pdf/Lifelong_Opportunity_HVAC_Technician_and_Refrigeration_Mechanic_Guide_English_v1.0.pdf",
    "30-electrician-and-electrical-technician/english/docx/Lifelong_Opportunity_Electrician_Guide_English_v1.0.docx":
        "30-electrician-and-electrical-technician/english/docx/Lifelong_Opportunity_Electrician_and_Electrical_Technician_Guide_English_v1.0.docx",
    "30-electrician-and-electrical-technician/english/pdf/Lifelong_Opportunity_Electrician_Guide_English_v1.0.pdf":
        "30-electrician-and-electrical-technician/english/pdf/Lifelong_Opportunity_Electrician_and_Electrical_Technician_Guide_English_v1.0.pdf",
    "54-occupational-therapy-assistant/english/docx/Physical Therapist Assistant.docx":
        "54-occupational-therapy-assistant/english/docx/Lifelong_Opportunity_Occupational_Therapy_Assistant_Guide_English_v1.0.docx",
    "54-occupational-therapy-assistant/english/pdf/Physical Therapist Assistant.pdf":
        "54-occupational-therapy-assistant/english/pdf/Lifelong_Opportunity_Occupational_Therapy_Assistant_Guide_English_v1.0.pdf",
}

for old_rel, new_rel in renames.items():
    old = ROOT / old_rel
    new = ROOT / new_rel
    if old.exists():
        new.parent.mkdir(parents=True, exist_ok=True)
        old.rename(new)

replacements = {
    "29-hvac-technician-and-refrigeration-mechanic/README.md": {
        "Lifelong_Opportunity_HVAC_Guide_English_v1.0.docx": "Lifelong_Opportunity_HVAC_Technician_and_Refrigeration_Mechanic_Guide_English_v1.0.docx",
        "Lifelong_Opportunity_HVAC_Guide_English_v1.0.pdf": "Lifelong_Opportunity_HVAC_Technician_and_Refrigeration_Mechanic_Guide_English_v1.0.pdf",
    },
    "30-electrician-and-electrical-technician/README.md": {
        "Lifelong_Opportunity_Electrician_Guide_English_v1.0.docx": "Lifelong_Opportunity_Electrician_and_Electrical_Technician_Guide_English_v1.0.docx",
        "Lifelong_Opportunity_Electrician_Guide_English_v1.0.pdf": "Lifelong_Opportunity_Electrician_and_Electrical_Technician_Guide_English_v1.0.pdf",
    },
    "54-occupational-therapy-assistant/README.md": {
        "Physical Therapist Assistant.docx": "Lifelong_Opportunity_Occupational_Therapy_Assistant_Guide_English_v1.0.docx",
        "Physical Therapist Assistant.pdf": "Lifelong_Opportunity_Occupational_Therapy_Assistant_Guide_English_v1.0.pdf",
    },
}

for rel, mapping in replacements.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8-sig")
    for old, new in mapping.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")

print("Publication preflight corrections applied.")
