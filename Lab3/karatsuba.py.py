def Multiply_integer(a,b):
    a_string=str(a)
    b_string=str(b)
    result=str(a*b)
    return result

def Multiply_string(a,b):
    result=str(int(a)*int(b))
    return result


def Multiply_Recursive(a,b):
    if len(a)==1 or len(b)==1:
        return str(int(a)*int(b))
    
    mid=min(len(a),len(b))//2
    a_High,a_Low=a[:-mid],a[-mid:]
    b_High,b_Low=b[:-mid],b[-mid:]
    
    k1=Karatsuba_Recursive(a_High,b_High)
    k2=Karatsuba_Recursive(a_Low,b_Low)
    k3=Karatsuba_Recursive(str(int(a_High)+int(a_Low)),str(int(b_High)+int(b_Low)))
    
    result=str(int(k1)*10**(2*mid)+(int(k3)-int(k1)-int(k2))*10**mid+int(k2))
    return result

def Visualize_Karatsuba(a,b,indent=""):
    if len(a)==1 or len(b)==1:
        product=int(a)*int(b)
        print(indent + a + " *"+b + "=" + str(product))
        return
    mid=min(len(a),len(b))//2
    a_High,a_Low=a[:-mid],a[-mid:]
    b_High,b_Low=b[:-mid],b[-mid:]

    print(indent + a_High +" "+a_Low)
    print(indent + b_High + " "+b_Low)

    Visualize_Karatsuba(a_High,b_High,indent + " "+ mid)
    Visualize_Karatsuba(a_Low,b_Low,indent + " "+ mid)

    k1=str(int(a_High)* int (b_High))
    k2=str(int(a_Low)*int(b_Low))
    k3=str(int(a_High + a_Low)* int ( b_High + b_Low) - int(k1) - int(k2))

    print(indent + "-" *(2*mid))
    print(indent + k1 + " "*mid + k2)
    print(indent + "-" *(2*mid))
    print(indent + k3)
    print(indent + "-" * (2*mid))

    result=str(int(k1) * 10**(2*mid) + int(k3) * 10**mid + int(k2))
    print(indent + result) 
def Karatsuba_Recursive(a,b):
    if len(a)==1 or len(b)==1:
        return str(int(a)*int(b))
    mid=min(len(a),len(b))//2
    a_High, a_Low=a[:-mid], a[-mid:]
    b_High, b_Low=b[:-mid], b[-mid:]

    k1=Karatsuba_Recursive(a_High,b_High)
    k2=Karatsuba_Recursive(a_Low,b_Low)
    k3=Karatsuba_Recursive(str(int(a_High)+int(a_Low)),str(int(b_High)+int(b_Low)))

    result=str(int(k1)*10**(2*mid)+(int(k3)-int(k1)-int(k2))*10**mid+int(k2))
    return result

def Multiply2(x,y):
    try:
        if not all(bit in '01' for bit in x) or not all(bit in '01' for bit in y):
            return ""
        result=bin(int(x,2)* int(y,2))[2:]
        return result
    except ValueError:
        return ""
    
def Multiply16(x,y):
    try:
        if not all(char in '0123456789ABCDEF' for char in x.upper()) or not all(char in '0123456789ABCDEF' for char in y.upper()):
            return ""
        result =hex(int(x,16) * int(y,16))[2:]
        return result
    except ValueError:
        return ""
    

print("Enter binary digits for multiplication:")
value1=input("Enter first value")
value2=input("Enter second value")
check=Multiply2(value1,value2)
print(check)

print("Enter hexadecimal digits for multiplication:")
value11=input("Enter first value")
value22=input("Enter second value")
check1=Multiply16(value1,value2)
print(check1)

# usage of Visualize_Karatsuba
a="22"
b="45"
print("Visualizing Karatsuba Multiplication:")
Visualize_Karatsuba(a,b)

    