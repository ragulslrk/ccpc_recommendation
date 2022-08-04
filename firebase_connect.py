#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import firebase_admin
from firebase_admin import credentials,firestore
import json
import re
cred = credentials.Certificate("./private_key.json")
firebase_admin.initialize_app(cred)
datab= firestore.client()
vtitle=[]
ititle=[]
usersref = datab.collection(u'users')
iewref = datab.collection(u'iew')
internref=datab.collection(u'internship')


# In[ ]:


#Function for removing special characters from the string
def splremover(x):
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


# In[ ]:


def videoreturn(uid):
#Fetching from user collection
    docs = usersref.stream()
    for doc in docs:
        data=doc.to_dict()
        if(uid==doc.get("uid")):
            x1=json.dumps(data.get("area of interest"))
    user=splremover(x1) 
    
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
    return(iewtags,interntags)


# In[ ]:


x=videoreturn(uid)

