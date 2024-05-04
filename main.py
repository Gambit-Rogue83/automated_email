import smtplib
import datetime as dt
import random
import datetime as dt
import pandas

my_email = "happy_programmer214@gmail.com"
password = "vexnarxlphojwuzh"

today = (dt.datetime.now().month, dt.datetime.now().day)


bday_data = pandas.read_csv("birthdays.csv")
bday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in bday_data.iterrows()}
if today in bday_dict:
    bday_person = bday_dict[today]
    letter = f"letter_{random.randint(1, 3)}.txt"
    with open(letter) as email:
        contents = email.read()
        contents = contents.replace("[NAME]", bday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=bday_person["email"],
            msg=f"Subject: Happy Birthday\n\n{contents}"
        )

# now = dt.datetime.now()
# day = now.weekday()

# if day == 4:
#     with open("quotes.txt") as quote_file:
#         quote_list = quote_file.readlines()
#         quote = random.choice(quote_list)
# #
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="unsatisfied_programmer412@ymail.com",
#             msg=f"Subject: Quote of the Week\n\n{quote}"
#         )

#


