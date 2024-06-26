import re
def mask_email(email):
    parts = email.split("@")
    username = parts[0]
    domain = parts[1]
    masked_username = username[0] + "*******" + username[1]
    masked_email = masked_username + "@" + domain
    return masked_email

#Usage
email1 = "example@email.com"
email2 = "john.doe@email.com"
masked_email1 = mask_email(email1)
masked_email2 = mask_email(email2)
your_email = input("What is your  email?")
your_masked_email = mask_email(your_email)


print(masked_email1)
print(masked_email2)
print("Your masked email is: " + your_masked_email)
