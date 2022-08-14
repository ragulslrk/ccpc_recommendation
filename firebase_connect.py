import firebase_admin
from firebase_admin import credentials,firestore
import json
import re
cred = credentials.Certificate("./private_key.json")
firebase_admin.initialize_app(cred)
datab= firestore.client()
vtitle=[]
ititle=[]
iewref = datab.collection(u'iew')
internref=datab.collection(u'internship')


def splremover(x):
    print(x)
    bad_chars = [';', ':', '!', "*",'(',')','"']
    temp = ''
    str1=""
    for i in bad_chars:
        temp+= i;
#Replacing special characters with null and converting to string
        res = str1.join(re.sub(rf'[{temp}]', '',x))
#Joining the individual charactes into list
        user=list(res.split(','))
    return user

def videoreturn(aoi):
#Cleaning the incoming area of interest
    xx=re.sub(r"[\(\)]",'',aoi)
    user=list(xx.split(","))
#Fetching from iew
    docs = iewref.stream()
    for moc in docs:
        rdata=moc.to_dict()
        x2=json.dumps(rdata.get("category_name"))
        vtitle.append(splremover(x2))
#Fetching from internship
    idocs = internref.stream()
    for moc in idocs:
        idata=moc.to_dict()
        x3=json.dumps(idata.get("domain_name"))
        ititle.append(splremover(x3))
#Checking if genre present in video title
    flag=1
    yesvideotags=[]
    novideotags=[]
    for i in range(len(user)):
        for j in range(len(vtitle)):
            if user[i] in vtitle[j][0]:
                yesvideotags.append(vtitle[j][0])
            else:
                if(flag):
                    novideotags.append(vtitle[j][0])
        flag=0
#Checking if genre present in internship title
    flag=1
    yesinterntags=[]
    nointerntags=[]
    for i in range(len(user)):
        for j in range(len(ititle)):
            if user[i] in ititle[j][0]:
                yesinterntags.append(ititle[j][0])
            else:
                if(flag):
                    nointerntags.append(ititle[j][0])
        flag=0
#Combining the 2 arrays
    iewtags=yesvideotags+novideotags
    interntags=yesinterntags+nointerntags
    iewtags = [a for a in iewtags if a.strip()]
    interntags = [ b for b in interntags if b.strip()]
    return(iewtags,interntags)
