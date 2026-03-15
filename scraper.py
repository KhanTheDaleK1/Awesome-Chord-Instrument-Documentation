import requests
from bs4 import BeautifulSoup
import re
import statistics
import time
import os

# 1. Map your unique placeholder tags to specific eBay queries
INSTRUMENTS = {
    "OM-27": "Suzuki Omnichord OM-27",
    "OM-84": "Suzuki Omnichord OM-84",
    "QCHORD": "Suzuki QChord",
    "POLY800": "Korg Poly-800"
}

def get_ebay_sold_listings(query):
    url = f"https://www.ebay.com/sch/i.html?_nkw={query.replace(' ', '+')}&LH_Sold=1&LH_Complete=1&_ipg=60"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    prices = []

    for item in soup.find_all('div', class_='s-item__info'):
        price_element = item.find('span', class_='s-item__price')
        if not price_element:
            continue
            
        price_text = price_element.text.strip()
        if 'to' in price_text.lower():
            continue
            
        clean_price_str = re.sub(r'[^\d.]', '', price_text)
        try:
            if clean_price_str:
                prices.append(float(clean_price_str))
        except ValueError:
            continue

    return prices

def analyze_market_data(prices):
    if not prices:
        return "N/A"
    if len(prices) > 4:
        prices.sort()
        trim = max(1, len(prices) // 10)
        prices = prices[trim:-trim]
    return f"${round(statistics.mean(prices), 2):.2f}"

def update_readme(market_data):
    """Reads the README.md, replaces the price tags, and saves it."""
    readme_path = 'README.md'
    
    if not os.path.exists(readme_path):
        print("README.md not found. Skipping file update.")
        return

    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for model_id, avg_price in market_data.items():
        # Regex to find: <!-- PRICE_TAG_START -->ANY_TEXT<!-- PRICE_TAG_END --> and replace ANY_TEXT with the newly scraped price
        pattern = rf'(<!-- PRICE_{model_id}_START -->).*?(<!-- PRICE_{model_id}_END -->)'
        replacement = rf'\1{avg_price}\2'
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print("README.md successfully updated.")

def main():
    market_report = {}
    print("Starting Nightly Market Scraping Engine...\n")
    
    for model_id, search_query in INSTRUMENTS.items():
        print(f"Scraping data for {model_id}...")
        prices = get_ebay_sold_listings(search_query)
        avg_price = analyze_market_data(prices)
        market_report[model_id] = avg_price
        
        # Polite delay to avoid IP blocks from eBay
        time.sleep(3)
        
    update_readme(market_report)

if __name__ == "__main__":
    main()
