import email, getpass, imaplib, os, re
from matplotlib import pyplot as plt
from NavpsModule import Navps

detach_dir = "‎~/Documents/08_PYTHON/00_PROJECTS/PyCharm"

user = input("Enter gmail address: ")
pwd = getpass.getpass("Enter password: ")

m = imaplib.IMAP4_SSL("imap.googlemail.com", 993)

try:
    m.login(user, pwd)
except:
    print("Error: Login unsuccessful")

print(m)
#select the inbox to search emails from
m.select("Personal/NAVPS-Sunlife")
resp, items = m.search(None, '(FROM "phil_mfonline@sunlife.com")')
mailIdItems = items[0].split()
print(f"items\n{items}")
print(f"mailIdItems\n{mailIdItems}")

my_rawmsgs = [] # store relevant msgs here in please
my_msgs = []
msg_cnt = 0
break_ = False

#pythonic way to convert an array of objects into another object
#mailIdItems = [ int(x) for x in mailIdItems ]

if resp=='OK':
    for i in mailIdItems[:11:]:
        #gets the body from emails with the id in mailIdItems
        type, data = m.fetch(i, "(BODY.PEEK[TEXT])")
        print(data)
        #data[0][1] means idk
        my_rawmsgs.append(email.message_from_bytes(data[0][1]))

    #convert the byte string into a string
    #convert the string into a list of strings
    for i in range(len(my_rawmsgs)):
        byte_string = my_rawmsgs[i].get_payload(decode=True)
        msg = byte_string.decode().split()
        my_msgs.append(msg)

else:
    print("Error fetching emails.")

#for i in my_msgs:
    #print(f"my_msgs{i}")

navpsdict = []
for msg in my_msgs:
    for i, word in enumerate(msg):
        print(f"i: {i}\tword: {word}")
        if word.endswith(".</p>"):
            navpsdict.append(word)
        if word.endswith("<br>"):
            navpsdict.append(msg[i-2] + msg[i-1] + msg[i])


#print(navpsdict)

navpsobj = Navps("01/16/2019",
                 3.1157,
                 3.5618,
                 3.6747,
                 1.2716,
                 1.7159,
                 0.8817,
                 0.8790,
                 3.8082,
                 3.2896,
                 1.1221,
                 1.3090,
                 1.0407)

print(navpsobj.printAttr())
navpsobj.updateItem("bond", 3.4567)
print(navpsobj.getItem("bond"))
print(navpsobj.printAttr())
