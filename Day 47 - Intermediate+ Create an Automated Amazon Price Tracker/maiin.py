from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

my_email = "xxxxxxxxx@gmail.com"
my_pass = "xxxxxxxxx"

Url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(url=Url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
})

soup = BeautifulSoup(response.content, "lxml")
price = soup.find(name="span", class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
float_price = float(price_without_currency)
print(float_price)
print(price)
price1 = soup.find(class_="a-offscreen").get_text()
print((f"$ {float_price}"))
print(price1)
if float_price <= 100:

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs="shivamkumar819991@gmail.com",
                            msg=f"The price of your requested product is below 100 dollars\n\n"
                                f". It is now  ${float_price}\n\n Here is the link {Url}".encode("utf-8"))
