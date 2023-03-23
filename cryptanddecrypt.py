#PROJETS NGUETTA NANA - CRYPTAGE ET DECRYPTAGE DE MESSAGE



import re



class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None

    def __str__(self):
        return str(self.data)
    
    
    
#Code d'insertion du noeud gauche 
    def inserer_fils_gauche(self,valeur):
        if self.left == None:
            self.left = Node(valeur)
        else:
            nouveau_noeud = Node(valeur)
            nouveau_noeud.left = self.left
            self.left = nouveau_noeud
            
#Code d'insertion du noeud droit
    def inserer_fils_droit(self, valeur):
        if self.right == None:
            self.right = Node(valeur)
        else:
            nouveau_noeud = Node(valeur)
            nouveau_noeud.right = self.right
            self.right = nouveau_noeud
                
                
    
    def afficher(self, level=0):
        if self.right:
            self.right.afficher(level + 1)
        print(f"{' ' * 4 * level}{self.data}")
        if self.left:
            self.left.afficher(level + 1)
                


                
def dechiffrage(noeud,val_code):
    
    
    if noeud and val_code is None :
    
        return 
    
    copyracine=noeud
    
    mot =""
    i =0
    
    
    
    
    while(i<len(val_code)):        
        
        x=val_code[i]
        
        if x=='0':
            noeud=noeud.left
            
            
            if noeud.left  and noeud.right != None:
            
               compteur=+1
            else:

                 mot+=noeud.data
                 noeud=copyracine
                
        
        if x=='1':
            noeud=noeud.right
            if noeud.left  and noeud.right != None:
                
                compteur=+1
            else:
                 mot+=noeud.data
                 noeud=copyracine


         
                 
        i+=1
        
        

       
    mot=re.sub('-', '', mot)             
    print("Phrase: "+mot)
    




def chiffrage(noeud,phrase):
    
            
    # Sous arbre gauche
    noeudpri=noeud
    noeudsav=noeudpri
    cod=''
   
    for x in phrase:
        
        
        
         noeudpri=noeud.left
         cod+='0'
         while(noeudpri!=None and noeudpri.left!=None ):
             if noeudpri.left.left.data==x:
                 cod+='00'
                 noeudpri=noeudsav
                 break
                 
             if noeudpri.left.right.data==x:
                 cod+='01'
                 noeudpri=noeudsav
                 break
                 
             noeudpri=noeudpri.right
             cod+='1'
             
   
                   
             
         noeudpri=noeudsav
        
         if x in ('A','O','E','I','U',' ','0','1','2','3','4','5','6','7','8','9'):
             continue
         
         noeudpri=noeud.right
         cod+='1'
         
         while(noeudpri!=None and noeudpri.right!=None ):
             if noeudpri.left.left.data==x:
                 cod+='00'
                 noeudpri=noeudsav
                 break
                 
             if noeudpri.left.right.data==x:
                 cod+='01'
                 noeudpri=noeudsav
                 break
                 
             noeudpri=noeudpri.right
             cod+='1'
             
       
    print(cod)
         
         
         
def verification(noeud,message):
      
         
         if noeud == None:
             return
             
         if noeud!= None:
             if noeud.data  in message:
                 print(noeud.data)
             
             verification(noeud.left,message)
             
             verification(noeud.right,message)   
    
        
                 
        
                
                
                
                
                
                
                
                
racine = Node('-')

racine.inserer_fils_gauche('-')



racine.left.inserer_fils_droit('-')
racine.left.inserer_fils_gauche('-')





racine.left.left.inserer_fils_gauche('A')
racine.left.left.inserer_fils_droit('E')

racine.left.right.inserer_fils_gauche('-')
racine.left.right.left.inserer_fils_gauche('I')
racine.left.right.left.inserer_fils_droit('O')

racine.left.right.inserer_fils_droit('9')
racine.left.right.inserer_fils_droit('-')


racine.left.right.right.inserer_fils_droit('-')
racine.left.right.right.inserer_fils_gauche('-')
racine.left.right.right.left.inserer_fils_gauche('U')
racine.left.right.right.left.inserer_fils_droit(' ')


racine.left.right.right.right.inserer_fils_droit('-')
racine.left.right.right.right.inserer_fils_gauche('-')
racine.left.right.right.right.left.inserer_fils_gauche('0')
racine.left.right.right.right.left.inserer_fils_droit('1')

racine.left.right.right.right.right.inserer_fils_droit('-')
racine.left.right.right.right.right.inserer_fils_gauche('-')
racine.left.right.right.right.right.left.inserer_fils_gauche('2')
racine.left.right.right.right.right.left.inserer_fils_droit('3')

racine.left.right.right.right.right.right.inserer_fils_droit('-')
racine.left.right.right.right.right.right.inserer_fils_gauche('-')
racine.left.right.right.right.right.right.left.inserer_fils_gauche('4')
racine.left.right.right.right.right.right.left.inserer_fils_droit('5')

racine.left.right.right.right.right.right.right.inserer_fils_droit('-')
racine.left.right.right.right.right.right.right.inserer_fils_gauche('-')
racine.left.right.right.right.right.right.right.left.inserer_fils_gauche('6')
racine.left.right.right.right.right.right.right.left.inserer_fils_droit('7')

racine.left.right.right.right.right.right.right.right.inserer_fils_droit('-')
racine.left.right.right.right.right.right.right.right.inserer_fils_gauche('-')
racine.left.right.right.right.right.right.right.right.left.inserer_fils_gauche('8')
racine.left.right.right.right.right.right.right.right.left.inserer_fils_droit('9')




racine.inserer_fils_droit('-')

racine.right.inserer_fils_droit('-')

racine.right.right.inserer_fils_droit('-')
racine.right.right.inserer_fils_gauche('-')
racine.right.right.left.inserer_fils_gauche('D')
racine.right.right.left.inserer_fils_droit('F')

racine.right.right.right.inserer_fils_droit('-')
racine.right.right.right.inserer_fils_gauche('-')
racine.right.right.right.left.inserer_fils_gauche('G')
racine.right.right.right.left.inserer_fils_droit('H')

racine.right.right.right.right.inserer_fils_droit('-')
racine.right.right.right.right.inserer_fils_gauche('-')
racine.right.right.right.right.left.inserer_fils_gauche('J')
racine.right.right.right.right.left.inserer_fils_droit('K')

racine.right.right.right.right.right.inserer_fils_droit('-')
racine.right.right.right.right.right.inserer_fils_gauche('-')
racine.right.right.right.right.right.left.inserer_fils_gauche('M')
racine.right.right.right.right.right.left.inserer_fils_droit('N')

racine.right.right.right.right.right.right.inserer_fils_droit('-')
racine.right.right.right.right.right.right.inserer_fils_gauche('-')
racine.right.right.right.right.right.right.left.inserer_fils_gauche('P')
racine.right.right.right.right.right.right.left.inserer_fils_droit('Q')


racine.right.right.right.right.right.right.right.inserer_fils_droit('-')
racine.right.right.right.right.right.right.right.inserer_fils_gauche('-')
racine.right.right.right.right.right.right.right.left.inserer_fils_gauche('R')
racine.right.right.right.right.right.right.right.left.inserer_fils_droit('S')

racine.right.right.right.right.right.right.right.right.inserer_fils_droit('-')
racine.right.right.right.right.right.right.right.right.inserer_fils_gauche('-')
racine.right.right.right.right.right.right.right.right.left.inserer_fils_gauche('T')
racine.right.right.right.right.right.right.right.right.left.inserer_fils_droit('V')

racine.right.right.right.right.right.right.right.right.right.inserer_fils_droit('-')
racine.right.right.right.right.right.right.right.right.right.inserer_fils_gauche('-')
racine.right.right.right.right.right.right.right.right.right.left.inserer_fils_gauche('W')
racine.right.right.right.right.right.right.right.right.right.left.inserer_fils_droit('X')


racine.right.right.right.right.right.right.right.right.right.right.inserer_fils_droit('-')
racine.right.right.right.right.right.right.right.right.right.right.inserer_fils_gauche('-')
racine.right.right.right.right.right.right.right.right.right.right.left.inserer_fils_droit('Z')
racine.right.right.right.right.right.right.right.right.right.right.left.inserer_fils_gauche('Y')




racine.right.inserer_fils_gauche('-')
racine.right.left.inserer_fils_gauche('C')
racine.right.left.inserer_fils_droit('B')
#11001111111000110111110100011001111000101
#print("Saisir votre Message")
#message =input()


#dechiffrage(racine,"0111111111111111111000000101011010111111111111100000011111111111110101111111111100001")

#racine.afficher()
#verification(racine,"AETRI")













chiffrage(racine,"CACAO")
