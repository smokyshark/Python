def username_generator(first_name, last_name):
  if len(last_name) < 4: 
    return first_name[:3] + last_name
  else: return first_name[:3] + last_name[:4]

def password_generator(user_name):
  password = ""
  for i in range(len(user_name)):
    password += user_name[i-1]
  return password

first_name = "Abe"
last_name = "Simpson"
user_name = username_generator(first_name, last_name)
print(user_name)
password = password_generator(user_name)
print(password)
first_name = "Zoe"
last_name = "Lee"
user_name = username_generator(first_name, last_name)
print(user_name)
password = password_generator(user_name)
print(password)