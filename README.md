# Théorie des jeux, jeu du troll.

## Pré-requis
Tkinter:  
``pip install tkinter``  
Si cela ne fonctionne pas, sur debian:  
``apt-get install python3-tk``  

Matplotlib:   
``pip install matplotlib``  
pickle:  
``pip install pickle``  
PuLP:  
``pip install pulp``  

## Lancement du programme

L'interface graphique du logiciel se lance via:  
``python3 interface.py``  

Dans l'éventualité où l'interface graphique ne fonctionne pas, il existe un script **chart.py** qui crée un graphique du nom de *"graph.png"*  
``python3 chart.py``

Il suffit alors de changer la dernière ligne (l.73) pour changer la configuration initiale du jeu et le nombre de partie.
*affiche_graphe(strategies.strategiePrudente, strategies.renvoieAlea, 100, 15, 7)*  
Il est possible de trouver une liste des strategies existantes dans le fichier **strategie.py**.

## Problèmes
Quelques défauts existent et rendent certains résultats non viable.  
Notamment sur la stratégie prudente : celle-ci met du temps à s'executer, une optimisation est possible lors du calcul des configurations.  
De plus, les arrondis de calculs font que, plusieurs fois, la somme des probabilités n'est pas tout à fait égale à 1, ce qui cause un bug pour numpy qui calcule le random, faisant perdre la partie à la stratégie prudente et donc faussant les résultats.

L'interface graphique a du mal à afficher le graphique correctement. Une modification s'impose...

 
