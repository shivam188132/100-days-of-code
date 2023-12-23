alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction= input("type 'encode' to encrypt and 'decode' to decrypt \n")
text=input("enter the text you want to do: \n")
shift= int(input("enter the shift amount:  "))

def cesar(start_text, shift_amount, cipher_direction):
    end_text=""
    if direction=="decode":
        shift_amount*=-1
    for word in start_text:
        position=alphabet.index(word)
        new_position= position+ shift_amount
        end_text+=alphabet[new_position]
    print(f"here the {direction}d text is: {end_text} ")
cesar(start_text=text, shift_amount=shift, cipher_direction=direction)        