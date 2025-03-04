import PyPDF2
import requests
import re

def extract_urls_from_pdf(pdf_path):
    urls = set()
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            found_urls = re.findall(r'https?://\S+', text)
            urls.update(found_urls)
    return urls

def fetch_data_from_urls(urls):
    data = {}
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data[url] = response.text
            else:
                data[url] = f"Failed to fetch (status code: {response.status_code})"
        except requests.RequestException as e:
            data[url] = f"Request failed: {e}"
    return data

def save_data_to_file(data, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for url, content in data.items():
            file.write(f"URL: {url}\n\n{content}\n\n{'='*80}\n\n")

if __name__ == "__main__":
    pdf_path = "/mnt/data/Boeing Co. Analysis.docx.pdf"
    output_file = "boeing_data.txt"
    
    urls = extract_urls_from_pdf(pdf_path)
    collected_data = fetch_data_from_urls(urls)
    save_data_to_file(collected_data, output_file)
    
    print(f"Data collection complete. Saved to {output_file}")
