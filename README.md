# Objectifs
- Implémenter la stratégie prudente  
- Implémenter une ou plusieurs stratégie personnalisées  
- Créer une interface graphique permettant l'affichage de résultats de stratégie.  

# Installation de Pygame
 Sur Windows :  
``python3 -m pip install pygame``

Sur Unix :  
``pip install pygame``

# Ressources
Tuto ligne par ligne d'un jeu basique sur Pygame :  
https://www.pygame.org/docs/tut/ChimpLineByLine.html  

Tuto Open Classroom pour Pygame :  
https://openclassrooms.com/courses/interface-graphique-pygame-pour-python  
   
   
# Git Workflow 

Pour bien fonctionner ensemble sur Git :  
On travaillera uniquement sur la branche master, dans un soucis de simplicité.
Pour ne pas avoir de conflit et casser le répo, nous allons utiliser le workflow suivant :  
 * Lors du commit, ne pas oublier de mettre le numéro de la tâche en cours :  
 *git commit -m "task#42 ..."*  

 * Avant de push son code :  
 *git pull origin master --rebase*  

 * Une fois le rebase effectué :  
 *git push origin master*  

