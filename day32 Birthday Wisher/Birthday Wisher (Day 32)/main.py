import smtplib
# old
"""my_email = "ramubhaiya487@gmail.com"
password = "XXXXXXXXXXXXXXXXX"
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="ramubhaiya487@outlook.com",
                    msg="Subject:hi champak lal\n\n This is the body of the email.")
connection.close()"""

# new
my_email = "ramubhaiya487@gmail.com"
password = "ymsfxuvubvsimaeq"


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="ramubhaiya487@outlook.com",
                        msg="Subject:hi champak lal\n\n This is the body of the email.")
