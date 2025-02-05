import google.generativeai as genai
import os
import json
from .prompt_service import PromptService
from .firebase_service import FirebaseService
from .time_service import TimeService

class GeminiService:
    prompts_dictionary = PromptService.load_prompt() # prompt engineering
    firebase_service = None

    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.firebase_service = FirebaseService()
        self.time_service = TimeService()

    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        try:
            response_text = response.text.strip()
            if response_text.startswith("```json"):
                response_text = response_text.replace("```json", "", 1)
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            response_text = response_text.strip()
            
            response_json = json.loads(response_text)
            # print("GeminiService, break_down_information(): Parsed JSON response:", json.dumps(response_json, indent=2))
            return response_json
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            print("Original response:", response.text)
            return None 
        return response

    def break_down_information(self, information, prompt_template):
        prompt = f"Rules:{prompt_template}\nInput:{information}"
        response = self.generate_response(prompt)
        return response['data']
        
        
        
    


    def ignite_the_spark(self, friend_data):
        """
        user wants to reconnect with a friend. goal is to learn friend biograpy and entries and come up with 5 questions to ask and 5 meetup ideas
        """
        friend_name = friend_data.get("name")
        last_entry = friend_data.get("data")
        last_entry = " | ".join(last_entry)
        friend_bio = self.firebase_service.get_bio(friend_name)
        friend_entries = self.firebase_service.get_all_information(friend_name)
        friend_entries = " | ".join(friend_entries)
        friend_last_talked = self.firebase_service.get_when_last_talked(friend_name)
        friend_last_talked=friend_last_talked.get("date")
        today = self.time_service.get_current_time()
        prompt = f"rules: {self.prompts_dictionary['igniteTheSpark']}\nfriend name: {friend_name}\nfriend bio: {friend_bio}\nfriend last entry: {last_entry}\nfriend entries: {friend_entries}\nfriend last talked: {friend_last_talked}\n today's date: {today}"
        response = self.generate_response(prompt)
        return response['conversation_questions'], response['meetup_ideas']
