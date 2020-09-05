import requests
from bs4 import BeautifulSoup
import re
from pdfreader import SimplePDFViewer, PageDoesNotExist
import urllib.request
import shutil

def scrape_html() -> list:
    url = "http://example.com"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.findAll("tag", {"id": "id_name", "class": "class_name"}) # use any technique supported by BeautifulSoup to pull the data out.
    # If using the default template, return in the format: Staff cases, Student cases, Total cases, Quarantined 
    return ["", "", "", ""]
    
    
def scrape_pdf() -> list:
  url = ""
  filename = "./NAMETemp.pdf"
  with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
  # If using the default template, return in the format: Staff cases, Student cases, Total cases, Quarantined 
  return ["", "", "", ""]
  
# Below is a copy of a cleanup function that is commonly used. This will strip out all letters from the list elements. Empty elements are also stripped
def strip_results(results: list) -> list:
    i = 0
    while i < len(results):
        # Strip out empty entries
        results[i] = re.sub("\D", "", str(results[i]))
        if results[i] == '':
            del results[i]
        else:
            i += 1
    return results
