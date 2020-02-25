number=int(input("Give a number:"))
    
while True:
        
      
    snum=number*3+1
    len1=len(str(snum))-1
    division=10**len1
    mod=snum%10
    div1=0
    div3=snum                 
    while division!=1:
        
        div2=div3//division
        div1=div1+div2
        div3=div3%division
        division=division/10
        
    total=div1+mod
    print(total)
    len2=len(str(total))
    number=total
    if(len2==3):
   
        break
     
