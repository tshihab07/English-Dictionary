import json
from difflib import get_close_matches

class Translate:
    def __init__(self, word, data):
        self.word = word
        self.data = data
        self.filter = list(filter(lambda x: x.startswith(self.word[0]), self.data.keys()))
        self.closest_match = get_close_matches(self.word, self.filter)
        self.not_found = "Word not found. Please check the spelling or try another word."
    
    
    @staticmethod
    def input_prompt(message):
        return input(message).strip().lower()


    @classmethod
    def get_data(cls, file):
        try:
            with open(file, "r") as f:
                dict_data = json.load(f)
        
        except FileNotFoundError:
            raise Exception(f"File '{file}' not found. Please ensure it exists in the correct path.")

        user_word = cls.input_prompt("Enter word: ")
        return cls(user_word, dict_data)
    
    
    def user_confirmation(self):
        if not self.closest_match:
            return None
        else:
            response = self.input_prompt(f"Did you mean {self.closest_match[0]} instead? Enter Y if yes, or N if no: ")
            return response
    
    
    def get_meaning(self):
        if self.word in self.data:
            return self.data[self.word]
        
        elif len(self.closest_match) > 0:
            user_choice = self.user_confirmation()
            if user_choice == "y":
                return self.data[self.closest_match[0]]
            
            elif user_choice == "n":
                return self.not_found
            
            else:
                return "Invalid input. Please enter Y or N."

        else:
            return self.not_found
        

def main():
    try:
        data = Translate.get_data("words-data.json")
        result = data.get_meaning()
        print(result)

    except Exception as e:
        print(e)


main()
