from src.gemini_service import GeminiService
from src.time_service import TimeService
from src.prompt_service import PromptService
from src.menu_service import MenuService
from src.firebase_service import FirebaseService
def main():
    # Initialize services
    gemini_service = GeminiService() # prpcess information
    menu_service = MenuService() # display information and interactoin
    prompts_dictionary = PromptService.load_prompt() # prompt engineering
    firebase_service = FirebaseService()

    # Check if Firebase is properly initialized
    if not firebase_service.db:
        print("Error: Could not connect to Firebase. Please check your configuration.")
        return

    # Main menu loop
    choice = menu_service.display_menu()

    if choice == "1":
        menu_service.handle_new_entry(gemini_service, prompts_dictionary, firebase_service)
    elif choice == "2":
        """
        i can look up all my friends
        the list is sorted by the last entry date
        i can select a friend, lets say type the name
        then i get 5 questions about recent entry-follow up
        5 meetup ideas to propose.
        """
        # Im free for action

        friends = firebase_service.get_sorted_friends()
        if not friends:
            print("No friends found or could not fetch friends list.")
            exit()
        
        print("Select a friend:")
        i=1
        for friend, data in friends.items():
            print(f"{i}. {friend}. last talk: {data['date']} \n")
            i+=1
        input_friend = input("Enter the number of the friend: ")
        friend_name = list(friends.keys())[int(input_friend) - 1]
        print(f"Selected friend: {friend_name}")

        # get bio
        bio = firebase_service.get_bio(friend_name)
        # get all entries
        entries = firebase_service.get_all_information(friend_name)

        # get last entry
        last_entry = friends.get(friend_name).get("data")
        last_entry = " | ".join(last_entry)

        print(f"my friend {friend_name}, bio: {bio}, last entry: {last_entry}. i want to meetup with him")



    elif choice == "3":
        print("Add new friend")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

