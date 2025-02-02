import json

class PromptService:
    @staticmethod
    def load_prompt(file_path="prompts.json"):
        with open(file_path, "r", encoding="utf-8") as file:
            prompts = json.load(file)
            
        # Process any @file references
        for key, value in prompts.items():
            if isinstance(value, str) and value.startswith("@file:"):
                file_to_read = value[6:]  # Remove "@file:" prefix
                try:
                    with open(file_to_read, "r", encoding="utf-8") as referenced_file:
                        prompts[key] = referenced_file.read()
                except FileNotFoundError:
                    print(f"Warning: Referenced file {file_to_read} not found")
                    
        return prompts 