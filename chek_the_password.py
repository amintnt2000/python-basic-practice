def chek_the_password(password:str):
    reason = []
    if len(password) < 8:
        reason.append("Password most have at least 8 character")
    if not any(i.isupper() for i in password):
        reason.append("Password most have at least one Capital letter")
    if not any(i.islower() for i in password):
        reason.append("Password most have at least one lowercase letter")
    if not any(i.isdigit() for i in password):
        reason.append("Password most have at least one number in it")
    if not any(i in "!@#$%^&*()_+?/><,.|:{}[]" for i in password):
        reason.append("Password most have at least one special character")

    if not reason:
        return "strong password"
    else:
        return "Weak password", reason

password = input("Enter the password:")
print(chek_the_password(password))