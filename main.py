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
    # Main menu loop
    choice = menu_service.display_menu()

    if choice == "1":
        menu_service.handle_new_entry(gemini_service, prompts_dictionary, firebase_service)
    elif choice == "2":
        print("Im free for action")
    elif choice == "3":
        print("Add new friend")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

