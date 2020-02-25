with open('words.txt','r') as file: 
    
    for line in file:
        
        badconsonants = 0
        consonants = 0
        
        for word in line.split():
            
            
            letters=list(word)
            
        
            for i in letters:
                
                if(i == 'f' or i == 'c' or i == 'k' or i == 'r'):  
                    badconsonants = badconsonants + 1
                
                elif(i=='b' or i=='d' or i=='g' or i=='h' or i=='j' or i=='l' or i=='m'or i=='n' or i=='p' or i=='q' or i=='s' or i=='t' or i=='v' or i=='w' or i=='x' or i=='y' or i=='z'):
                    consonants = consonants + 1
                
            if badconsonants>consonants:
                
            
               print(word,"κακη")
            else:
               print(word,"καλή")
