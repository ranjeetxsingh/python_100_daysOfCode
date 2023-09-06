alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



n = len(alphabet)
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.



# def encrypt(text, shift):
#   cipher_text = ""
#   for letter in text:
#     position = alphabet.index(letter)
#     new_position = position + shift
#     if new_position >= n:
#       new_position = new_position - n
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The encoded text is {cipher_text}")


# def decrypt(text, shift):
#   decipher_text = ""
#   for letter in text:
#     position = alphabet.index(letter)
#     new_position = position - shift
#     new_letter = alphabet[new_position]
#     decipher_text += new_letter
#   print(f"The decoded text is {decipher_text}")
    

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# encrypt(text, shift)
# decrypt(text, shift) 
# if direction == 'encode':
#   encrypt(text, shift)
# elif direction == 'decode':
#   decrypt(text, shift)
# else:
#   print("Invalid input")

keep_going = True

def caeser(text, shift):
  output_text = ""
  shift = shift % 26
  if direction=='decode':
      shift = -1 * shift
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = (position + shift)%26
      output_text += alphabet[new_position]
    else:
      output_text += char
  print(f"The {direction}d text is {output_text}")
  
while keep_going:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caeser(text, shift)
  user_input = input("Type 'yes' if you want to again.otherwise type 'no'. \n").lower()
  if user_input=='no':
    keep_going = False
    print("Good bye")