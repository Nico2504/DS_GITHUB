# -*- coding: utf-8 -*-

import socket
UDP_IP="192.168.0.202"#adresse IP du serveur
UDP_PORT= 5005#port UDP

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(1.0)#délai d'une seconde

sock.connect((UDP_IP,UDP_PORT))#connexion au serveur UDP
sock.send("cinema")#envoie du message au serveur UDP

trameReponse, addr = sock.recvfrom(1024)#ligne de décodage des trames

print "Réception de la trame de réponse", trameReponse.encode("hex")#afficher trame reponse en hexadecimal

b3= ord(trameReponse[3])<<24#decalage de bit
b2= ord(trameReponse[2])<<16#decalage de bit
b1= ord(trameReponse[1])<<8#decalage de bit
b0= ord(trameReponse[0])<<0#decalage de bit


code = b0|b1|b2|b3#addition du code

print code#afficher code 

