Customizable hangman terminal game with player vs. player or player vs. robot featuresets.

Project was used to better understand and familiarize myself with standard Python scripting after self-study this summer, 
as well as learning about and working with new libraries in bs4, urllib & requests (Web scraping).

Two routes of functionality:

1. Player Versus Player:
  Guesser can set their username & the amount of tries they'd like to have in guessing the secret word.
  Wordmaker can set their username & specify the secret word.
 
2. Player Versus "Robot":
  Guesser can set their username & the amount of tries they'd like to have in guessing the secret word.
  "The Robot" picks a random word from the MIT 10,000 word list website & attempts to find a matching definition from vocabulary.com.
    If found, it offers the user the ability to use a "hint" by sacrificing half their "tries" at any time.
    
To revisit & revise:
  - Rewrite the program utilizing proper object-oriented etiquette (Classes, constructor methods etc)
  - Implement the "hint" system for Player Versus Player, allowing the Wordmaker to either set their own hint or automatically search for a definition.
  (FIXED IN LATEST COMMIT) Sometimes "hint" definitions scraped from website includes the secret word, so I'd like to implement a simple
                           check for these cases and replace with *'s
  
End goal:
  - Rewrite the program using tkinter libraries to deliver an interactive graphic experience rather than utilizing the terminal.
