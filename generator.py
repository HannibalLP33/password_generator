import string
import random
from itertools import permutations
import pyperclip3 as pc

def password_gen(password_length):
    
    password = []
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    special_char = list("!@#$%^&*()_+-=|;:',./<>?~`")
    
    distribution = []
    password_perm = permutations(list(range(5,password_length)),3)
    
    
    for perm in password_perm:
        if perm[0] + perm[1] + perm[2] == password_length:
            distribution.append(perm)
    chosen_dist = random.choice(distribution)

    # Chose a random letter and append it to the password
    # Shuffle the password for good measure with every appenditure
    for x in range(chosen_dist[0]):
        password.append(random.choice(letters))
        random.shuffle(password)
        
    for y in range(chosen_dist[1]):
        password.append(random.choice(numbers))
        random.shuffle(password)

    for z in range(chosen_dist[2]):
        password.append(random.choice(special_char))
        random.shuffle(password)

    # One last shuffle 
    random.shuffle(password)
    
    # Turn the list into a string
    password = "".join(password)
    
    # Copy password into clipboard
    pc.copy(password)


password_gen(65)