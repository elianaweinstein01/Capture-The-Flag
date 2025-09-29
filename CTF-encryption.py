# Eliana Weinstein

# This is teh substitution map I created for the Youtube link. the player will need to find the map
substitution_map = {
    'P':'z', 'h': 'X', 't': 'L', 'p': 'R', 's': 'M', ':': 'Y', '/': 'Q', 'w': 'K', '.': ',',
    'y': 'F', 'o': 'N', 'u': 'B', 'b': 'C', 'e': 'W', 'r': 'A', 'l': 'D', 'n': 'I',
    'T': 'V', 'k': 'O', 'B': 'i', 'Q': 'S', 'c': 'G', 'x': 'U', '-': 'E', 'H': 'H', '8': '7'
}

# Create the reverse map for decryption
reverse_map = {v: k for k, v in substitution_map.items()}

# Function to encrypt the message
def substitution_encrypt(message, substitution_map):
    encrypted_message = []
    for char in message:
        if char in substitution_map:
            encrypted_message.append(substitution_map[char])
        else:
            encrypted_message.append(char)  # Leave unchanged if no substitution exists
    return ''.join(encrypted_message)

# Function to decrypt the message
def substitution_decrypt(encrypted_message, reverse_map):
    decrypted_message = []
    for char in encrypted_message:
        if char in reverse_map:
            decrypted_message.append(reverse_map[char])
        else:
            decrypted_message.append(char)  # Leave unchanged if no substitution exists
    return ''.join(decrypted_message)

# how I encrypted it
message = "https://www.youtube.com/watch?v=TkBPQcy-Hx8"
encrypted_message = substitution_encrypt(message, substitution_map)
print("Encrypted message:", encrypted_message)


# Assuming the player finds the map, they can use this code to decrypt
decrypted_message = substitution_decrypt("XLLRMYQQKKK,FNBLBCW,GNmQKaLGX?v=VOizSGFEHU7", reverse_map)
print("Decrypted message:", decrypted_message)


