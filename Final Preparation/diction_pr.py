def count_frequrency_letter(input_string):
    letter_frequency={}
    for charact in input_string:
       
        if charact.isalpha():
             char_lower=charact.lower()
             
             if char_lower in letter_frequency:
               letter_frequency[char_lower]+=1
             else:
               letter_frequency[char_lower]=1
               
    return letter_frequency
result=count_frequrency_letter("Hello World")
print(result)
        
        
def stringcheck(instring):
    if len(instring)!=0:
        return len(instring)
    else:
        return 0
    
z=stringcheck("Hello")
print(z)
mydata="Hello guys"
print(len(mydata))