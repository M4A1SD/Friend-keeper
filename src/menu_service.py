class MenuService:
    def __init__(self):
        self.menu = ["1. I have new entry", "2. Im free for action", "3. Add new friend"]
        self.friends = ["benny", "niko", "lior"]
        # self.friends = firbase.get_all_friends()

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
            firebase_service.upload_information(friend_name, response_json)
        else:
            print("not saved") 