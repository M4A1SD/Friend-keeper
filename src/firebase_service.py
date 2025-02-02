import firebase_admin
from firebase_admin import credentials, firestore



class FirebaseService:
    db = None
    def __init__(self):
        try:
            cred = credentials.Certificate("key.json")
            firebase_admin.initialize_app(cred)
            db = firestore.client()
            self.db = db
        except Exception as e:
            print("couldnt connect to firebase")
            print(e)

    def upload_to_db(self, friend_name, new_information, current_date):
        try:
            doc_ref = self.db.collection("friends").document(friend_name).collection("Entries").document(current_date)
            doc_ref.set({
                "data": new_information,
                "timestamp": current_date
            })
            return True
        except Exception as e:
            print("failed to upload to firevbase")
            print(e)
            return False




    def get_all_friends(self):
        try:
            return self.db.collection("friends").get()
        except Exception as e:
            print("failed to get all friends")
            print(e)
            return None
    
    def get_bio(self, friend_name):
        try:
            friend_ref = self.db.collection("friends").document(friend_name)

            friend_doc = friend_ref.get()
            if friend_doc.exists:
                friend_data = friend_doc.to_dict()
                biography = friend_data.get("biography")
                return biography
            else:
                return None
        except Exception as e:
            print("failed to get bio")
            print(e)
            return None

    def get_all_information(self, friend_name):
        try:
            friend_ref = self.db.collection("friends").document(friend_name)
            entries_ref = friend_ref.collection("Entries")
            entries = entries_ref.stream()
            return entries
        except Exception as e:
            print("failed to get all information")
            print(e)
            return None
    def get_when_last_talked(self, friend_name):
        try:
            entries_ref = self.db.collection("Friends").document(friend_name).collection("Entries")
            latest_entry_query = entries_ref.order_by("timestamp", direction=firestore.Query.DESCENDING).limit(1)
            latest_entries = latest_entry_query.get()
            if latest_entries:
                latest_doc = latest_entries[0]
                # latest_doc.id is the human readable date
                return {"date": latest_doc.id, "data": latest_doc.to_dict()}
            else:
                return None

 
        except Exception as e:
            print("failed to get when last talked")
            print(e)
            return None

