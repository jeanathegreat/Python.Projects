import email, getpass, imaplib, os, re
from matplotlib import pyplot as plt

detach_dir = "‎~/Documents/08_PYTHON/00_PROJECTS/PyCharm"

user = input("Enter gmail address: ")
pwd = getpass.getpass("Enter password: ")

m = imaplib.IMAP4_SSL("imap.googlemail.com", 993)

#try:
m.login(user, pwd)

print(m)
#select the inbox to search emails from
m.select("Personal/NAVPS-Sunlife")
resp, items = m.search(None, '(FROM "phil_mfonline@sunlife.com")')
mailIdItems = items[0].split()

my_msg = [] # store relevant msgs here in please
msg_cnt = 0
break_ = False

#mailIdItems = [ int(x) for x in mailIdItems ]
print(mailIdItems)

if resp=='OK':
    for item in mailIdItems[0:11:]:
        type, data = m.fetch(item, "(BODY.PEEK[TEXT])")
        raw = email.message_from_bytes(data[0][1])
        print(f"Email no. {item}\n{raw}")
else:
    print("Error fetching emails.")


#print(f"mailiditems: {mailIdItems[0]}")
#print(type)
#print(data)
#print("This is raw")
#print(raw)
#print("This is data")
#print(data[0][1])
 #   for response_part in data:
 #       if isinstance(response_part, tuple):
 #           msg = email.message_from_string(response_part[1])
 #           email_subject = msg['subject']
 #           email_from = msg['from']
 #           print(f"From :{email_from}")
 #           print(f"Subject :{email_subject}")


#except:
 #   print(f"Error: Login unsuccessful")
    #phil_mfonline@sunlife.com