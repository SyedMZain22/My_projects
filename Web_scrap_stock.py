import time
import csv
from bs4 import BeautifulSoup
import requests
#SMZBF
#BASIC WEB SCRAPING PROJECT
def parse_stock():
    try:
        url = 'https://finance.yahoo.com/quote/%5EIXIC?p=%5EIXIC'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        req = requests.get(url, headers=headers)
        req.raise_for_status()
        soup = BeautifulSoup(req.text, 'html.parser')
        price_element = soup.find('fin-streamer', {'data-test': 'qsp-price'})
        change_element = soup.find('fin-streamer', {'data-test': 'qsp-price-change'})

        if price_element and change_element:
            current_price = price_element.text
            change = change_element.text
            return current_price, change
        else:
            return "Data not found", "Data not found"
    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:", e)
        return "N/A", "N/A"
    except Exception as e:
        print("An error occurred:", e)
        return "N/A", "N/A"

while True:
    current_price, change = parse_stock()
    print("The current stock price:", current_price)
    print("Change:", change)
    with open("output1.csv", "a", newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([current_price, change])

    time.sleep(1)
