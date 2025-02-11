import tkinter as tk
from tkinter import messagebox, scrolledtext
from difflib import get_close_matches
import json

class Translate:
    def __init__(self, root):
        self.root = root
        self.root.title("English Dictionary")
        self.root.configure(bg="white")

        # Load the data
        try:
            with open("words-data.json", "r") as file:
                self.data = json.load(file)
        
        except FileNotFoundError:
            messagebox.showerror("Error", "words-data.json file not found!")
            self.root.destroy()

        # Header
        self.header = tk.Label(root, text="English Dictionary", bg="cornflower blue", fg="white", font=("Arial", 18, "bold"))
        self.header.pack(fill=tk.X)

        # Search field and buttons
        self.search_bar = tk.Frame(root, bg="white")
        self.search_bar.pack(pady=20)

        self.search_label = tk.Label(self.search_bar, text="Enter a word:", bg="white", font=("Arial", 12))
        self.search_label.pack(side=tk.LEFT, padx=5)

        self.user_input = tk.Entry(self.search_bar, font=("Arial", 12), width=30)
        self.user_input.pack(side=tk.LEFT, padx=5)

        self.search_btn = tk.Button(self.search_bar, text="Search", command=self.search_word, font=("Arial", 12), bg="cornflower blue", fg="white")
        self.search_btn.pack(side=tk.LEFT, padx=5)

        self.clear_btn = tk.Button(self.search_bar, text="Clear", command=self.clear_input, font=("Arial", 12), bg="cornflower blue", fg="white")
        self.clear_btn.pack(side=tk.LEFT, padx=5)

        # Output area
        self.display_area = tk.Frame(root, bg="white")
        self.display_area.pack(pady=10)

        self.word_meaning = scrolledtext.ScrolledText(self.display_area, wrap=tk.WORD, width=50, height=10, font=("Arial", 12), bg="white")
        self.word_meaning.pack()
        self.word_meaning.configure(state="disabled")

        # Suggestion buttons
        self.suggestion = tk.Frame(root, bg="white")
        self.suggestion.pack(pady=10)

        self.yes_btn = tk.Button(self.suggestion, text="Yes", command=self.accept_suggestion, font=("Arial", 12), bg="cornflower blue", fg="white")
        self.no_btn = tk.Button(self.suggestion, text="No", command=self.reject_suggestion, font=("Arial", 12), bg="cornflower blue", fg="white")
        
        self.reset_state()

    # reset the UI to the default state.
    def reset_state(self):
        self.word_meaning.configure(state="normal")
        self.word_meaning.delete(1.0, tk.END)
        self.word_meaning.configure(state="disabled")
        self.yes_btn.pack_forget()
        self.no_btn.pack_forget()

    
    # Search for the word entered by the user
    def search_word(self):
        self.reset_state()

        word = self.user_input.get().strip().lower()

        if not word:
            messagebox.showwarning("Input Error", "Please enter a word to search.")
            return

        if word in self.data:
            meanings = self.data[word]
            self.display_result(meanings)
        
        else:
            self.suggest_word(word)

    # Suggest a close match for the entered word
    def suggest_word(self, word):
        filtered_word = list(filter(lambda x: x.startswith(word[0]), self.data.keys()))
        closest_matches = get_close_matches(word, filtered_word)

        if closest_matches:
            suggested_word = closest_matches[0]
            self.word_meaning.configure(state="normal")
            self.word_meaning.insert(tk.END, f"Did you mean \u2022\u2022\u2022 {suggested_word} \u2022\u2022\u2022 instead?", "suggestion")
            self.word_meaning.tag_configure("suggestion", font=("Arial", 12, "bold italic"))
            self.word_meaning.configure(state="disabled")
            self.yes_btn.pack(side=tk.LEFT, padx=5)
            self.no_btn.pack(side=tk.LEFT, padx=5)

            self.suggested_word = suggested_word  # store the suggestion for later use
        
        else:
            self.word_meaning.configure(state="normal")
            self.word_meaning.insert(tk.END, "Word not found. Please check the spelling or try another word.", "error")
            self.word_meaning.tag_configure("error", font=("Arial", 12))
            self.word_meaning.configure(state="disabled")


    # Handle the case where the user accepts the suggested word
    def accept_suggestion(self):
        self.user_input.delete(0, tk.END)
        self.user_input.insert(0, self.suggested_word)
        meanings = self.data[self.suggested_word]
        self.display_result(meanings)
        self.yes_btn.pack_forget()
        self.no_btn.pack_forget()

    
    # Handle the case where the user rejects the suggested word
    def reject_suggestion(self):
        self.word_meaning.configure(state="normal")
        self.word_meaning.delete(1.0, tk.END)
        self.word_meaning.insert(tk.END, "Word not found. Please check the spelling or try another word.", "error")
        self.word_meaning.tag_configure("error", font=("Arial", 12))
        self.word_meaning.configure(state="disabled")
        self.yes_btn.pack_forget()
        self.no_btn.pack_forget()

    
    # Display the meanings of the word
    def display_result(self, meanings):
        self.word_meaning.configure(state="normal")
        self.word_meaning.delete(1.0, tk.END)
        
        if isinstance(meanings, list):
            self.word_meaning.insert(tk.END, "\n".join(meanings), "result")
        
        else:
            self.word_meaning.insert(tk.END, meanings, "result")
        
        self.word_meaning.tag_configure("result", font=("Arial", 12))
        self.word_meaning.configure(state="disabled")

    # Clear the input and output fields
    def clear_input(self):
        self.user_input.delete(0, tk.END)
        self.reset_state()


# Create the main window
root = tk.Tk()
app = Translate(root)
root.mainloop()
