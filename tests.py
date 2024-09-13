# https://pythonprinciples.com/challenges/
# Challenge 1
# def capital_indexes(word):
#     letterindices=([i for i, letter in enumerate(word) if letter.isupper()])
#     return letterindices

def capital_indexes(word):
    letterindices=[]
    for i in range(len(word)):
        if word[i].isupper():
            letterindices.append(i)
    return letterindices

#tester code
letters=capital_indexes("HellO TeSTer, I aM mOcKinG yOu")
print(letters)

#Challenge 2
def mid(word):
    n=len(word)
    if n%2==0:
        return ""
    else:
        a=int((n-1)/2)
        return str(word[a])
        
#test code
print(mid("alasar"))
print(mid("aactora"))

#challenge 3
def online_count(statuses):
    m=0
    for i in statuses.values():
        if i=="online":
            m+=1
    return m
        
#test code
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Eloi": "offline",
    "Iana": "offline",
    "Julia": "offline",
    "Nadia": "online"
}
print(online_count(statuses))

#challenge 4
def random_number():
    import random
    return random.randint(1,100)

print(random_number())

#challenge 5
def only_ints(a,b):
    return (type(a)==int and type(b)==int)
    
print(only_ints(2,1))

#challege 6
def double_letters(word):
    for i in range(0,len(word)-1):
        if(word[i]==word[i+1]):
            return True
    return False

print(double_letters("hello"))

#challenge 7
# def add_dots(strng):
#     m=strng
#     for i in range(0,len(m)-1):
#         m=m[:2*i+1]+"."+m[2*i+1:]
#     return m
# def add_dots(s):
#     return ".".join(s)

# def remove_dots(s):
#     return s.replace(".", "")
def add_dots(char):
    n=len(char)
    out=''
    for i in range(n):
        if i==(n-1):  
            out+=char[i]
        else:
            out+=char[i]+'.'
    return out   
print(add_dots("test"))

def remove_dots(strng):
    m= ""
    index = ["."]
    for i in strng:
       if i not in index:
           m+= i
    return m

print(remove_dots("t.e.s.t"))  

#challenge 8
def count(strng):
    m=0
    for i in range(0,len(strng)-1):
        if strng[i]=="-":
            m+=1
    return (m+1)
print(count("ter-min-a-tor"))

#challenge 9
def is_anagram(word1,word2):
    sorted1= ''.join(sorted(word1))
    sorted2= ''.join(sorted(word2))
    return (sorted1==sorted2)

print(is_anagram("python","hyotnep"))
#challenge 10
def flatten(matrix):
    output=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            output.append(matrix[i][j])
    return output

print(flatten([[1, 2], [3, 4],[5,6]]))
                
#challenge 11
def largest_difference(numlist):
    return max(numlist)-min(numlist)

nums=[1, 2, 3,0,8,3,155,23,5,-8]
print(largest_difference(nums))

#challenge 12
def div_3(n):
    return n%3==0

#challenge 13
def get_row_col(pos):
    poslist=[]
    # row
    poslist.append(int(pos[1])-1)
    r=pos[0]
    if r=="A":
        r1=0
    elif r=="B":
        r1=1
    elif r=="C":
        r1=2
    poslist.append(r1)
    # column
    return tuple(poslist)
    
print(get_row_col("A3"))

# challenge 14
def palindrome(word):
    m=0
    for i in range(len(word)):
        if word[i]!=word[len(word)-i-1]:
            m+=1
    if m==0:
        return True
    else: return False
    
print(palindrome("aba"))

# challenge 15
def up_down(num):
    return tuple([num-1,num+1])

# challenge 16
def consecutive_zeros(binum):
    m=0
    n=0
    for i in range(len(binum)):
        if binum[i]=="1":
            m=0
        if binum[i]=="0":
            m+=1
            if m>n:
               n=m
    return n
    
print(consecutive_zeros("10011010001100100010"))

# challenge 17
def all_equal(numlist):
    m=0
    for i in range(len(numlist)):
        if numlist[i]!=numlist[0]:
            m+=1
    if m==0: 
        return True
    else: 
        return False
    
        
print(all_equal([1, 1,1,1,1,1]))

# challenge 18
def triple_and(boo1,boo2,boo3):
    if (boo1==False or boo2==False or boo3==False):
        return False
    return True

# challenge 19

def convert(numlist): 
    return [str(numlist[i]) for i in range(len(numlist))]

# challenge 20
def zap(a,b):
    output=[]
    for i in range(len(a)):
        tuplelist=tuple([a[i],b[i]])
        output.append(tuplelist)
    return output

# challenge 21

def validate(code):
    if "def" not in code:
        return "missing def"
    elif ":" not in code:
        return "missing :"
    elif "(" and ")" not in code:
        return "missing paren"
    elif code.index("(")==(code.index(")")-1):
        return "missing param"
    elif "   " not in code:
        return "missing indent"
    elif "validate" not in code:
        return "wrong name"
    elif "return" not in code:
        return "missing return"
    return True
    
# challenge 22
def list_xor(n,list1,list2):
    in_1=(n in list1)
    in_2=(n in list2)
    return (in_1 or in_2) and not(in_1 and in_2)
# challenge 23

def param_count(*num):
    numlist=num
    return len(numlist)

# challenge 24
# def format_number(num):
#     if num<0:
#         raise Exception("no numbers below zero")
#     m=str(num)
#     for i in range(1,(len(m)-1)//3+1):
#         m=m[0:(len(m)+1-4*i)]+","+m[(len(m)+1-4*i):len(m)]
#     return m

def format_number(num):
    if num<0:
        raise Exception("no numbers below zero")
    m=str(num)[::-1]
    out=''
    for i in range(len(m)):
        if (i+1)%3==0:
            out+=m[i]+','
        else:
            out+=m[i]
    return out[::-1]

def format_number2(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]
    
print(format_number(10000000000))
print(format_number2(10000000000))
#  challenge 25

def find_all_factors(num):
    if num<1:
        return []
    else:
        return [i for i in range(1,num+1) if num%i==0]
    

print(find_all_factors(8))

# challenge 26

topics = ["System Architecture",
          "Memory and Storage",
          "Computer Networks",
          "Network Security",
          "Systems Software",
          "Ethical, Legal, Cultural & environmental Impacts of digital technology",
          "Algorithms",
          "Programming Fundamentals",
          "Producing Robust Programs",
          "Boolean Logic",
          "Programming Languages and IDEs"]

# complete the code here...

def progress_tracker(topics):
    n=len(topics)
    revision_score=0
    for topic in topics:
        revised=input("Did you complete your revision on "+topic+"? (Yes or No)")
        if revised=='Yes':
            revision_score+=1
        else: continue
    percentage=100 * revision_score/n
    print('Your revision score:'+str(percentage)+'%')

# progress_tracker(topics) 