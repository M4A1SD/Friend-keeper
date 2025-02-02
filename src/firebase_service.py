import firebase_admin
from firebase_admin import credentials, firestore
from src.time_service import TimeService


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

    def upload_information(self, friend_name, new_information):
        """
        friends -> friend_name -> Entries -> current_date -> {data: new_information, timestamp: firestore.SERVER_TIMESTAMP}

        """
        try:
            current_date = "" + TimeService.get_current_time()

            print(f" firebase_service, upload_information(): uploading to firebase: {friend_name}->{current_date}-> (data: {new_information} , timestamp: {firestore.SERVER_TIMESTAMP})")
            doc_ref = self.db.collection("friends").document(friend_name).collection("entries").document(current_date)
            doc_ref.set({
                "data": new_information,
                "timestamp": firestore.SERVER_TIMESTAMP
            })
            return True
        except Exception as e:
            print("failed to upload to firevbase")
            print(e)
            return False

    def get_all_friends(self):
        """
        return names ['niko', 'benny', 'lior']
        """
        try:
            friends = self.db.collection("friends").stream()
            names_array = []
            for friend in friends:
                names_array.append(friend.id)
            return names_array

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
            entries_ref = friend_ref.collection("entries")
            entries = entries_ref.stream()
            return entries
        except Exception as e:
            print("failed to get all information")
            print(e)
            return None
    
    def get_when_last_talked(self, friend_name):
        """
        return the date "2025-01-01 12:23"
        """
        try:
            entries_ref = self.db.collection("friends").document(friend_name).collection("entries")
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

    def get_sorted_friends(self):
        """
        return names ['niko', 'benny', 'lior']
        in order of last entry date
        """
        names_array = []
        friends_dict = {}
        friends = self.get_all_friends()
        for friend in friends:
            last_entry_date = self.get_when_last_talked(friend)
            friends_dict[friend] = last_entry_date

        sorted_friends = sorted(friends_dict.items(), key=lambda x: x[1], reverse=True)
        for friend in sorted_friends:
            names_array.append(friend[0])
        return names_array