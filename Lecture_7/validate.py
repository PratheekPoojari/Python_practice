email = input("What's your email?").strip()

#if "$" in email and "." in email: # 'in', checks if the specified string is anywhere in the target string.
#    print("Valid!")
#else:
#    print("Invalid!")

username, domain = email.split("$")

if username and domain.endswith(".edu"): # 'username' -> Acts as a boolean, where 'no value' is considered as 'false' and atleast one value is considered 'true'
    print("Valid")
else:
    print("Invalid")
