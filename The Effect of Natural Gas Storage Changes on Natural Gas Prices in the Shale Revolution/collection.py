import PyPDF2
import re

def extract_financial_data(pdf_path):
    data = {
        "Total Revenue": [],
        "Commercial Airplanes Revenue": [],
        "Defense, Space & Security Revenue": [],
        "Global Services Revenue": [],
        "Boeing Capital Revenue": []
    }
    
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                revenue_match = re.findall(r'Total\s+(\d{2},\d{3})', text)
                if revenue_match:
                    data["Total Revenue"].extend(revenue_match)
                
                commercial_match = re.findall(r'Commercial Airplanes\s+(\d{2},\d{3})', text)
                if commercial_match:
                    data["Commercial Airplanes Revenue"].extend(commercial_match)
                
                defense_match = re.findall(r'Defense, Space & Security\s+(\d{2},\d{3})', text)
                if defense_match:
                    data["Defense, Space & Security Revenue"].extend(defense_match)
                
                services_match = re.findall(r'Global Services\s+(\d{2},\d{3})', text)
                if services_match:
                    data["Global Services Revenue"].extend(services_match)
                
                capital_match = re.findall(r'Boeing Capital\s+(\d{2,3})', text)
                if capital_match:
                    data["Boeing Capital Revenue"].extend(capital_match)
    
    return data

if __name__ == "__main__":
    pdf_path = "Boeing_Co_Analysis.pdf"  # Update with the correct file path
    extracted_data = extract_financial_data(pdf_path)
    
    for key, values in extracted_data.items():
        print(f"{key}: {values}")
