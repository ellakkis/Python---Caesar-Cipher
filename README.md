## Python---Caesar-Cipher

A program were you can use it as if you are sending secret messaged to your friend or love! 

# Program execution

- Program will ask you to chose to encode or decode
- Program will ask you to enter your message (only text for now)
- Program will ask you what shift you like to apply (shift is a number)
- Program will display the decoded/encoded message for you
- Program will ask you if you like to run the program again

# How it works

Let's assume you asked to encode 'hello' with shift '5':
Program will take the first letter from your word 'h' and try to match it with an item from a list of the alphabets. 
If found, it will take its position index and add the shift and then take the letter in the alphabet that is in the new position.
So 7 + 5 = 12 => new letter will be at position 12 in the alphabet list: 'm' and so on.

# 🐛Bug alert:🐛
What happens if you try to encode the word 'civilization'?
The solution for this bug has been incorporated here already
hint: go round and round the list!!


# TODO: What happens if the user enters a number/symbol/space?

#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?

#e.g. start_text = "meet me at 3"

#end_text = "•••• •• •• 3"

    


# Solution

Check file main.py
