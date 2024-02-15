import datetime as dt
import pandas
import random
import smtplib




today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")
print(data)
birthday_dict = {(data_row.month, data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthday_dict)

if today in birthday_dict:
    # key of dictionary k corresponding values dega
    birthday_person_details = birthday_dict[today]
    print(birthday_person_details)
    file_path = f"./letter_templates//letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person_details["name"])
    print(contents)

    my_email = birthday_person_details.email
    my_pass = "ymsfxuvubvsimaeq"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs="shivamkumar819991@outlook.com",
                            msg=f"Subject:HAPPY BIRTHDAY \n\n {contents}")


