
import firebase_admin
from firebase_admin import credentials

credentials = credentials.Certificate("./credentials/private_key.json")
firebase_admin.initialize_app(credentials)
