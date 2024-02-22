import hashlib
import itertools

# Step 1: Gather Password Hashes
# For demonstration purposes, let's assume we have a list of target password hashes
target_hashes = ['5f4dcc3b5aa765d61d8327deb882cf99', '098f6bcd4621d373cade4e832627b4f6']

# Step 2: Implement Brute Force Attack
def brute_force_attack():
    # Define the character set to use for generating combinations (e.g., lowercase letters and digits)
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    # Define the maximum password length to consider (e.g., 4 characters)
    max_length = 4

    # Iterate through all possible password lengths
    for length in range(1, max_length + 1):
        # Generate all combinations of characters of the current length
        for combination in itertools.product(charset, repeat=length):
            # Join the characters to form a password candidate
            password = ''.join(combination)
            # Hash the password using MD5 (you can replace hashlib.md5 with other hashing algorithms)
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            # Check if the hashed password matches any of the target hashes
            if hashed_password in target_hashes:
                print(f'Password found: {password}')
                return password

# Step 3: Implement Dictionary Attack
def dictionary_attack(dictionary):
    # Iterate through each word in the dictionary
    for word in dictionary:
        # Hash the word using MD5
        hashed_word = hashlib.md5(word.encode()).hexdigest()
        # Check if the hashed word matches any of the target hashes
        if hashed_word in target_hashes:
            print(f'Password found in dictionary: {word}')
            return word

# Example usage:
# Brute force attack
brute_force_attack()

# Dictionary attack with a predefined dictionary (replace with your own dictionary file)
dictionary = ['password', '123456', 'qwerty', 'letmein']
dictionary_attack(dictionary)
