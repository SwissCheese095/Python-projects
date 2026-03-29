def caeser_encrypt(text, shift):
  encryption = ""
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for letter in text:
    if letter in alphabet:
      letter_index = alphabet.index(letter)
      new_index = (letter_index + shift) % 26
      encryption += alphabet[new_index]
    else:
      encryption += letter
  return encryption
def caeser_decrypt(encryption,shift):
  decryption = ""
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for letter in encryption:
    if letter in alphabet:
      letter_index = alphabet.index(letter)
      new_index = (letter_index - shift) % 26
      decryption += alphabet[new_index]
    else:
      decryption += letter
  return decryption
text = input("Enter text: ")
shift = int(input("Enter shift: "))
result = caeser_encrypt(text, shift)
print("Encrypted text: " + result)
print("Decrypted text: " + caeser_decrypt(result, shift))