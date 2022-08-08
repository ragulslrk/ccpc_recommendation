
import firebase_admin
from firebase_admin import credentials``

credi = credentials.Certificate("./credentials/private_key.json")
firebase_admin.initialize_app(credi)
def prints():
    a='hi'
    return a