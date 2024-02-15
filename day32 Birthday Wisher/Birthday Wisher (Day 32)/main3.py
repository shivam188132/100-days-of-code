import datetime as dt
import smtplib
import random

my_email = "ramubhaiya487@gmail.com"
password = "XXXXXXXXX"


now = dt.datetime.now().day
print(now)
if now == 6:
    with open("quotes.txt") as data_file:
        data = data_file.readlines()
        print(type(data))
        quote = random.choice(data)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ramubhaiya487@outlook.com",
                            msg=f"Subject:Today's Motivation\n\n {quote}")
