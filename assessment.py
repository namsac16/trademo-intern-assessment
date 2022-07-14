from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
import csv

base_url = "https://www.sanctionsmap.eu/#/main/details/15/lists?search=%7B%22value%22:%22%22,%22searchType%22:%7B%7D%7D"

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get(base_url)

sleep(10)
html = driver.page_source           # Loading HTML Data of Website

soup = BeautifulSoup(html, "html.parser")       # Parsing HTML Data using BeautifulSoup
tables = soup.find_all("custom-table")          # Finding Required Table
for data in tables:
    table = data.find_all("ul", {"class": "filter-list"})       # Finding Required List
    with open("data.csv", "a", encoding="utf8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "FSD-ID", "Name", "Date"])
        for element in table:
            type = element.find("li", {"data-heading": "Type"}).text.strip()
            fsd_id = element.find("li", {"data-heading": "FSD Id"}).text.strip()
            name = element.find("li", {"data-heading": "Name"}).text.strip()
            dod = element.find("li", {"data-heading": "Date of designation (if available on FSD)"}).text.strip()
            writer.writerow([type, fsd_id, name, dod])
        writer.writerow([])