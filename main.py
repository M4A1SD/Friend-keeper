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
        else:
            print(friends)




    elif choice == "3":
        print("Add new friend")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

