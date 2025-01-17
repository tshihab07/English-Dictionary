# English Dictionary Application

## Overview
The English Dictionary Application is a user-friendly GUI-based tool built with Python and Tkinter. It allows users to search for the meanings of words from a predefined dataset. The app provides suggestions for misspelled words and offers an intuitive interface with features like a search bar, a clear button, and scrollable output for longer definitions. The application is ideal for learners, educators, and anyone looking to quickly find word meanings.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/tshihab/english-dictionary
   ```

2. **Install Dependencies:**
   Ensure you have Python installed on your system (version 3.6 or later). Install the required packages using:
   ```bash
   pip install json
   pip install difflib
   pip install tkinter

   ```

3. **Prepare the Data:**
   Ensure the `words-data.json` file is in the project directory. This file contains the dictionary data in JSON format.

   > **Acknowledgment:** The dataset used in this project was sourced from the WebstersEnglishDictionary repository. Full credit goes to the original author for compiling this resource. Refer to their repository for more details: [Github Source](https://github.com/matthewreagan/WebstersEnglishDictionary).

## Usage

1. **Run the Application:**
   Execute the script to launch the GUI:
   ```bash
   python gui.py
   ```

2. **Features:**
   - Enter a word in the search field and press the "Search" button to view its meaning.
   - If the input word is misspelled, the app will suggest the closest match. You can choose "Yes" to accept or "No" to reject the suggestion.
   - Use the "Clear" button to reset the input and output fields.
   - Scroll through long definitions using the integrated scrollable text area.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software in compliance with the license terms.
