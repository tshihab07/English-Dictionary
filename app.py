import json, difflib

def transalate(word, data):
    result = ""
    # Load the translation data
    if word in data:
        return data[word]
    
    else:
        filtered_data = list(filter(lambda x: x.startswith(word[0]), data.keys()))
        closest_match = difflib.get_close_matches(word, filtered_data)
        
        if len(closest_match) > 0:
            user_confirmation = input(f"Did you mean {closest_match[0]} instead? Enter Y if yes, or N if no: ").lower()
            
            if user_confirmation == "y":
                result = data[closest_match[0]]
            
            elif user_confirmation == "n":
                result = "The word doesn't exist. Please double check it."
            
            else:
                result = "We didn't understand your entry. Please try again."
            
    
    return result


def main():
    # Load the translation data
    with open("words-data.json", "r") as file:
        data = json.load(file)

    # Get the word from the user
    word = input("Enter a word: ").lower()
    
    # Translate the word
    result = transalate(word, data)
    print(result)



main()