with open("d","r")as f:d=[int(i)for i in f.readlines()]
c=0;o=d[0]+d[1]+d[2]
for i in range(len(d)-2):
 s=d[i]+d[i+1]+d[i+2]
 if s>o:c+=1
 o=s
print(c)