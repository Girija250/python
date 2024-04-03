vcount = 0;  
ccount = 0;  
str = "This is a really simple sentence";  
str = str.lower();  
for i in range(0,len(str)):   
    if str[i] in ('a',"e","i","o","u"):  
        vcount = vcount + 1;  
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        ccount = ccount + 1;  
print("Total number of vowel and consonant are" );  
print(vcount);  
print(ccount);  
