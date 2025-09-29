# Eliana Weinstein
# HASHING
# PLayer will use the ip addresses in the hash algorithm which shifts each letter by the corresponding digit

def scramble_message(message, big_number):
    # Convert the big number to a list of its digits
    shifts = [int(digit) for digit in str(big_number)]

    scrambled_message = []
    for i, char in enumerate(message):
        # Calculate the shift based on the corresponding digit in the number
        shift = shifts[i % len(shifts)]

        # Shift the ASCII value of the character by the shift value
        scrambled_char = chr(ord(char) + shift)
        scrambled_message.append(scrambled_char)

    return ''.join(scrambled_message)


# How i got the hashed message
message = "https://imgur.com/a/MxmN7z6"
big_number = 7578756875787568376936103778
scrambled = scramble_message(message, big_number)
print("Scrambled Message:", scrambled)


# this is the code user will need to write, based on the hint I provided

def dehash_message(scrambled_message, big_number):
    # Convert the big number to a list of its digits
    shifts = [int(digit) for digit in str(big_number)]

    original_message = []
    for i, char in enumerate(scrambled_message):
        # Calculate the shift based on the corresponding digit in the number
        shift = shifts[i % len(shifts)]

        # Reverse the shift by subtracting the shift value from the character
        original_char = chr(ord(char) - shift)
        original_message.append(original_char)

    return ''.join(original_message)


# Example usage
# provided by me
scrambled_message = "oy{xz?57prn}y3iwp6g8P~nN:="
# found by user in DNS enumeration
big_number = 7578756875787568376936103778
original = dehash_message(scrambled_message, big_number)
print("Original Message:", original)