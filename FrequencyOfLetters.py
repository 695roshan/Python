#to print the frequency of letters of a string in descending order
dict={}
list=[]
def most_frequent(st):
    for i in st:   
        dict[i]=st.count(i)
    for j in dict:
        list.append(dict[j])
s=input("Please enter a string: ")
mostFreq=most_frequent(s)
list.sort(reverse=True)
for i in list:
    for key,value in dict.items():
        if value == i:
            print(key,"=",value, end=" ")
            dict[key]=0
            break
        
