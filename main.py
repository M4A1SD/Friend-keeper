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
    choice = "0"

    while choice != "4":
        choice = menu_service.display_menu()
        if choice == "1":
            menu_service.handle_new_entry(gemini_service, prompts_dictionary, firebase_service)
            continue
        elif choice == "2":
            menu_service.handle_free_for_action(gemini_service)
            continue
        elif choice == "3":
            print("Add new friend")
            name = input("Enter the name of the friend: ")
            bio = input("Enter the bio of the friend: ")
            firebase_service.add_friend(name, bio)
            continue
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice") 

if __name__ == "__main__":
    main()

