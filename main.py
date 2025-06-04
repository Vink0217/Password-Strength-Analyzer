import math
import hashlib
import requests

def calculate_entropy(password):
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special_char = False

    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in '!@#$%^&*()-_+=<>':
            has_special_char = True

    character_size = 0
    if has_lowercase:
        character_size += 26
    if has_uppercase:
        character_size += 26
    if has_digit:
        character_size += 10
    if has_special_char:
        character_size += 32 

    if character_size == 0:
        return 0

    return len(password) * math.log2(character_size)

def check_password_breach(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    hash_list = (line.split(":") for line in response.text.splitlines())

    for hash_suffix, count in hash_list:
        if hash_suffix == suffix:
            return int(count)
    return 0

password = input("Enter Password: ")

has_uppercase = False
has_digit = False
has_special_char = False

for char in password:
    if char.isupper():
        has_uppercase = True
    if char.isdigit():
        has_digit = True
    if char in '!@#$%^&*()-_+=<>':
        has_special_char = True

rule_score = 0
if has_uppercase:
    rule_score += 1
if has_digit:
    rule_score += 1
if has_special_char:
    rule_score += 1


entropy = calculate_entropy(password)
print(f"Estimated Entropy: {entropy:.2f}")

if entropy < 28:
    entropy_score = 0
elif entropy < 36:
    entropy_score = 1
elif entropy < 60:
    entropy_score = 2
else:
    entropy_score = 3

total_score = (0.4 * rule_score) + (0.6 * entropy_score)


if total_score < 1:
    print("Overall Password Strength: Very Weak")
elif total_score < 2:
    print("Overall Password Strength: Weak")
elif total_score < 2.5:
    print("Overall Password Strength: Moderate")
elif total_score < 3:
    print("Overall Password Strength: Strong")
else:
    print("Overall Password Strength: Very Strong")

try:
    breach_count = check_password_breach(password)
    if breach_count:
        print(f"This password was found in {breach_count} data breaches!")
    else:
        print("This password has not been found in known breaches.")
except:
    print("Could not check password breaches (offline or error).")
