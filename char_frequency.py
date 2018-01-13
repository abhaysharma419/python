try:
    name=input('Enter the file name:')
    file=open(name)
except FileNotFoundError:
    print("Please run again with a vaild file name.")
    exit()


d={} 
#read the characters from the file and place them in a dictionary with their frequency of the characters as value in dictionary.

for line in file:
     
    for ch in line:
        ch.lower()
        if ch.isalpha():
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
l=[]
sum=0

#get the count of total characters in a file
for k, v in d.items():
    sum+=v

# calculate the percentage of word frequency in a file in decreasing order.

for k,v in d.items():
    l.append(((v/sum)*100,k))
    l.sort(reverse=True)
print(l)
