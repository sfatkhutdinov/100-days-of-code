import requests
from bs4 import BeautifulSoup
import smtplib
from secrets import EMAIL, SMTP, PASSWORD, USER_AGENT_STRING

URL = 'https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/' \
      'ref=sr_1_1?qid=1597662463'
headers = {
    'Accept-Language': 'en-us',
    'User-Agent': USER_AGENT_STRING
}
desired_price = 100

response = requests.get(url=URL, headers=headers)
response.raise_for_status()
product = response.text

soup = BeautifulSoup(product, parser='lxml', features='lxml')
product_name = soup.find(name='span',
                         class_='a-size-large product-title-word-break').text.strip()
price_text = soup.find(name='span',
                       class_='a-size-medium a-color-price priceBlockBuyingPriceString')
price = float(price_text.text.split('$')[1])


if price <= desired_price:
    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n"
                f"{product_name} is on sale for ${price}\n"
                f"You can purchase it here: {URL}".encode('ascii', errors='ignore')
        )

