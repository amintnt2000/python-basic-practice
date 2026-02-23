def password_checker(password:str):
    score = 0

    if len(password) > 8:
        score+=1
    if any(c.islower() for c in password):
        score+=1
    if any(c.isupper() for c in password):
        score+=1
    if any(c.isdigit() for c in password):
        score+=1
    if any(c in "@!?#$%^&*()_+=[]{}:;,.<>?|" for c in password):
        score+=1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

pwd = input('Enter your password :')
print(password_checker(pwd))

