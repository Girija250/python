str1 = "Grab";  
str2 = "Brag";   

if(len(str1)!= len(str2)):  
    print ("Both the strings are not anagram");  
else:  
    
    str1 = str1.lower();  
    str2 = str2.lower();  
     
    str1 = ''. join(sorted(str1));  
    str2 = ''. join(sorted(str2));  
      
    if (str1 == str2):  
        print ("Both the strings are anagram");   
    else:  
        print ("Both the strings are not anagram");  
