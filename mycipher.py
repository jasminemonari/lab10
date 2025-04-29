import sys

shift=int(sys.argv[1]) #accepts the integer to shift, index 1 is the argument given

result='' #empty string too append encoded message

for line in sys.stdin:
  line=line.upper() #converts all characters to uppercase

  for char in line:
    if 'A' <= char <= 'Z':  #checks if the character is a letter
      value=ord(char) #gets ASCII value of character
      position = value - ord('A') #makes sure A-Z stays from 0-25
      shifted = (position + shift) % 26 #checks for overflow
      new_char = shifted + ord('A')  #converts new character back to ASCII                                       
      letter=chr(new_char) #gets the new letter by conversion
      result+=letter #apends the new character

for i in range(0, len(result), 5):
    block = result[i:i+5] #index slices the block of input
    print(block, end=' ') #prints block of five letters
    if (i // 5 + 1) % 10 == 0: #checks if the blocks have reached ten per line
        print() #prints a new line if the if statement is proven true

  