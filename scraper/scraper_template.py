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
    # If using the default template, return in the format: Staff cases, Student cases, Total cases, Quarantined, On Campus Quarantine
    return ["", "", "", "", ""]
    
    
def scrape_pdf(online: bool) -> list:
  url = ""
  filename = "./pdf/NAMETemp.pdf"
  if online:
    with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
  data = pdfToText(filename)
  # If using the default template, return in the format: Staff cases, Student cases, Total cases, Quarantined 
  return ["", "", "", "", ""]

def scrape_csv(online: bool) -> list:
    url = "example.com"
    filename = "./csv/NAMETemp.csv"
    if online:
        with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    data = {}
    # Personal preference is to convert the CSV to dict. You can ignore this if you wish to write your own interpreter
    with open(filename) as f:
        reader = csv.reader(f, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]] = row[1:]
            
    return data[element_name]
  
# All code below is provided in the main code and is here for reference. 

# This will strip out all letters from the list elements. Empty elements are also stripped
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

def pdfToText(string: str) -> list:
    fd = open(string, "rb")
    viewer = SimplePDFViewer(fd)

    plain_text = []
    try:
        while True:
            viewer.render()
            plain_text += viewer.canvas.strings
            viewer.next()
    except PageDoesNotExist:
        pass
    return plain_text
