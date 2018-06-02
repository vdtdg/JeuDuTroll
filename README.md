# Théorie des jeux, jeu du troll.

## Pré-requis
Tkinter:  
``pip install tkinter``  
Si cela ne fonctionne pas, sur debian:  
``sudo apt-get install python3-tk``    
Attention, je crois que tkinter ne fonctionne pas sur les environnements virtuels python.  

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

## Changer la liste de stratégies
Les stratégies sont definies dans le fichier strategies.py selon les specifications du projet Troll.  
Pour ajouter des stratégies, il suffit d'ajouter le nom de sa stratégie et la fonction associée dans le fichier strategies.py dans le dict de la fonction ``switch_strategie`` du fichier **interface.py**.  
Il faut aussi ajouter le nom de la stratégie dans le tableau ``liste_strategie`` à la ligne 54 du fichier **interface.py**.


## Problèmes
Quelques défauts existent et rendent certains résultats non viable.  
Notamment sur la stratégie prudente : les arrondis de calculs font que, plusieurs fois, la somme des probabilités n'est pas tout à fait égale à 1, ce qui cause un bug pour numpy qui calcule le random, faisant perdre la partie à la stratégie prudente et donc faussant les résultats.  
Néanmoins, cela arrive assez peu souvent (<5%)  


 
