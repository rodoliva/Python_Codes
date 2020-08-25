import re

patternemail = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
patternpass = r"[a-zA-Z0-9#$%&.,]"
def checkemail(email):
    if (re.search(patternemail, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

def checkpass(password):
    if len(password) <= 10 :
        if (re.search(patternpass, password)):
            print("Valid pass")
        else:
            print("Invalid pass")
    else:
        print("Invalid pass")

if __name__ == '__main__':
    email = "www.4444.333m@gtestmail.com"
    checkemail(email)
    password='xW61h0n.hs'
    checkpass(password)
