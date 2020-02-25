with open('words2.txt','r') as file: 
    
    for line in file:
        
        for word in line.split():
            
            
            letters=list(word)
            a=len(letters)
            
                
            if a>3:
                p = word[1:] + word[0] + "ay"
                print(p)
                
                
                
                

        
            
