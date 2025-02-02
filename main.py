from src.gemini_service import GeminiService
from src.time_service import TimeService
from src.prompt_service import PromptService
from src.menu_service import MenuService

def main():
    # Initialize services
    gemini_service = GeminiService()
    menu_service = MenuService()
    prompts_dictionary = PromptService.load_prompt()

    # Main menu loop
    choice = menu_service.display_menu()

    if choice == "1":
        friend_name = menu_service.display_friends()
        new_information = menu_service.get_new_information()
        current_time = TimeService.get_current_time()
        
        gemini_service.break_down_information(
            new_information, 
            prompts_dictionary['breakDownInformation'],
            current_time
        )
        print("saved")
    elif choice == "2":
        print("Im free for action")
    elif choice == "3":
        print("Add new friend")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

