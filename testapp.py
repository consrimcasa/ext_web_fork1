import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.api_core.exceptions import ServiceUnavailable, RetryError
import os
# from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Initialize Firebase Admin SDK
firebase_credentials_path = os.path.join("./", 'firebase', 'consrimcasa-89f6e-firebase-adminsdk-vd1lo-83a337bd3e.json')
firebase_credentials = credentials.Certificate(firebase_credentials_path)
firebase_admin.initialize_app(firebase_credentials)

# print("start config")
# cred = credentials.Certificate("/Users/med_mahmoud/Desktop/minister_exterieure_project/site_web/minister_ext_website/minister_ext/firebase/testfunction-cc830-firebase-adminsdk-b1x8c-1ac707a227.json")


# try:
#     # firebase_admin.initialize_app(cred)
#     print("end config")

#     def get_users():
#         # Example: Fetch documents from Firestore
#         data = []
#         try:
#             docs = firestore.client().collection('users').stream()
#             for doc in docs:
#                 data.append(doc.to_dict())
#             print(f"data : {data}")
#             return data
#         except ServiceUnavailable as su_exception:
#             print(f"ServiceUnavailable exception: {su_exception}")
#         except RetryError as retry_exception:
#             print(f"RetryError exception: {retry_exception}")

#     print("start fetch data")
#     result = get_users()
#     print("end fetch data")
#     print(f"result : {result}")

# except Exception as e:
#     print(f"Error during initialization: {e}")


user_data = {
                'id': "user_id",
                # 'image': None,  # You can handle image upload separately
                'firstName': "first_name",
                'lastName': "last_name",
                'phoneNumber': "phone_number",
                'email': "email",
                'password': "hashed_password",
            }

            # Save user data to Firestore
db = firestore.client()
user_ref = db.collection('users').document("user_id")
user_ref.set(user_data)
print("end add data")

