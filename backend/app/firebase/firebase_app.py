import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("app/firebase/resumecreatorgb-firebase-adminsdk-fbsvc-e60af97fdb.json")
firebase_app = firebase_admin.initialize_app(cred)
firestore_db = firestore.client()
