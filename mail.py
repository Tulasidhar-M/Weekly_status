import smtplib
import yagmail
import pandas as pd

import mysql.connector


host= 'TGHU1DELL0030'
user= 'sa'
passwd= 'Dbase@1234'
db= 'accelerator'

mydb = mysql.connector.connect(
     host=host,
     user=user,
     passwd=passwd,
     database=db
     )
myconn =mydb

query = """select * from OverallApp_description_name;"""

df = pd.read_sql(query, myconn)

# receiver = "*******@gmail.com"

print(df)
exit()
yag = yagmail.SMTP("*******@gmail.com")
yag.send(
        to=receiver,
        subject="Verify your email",
        contents=df.to_string(), 
        )

print("done")