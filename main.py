alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  final_text = ""
  if direction == "decode":
    shift *= -1
  for letter in text:
    for char in alphabet:
      if letter == char:    
        position = alphabet.index(char) + shift
        
        # when reaching end of the list
        if position >= 26:
          new_position = position - 26
          final_text += alphabet[new_position]
          break
        
        # when the letter is a and need to decode
        elif position < 0:
          new_position = 26 + position
          final_text += alphabet[new_position] 
          break
        else:
          final_text += alphabet[position] 
          break
  print(f"Here's the {direction}d result: {final_text}")
  

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
 
user_wants_to_rerun_caesar = True
while user_wants_to_rerun_caesar == True:
  user_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  user_text = input("Type your message:\n").lower()
  user_shift = int(input("Type the shift number:\n"))

  # if a user enters a shift larger than 26
  if user_shift > 26:
    shift = user_shift % 26
    print(f"shift: {shift}")
  
  caesar(user_text, user_shift, user_direction)
  user_input = input("Do you want to run Caesar again? Y or N\n").lower()
  user_wants_to_rerun_caesar = False if user_input == "n" else True