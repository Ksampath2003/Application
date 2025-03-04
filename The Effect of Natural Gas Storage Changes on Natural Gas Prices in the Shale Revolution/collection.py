import PyPDF2
import re

def extract_natural_gas_data(pdf_path):
    data = {
        "Henry Hub Spot Price": [],
        "Monthly Storage Change": [],
        "WTI Spot Price": [],
        "Power Demand": [],
        "Heating Degree Days": []
    }
    
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                hh_price_match = re.findall(r'Henry Hub Spot Price.*?(\d{3,4})', text)
                if hh_price_match:
                    data["Henry Hub Spot Price"].extend(hh_price_match)
                
                storage_match = re.findall(r'Monthly Storage Change.*?(\d{1,4})', text)
                if storage_match:
                    data["Monthly Storage Change"].extend(storage_match)
                
                wti_match = re.findall(r'WTI Spot Price.*?(\d{1,3})', text)
                if wti_match:
                    data["WTI Spot Price"].extend(wti_match)
                
                power_match = re.findall(r'Power Demand.*?(\d{1,5})', text)
                if power_match:
                    data["Power Demand"].extend(power_match)
                
                hdd_match = re.findall(r'Heating Degree Days.*?(\d{1,5})', text)
                if hdd_match:
                    data["Heating Degree Days"].extend(hdd_match)
    
    return data

if __name__ == "__main__":
    pdf_path = "Natural_Gas_Analysis.pdf"  # Update with the correct file path
    extracted_data = extract_natural_gas_data(pdf_path)
    
    for key, values in extracted_data.items():
        print(f"{key}: {values}")
