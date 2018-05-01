# Objectifs
- Implémenter la stratégie prudente  
- Implémenter une ou plusieurs stratégie personnalisées  
- Créer une interface graphique permettant l'affichage de résultats de stratégie.  

# Installation de Pygame
 Sur Windows :  
``python3 -m pip install pygame``

Sur Unix :  
``pip install pygame``


# Git Workflow 


* **Starting a new task :**


    For the task n°XXX  
    git checkout master  
    git pull origin master *(get the latest code from the remote)*  
    git checkout -b task/XXX *(or fix/XXX if it is a bug correction)*  



* **Task ending :**


    git add . *(in order to add all the modified files to the next commit)*  
    git commit -m "Commit message"   
    git checkout master *(So you come back to the local master)*   
    git pull origin master *(then you pull changes from origin into your local master)*  
    git checkout task/XXX *(you go back to you branch)*   
    git rebase master *(it merges the code on master on your new code)*  
    *-> Now Git might tell you that there is a conflit and you should fix it. All you have to do is to the file where the conflit happened, fix it and type ``git add . && git rebase --continue``* 
    *-> run all the unit tests of the project and test if what you've done is 100% OK.*  
    git push origin task/XXX *(push your branch in GitHub so it can be peer-reviewed)*  
    



* **After your task is accepted by peers :**


    git checkout master *(go to master)*  
    git pull origin master *(pull the lastest changes)*  
    git checkout task/XXX *(go back to your branch)*  
    git rebase master *(apply the changes and fix conflict if any)*  
    git checkout master *(go back to master)*  
    git merge --no-ff task/XXX *(this merge your branch into your local master)*     
    git push origin master *(et Voila!)*  
    


* **Deleting branches (TBD) :**


    git branch -D task/XXX *(delete the local branch)*  
    git push origin --delete task/XXX *(delete the distant branch)*  


* **In case of an error from git when you push at the end of a task :**

   
    git push origin --delete task/XXX *(delete the distant branch)*  
    git push origin task/XXX *(then reupload it)*  