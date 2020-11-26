import pandas as pd
import datetime
import smtplib
gmailid=''  #enter your mail id in inverted commas
gmailpassword = ''  #enter your email password, before running this program.
def send_email(to,sub,msg):
    print(f'email to {to} sent with subject {sub} with message {msg}')
    s = smtplib.SMTP('smtp.gmail.com','587')
    s.starttls()
    s.login(gmailid,gmailpassword)
    s.sendmail(gmailid,to,f'SUBJECT : {sub}\n\n\n Message: {msg}')
    s.quit()




if __name__ == '__main__':
    df = pd.read_excel('birthrecord.xlsx')
    today = datetime.datetime.now().strftime("%d-%m")
    print(type(today))
    for index,item in df.iterrows():
        bdate1 = item['bdate'].strftime("%d-%m")
        if today == bdate1:

            send_email(item['email'],'Birthday message',item['dailouge'])

