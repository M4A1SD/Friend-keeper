from .firebase_service import FirebaseService

class MenuService:
    firebase_service = None
    def __init__(self):
        self.firebase_service = FirebaseService()
        self.menu = ["1. I have new entry", "2. Im free for action", "3. Add new friend"]
        # self.friends = ["benny", "niko", "lior"]
        self.friends = self.firebase_service.get_all_friends()

    def display_menu(self):
        print(self.menu)
        return input("Enter your choice:\n")

    def display_friends(self):
        print(self.friends)
        return input("enter friend name:\n")

    def get_new_information(self):
        return input("enter new information:\n")
    
    def handle_new_entry(self, gemini_service, prompts_dictionary, firebase_service):
        friend_name = self.display_friends()
        new_information = self.get_new_information()
        
        response_json = gemini_service.break_down_information(
            new_information, 
            prompts_dictionary['breakDownInformation']
        )
        
        stop = input("Enter 1 to continue...")
        if stop == "1":
            self.firebase_service.upload_information(friend_name, response_json)
        else:
            print("not saved")

    def handle_free_for_action(self, gemini_service):
        friends = self.firebase_service.get_sorted_friends()
        if not friends:
            print("No friends found or could not fetch friends list.")
            return
        
        print("Select a friend:")
        for i, (friend, data) in enumerate(friends.items(), 1):
            print(f"{i}. {friend}. last talk: {data['date']} \n")
        
        input_friend = input("Enter the number of the friend: ")
        friend_name = list(friends.keys())[int(input_friend) - 1]
        friend_data = {
            "name": friend_name,
            "data": friends.get(friend_name).get("data")
        }
        print(f"Selected friend: {friend_name}")

        questions, meetup_ideas = gemini_service.ignite_the_spark(friend_data)
        
        print("\nFollow-up questions:")
        for i, question in enumerate(questions, 1):
            print(f"{i}. {question}")
        
        print("\n-------------------------\nMeetup ideas:")
        for i, idea in enumerate(meetup_ideas, 1):
            print(f"{i}. {idea}") 