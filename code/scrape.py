import csv
import email
import imaplib
import time
from datetime import datetime as dt
from pathlib import Path

from NavpsModule import Navps

start_time = time.time()
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

my_rawmsgs = [] # store relevant msgs here please
my_msgs = []
msg_cnt = 0
break_ = False

#pythonic way to convert an array of objects into another object
#mailIdItems = [ int(x) for x in mailIdItems ]

if resp=='OK':
    for i in mailIdItems[::]:
        #gets the body from emails with the id in mailIdItems
        type, data = m.fetch(i, "(BODY.PEEK[TEXT])")
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


navsplist = []
ntemp = []

#clean list of my_msgs to only get date and fundnames and values
for msg in my_msgs:
    for i, word in enumerate(msg):
        print(f"i: {i}\tword: {word}")
        if word.endswith(".</p>"):

            #split the .</p> from the date
            temp = word.split(".")
            print(temp[0])
            #date string to datetime object
            dateobj = dt.strptime(temp[0], '%m/%d/%Y')
            navsplist.append(dateobj)
            nav = Navps()
            nav.updateItem("date", dateobj)
            nav.add(dateobj, ntemp)
        if word.endswith("<br>"):
            #split the <br> from the fund types and values
            temp=word.split("<")
            #fund was found in the word before the word ending in <br>
            if msg[i-1].casefold().find("fund") == 0:
                strtemp = msg[i-2] + msg[i-1] + temp[0]
                navsplist.append(strtemp)
                nav = Navps()
                nav.add(strtemp, ntemp)



print(len(my_msgs) == len(my_rawmsgs))
print(navsplist)

datestr = "01/16/2019"
dtobj = dt.strptime(datestr,'%m/%d/%Y')
print(isinstance(dtobj, dt))

#given list create a csv of the ff data:
#bondfund.csv [(date1, bfvalue2),(date2, bfvalue2),...]
#balancedfund.csv [(date1, bfvalue2),(date2, bfvalue2),...]
#equityfund.csv [(date1, efvalue2),(date2, efvalue2),...]
#marketfund.csv [(date1, efvalue2),(date2, efvalue2),...]
#gsfund.csv [(date1, efvalue2),(date2, efvalue2),...]
#dynamicfund.csv [(date1, efvalue2),(date2, efvalue2),...]
#indexfund.csv [(date1, efvalue2),(date2, efvalue2),...]
#advantagefund.csv [(date1, efvalue2),(date2, efvalue2),...]
#abundancefund.csv [(date1, efvalue2),(date2, efvalue2),...]
#wellspringfund.csv [(date1, efvalue2),(date2, efvalue2),...]
#voyagerfund.csv [(date1, efvalue2),(date2, efvalue2),...]
#starter.csv [(date1, efvalue2),(date2, efvalue2),...]

choices = {"bof":"bondfund.csv",
           "baf":"balancedfund.csv",
           "ef":"equityfund.csv",
           "mf":"marketfund.csv",
           "gf":"gsfund.csv",
           "df":"dynamicfund.csv",
           "inf":"indexfund.csv",
           "adf":"advantagefund.csv",
           "abf":"abundancefund.csv",
           "wf":"wellspringfund.csv",
           "vf":"voyagerfund.csv",
           "sf":"starterfund.csv",
           "a28":"a2028fund.csv",
           "a38":"a2038fund.csv",
           "a48":"a2048fund.csv"}

funds = ['bof','baf','ef','mf','gf','df','inf','adf','abf','wf','vf','sf','a28','a38','a48']

bof = choices.get(funds[0], "default")
baf = "balancedfund.csv"
ef = "equityfund.csv"
mf = "marketfund.csv"
gf = "gsfund.csv"
df = "dynamicfund.csv"
inf = "indexfund.csv"
adf = "advantagefund.csv"
abf = "abundancefund.csv"
wf = "wellspringfund.csv"
vf = "voyagerfund.csv"
sf = "starterfund.csv"
a28 = "a2028fund.csv"



def create_dict_from_list(option, strlist):
    #how you would do switch in python
    result = choices.get(option, "default")
    resultfund = result.split("fund")
    dicts = {}
    dateFound = False
    fundvalue = 0
    date = None
    for item in strlist:
        if isinstance(item, dt) == True:
            date = item
            dateFound = True
            continue


        if item.casefold().find(resultfund[0]) == 0:
            if dateFound == True:
                itemlist = item.split(":")
                fundvalue = itemlist[1]
                dicts[date] = fundvalue
                dateFound = False
                fundvalue = 0
        #else: #need to process what to do with other fund values

    return dicts

def create_csv_from_dict(option, dicttocsv):
    result = choices.get(option, "default")
    csv_columns = ['Date', 'Fund Value']
    detach_dir = Path("output/")
    newcsvfile = detach_dir/result
    try:
        with open(newcsvfile, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csv_columns)
            for key, value in dicttocsv.items():
                writer.writerow([key, value])
    except IOError:
        print("I/O error")

for fund in funds[:-3]:
    csvdict = create_dict_from_list(fund, navsplist)
    create_csv_from_dict(fund, csvdict)
print(csvdict)

print(f"time elapsed: {format(time.time() - start_time)}s")
