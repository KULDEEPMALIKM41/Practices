import pandas as pd
import datetime
import smtplib
# import os

# os.chdir(r"E:\study\company_work\python_tools\Data Analysis")

GMAIL_ID = "your-gmail-id"
GMAIL_PASS = "your-gmail-password"

def sendEmail(to, sub, msg, name):
    print(f"email sent to {to}")
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PASS)
    s.sendmail(GMAIL_ID,to,f"Subject: {sub}\n\n{msg} {name}")
    s.quit()


if __name__ == "__main__":
    df = pd.read_excel("statics/data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    sent_mark = []
    for index, item in df.iterrows():
        bday = item["Birthday"].strftime("%d-%m")
        if today == bday and yearNow not in str(item["WishedYear"]):
            sendEmail(item['Email'],'Birthday Wishes',item['Dialogue'], item['Name'])
            sent_mark.append(index)
    for sent in sent_mark:
        yr = df.loc[sent, "WishedYear"]
        df.loc[sent, "WishedYear"] = str(yr)+", "+str(yearNow)
    df.to_excel("statics/data.xlsx" ,index=False)