maximl = 256

def maxdc(str, n): 
  
   
    count = [0] * maximl 
      
    for i in range(n): 
        count[ord(str[i])] += 1
      
    jey = 0
    for i in range(maximl): 
        if (count[i] != 0): 
            jey += 1    
      
    return jey 
  
def smdc(str): 
  
    n = len(str)     
  

    jey = maxdc(str, n) 
    minl = n      
      
 
    for i in range(n): 
        for j in range(n): 
            subs = str[i:j] 
            subs_lenght = len(subs) 
            subdc = maxdc(subs,subs_lenght) 
              
 
            if (subs_lenght < minl and 
                jey == subdc): 
                minl = subs_lenght 
  
    return minl 
  
 
if __name__ == "__main__": 
      
    str1 = str (input("enter lower case string: "))
    l = smdc(str1)
    print( "The length of the smallest substring",l) 