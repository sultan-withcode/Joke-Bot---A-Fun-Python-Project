# Joke Bot Repository Code Setup

# Constants
PROMPT = "Aap kya chahte hain? "
JOKE = "Yeh raha aapke liye ek joke: Ek programmer apni dost se kehta hai: 'Jab tum grocery store jao, ek liter doodh le aana, aur agar anday hon to 12 le aana.' Dost 13 liter doodh le aayi. Programmer ne poocha kyun? Dost ne jawab diya: 'Kyunki anday thay.'"
SORRY = "Maaf kijiyega, main sirf jokes sunata hoon."

# Import random module for enhancements (if needed later)
import random

# Function to run the Joke Bot
def joke_bot():
    # Taking input from the user
    user_input = input(PROMPT)

    # Responding based on user input
    if user_input.lower() == "joke":
        print(JOKE)
    else:
        print(SORRY)

# Run the bot
if __name__ == "__main__":
    joke_bot()
