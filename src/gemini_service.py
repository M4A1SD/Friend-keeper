import google.generativeai as genai
import os
import json

class GeminiService:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")
    
    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        return response

    def break_down_information(self, information, prompt_template, current_time):
        prompt = f"Rules:{prompt_template}\nInput:{information}\nCurrent time:{current_time}"
        response = self.model.generate_content(prompt)
        
        try:
            response_text = response.text.strip()
            if response_text.startswith("```json"):
                response_text = response_text.replace("```json", "", 1)
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            response_text = response_text.strip()
            
            response_json = json.loads(response_text)
            print("Parsed JSON response:", json.dumps(response_json, indent=2))
            return response_json
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            print("Original response:", response.text)
            return None 
        
    


    def ignite_the_spark(self, friend_name):
        """
        user wants to reconnect with a friend. goal is to learn friend biograpy and entries and come up with 5 questions to ask and 5 meetup ideas
        """
        friend_bio = self.firebase_service.get_bio(friend_name)
        friend_entries = self.firebase_service.get_all_information(friend_name)
        friend_last_talked = self.firebase_service.get_when_last_talked(friend_name)
        
        pass
