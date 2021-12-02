with open('d')as f:d=[x.strip().split() for x in f.readlines()];dp=0;h=0
for i in d:
 if i[0]=="forward":h+=int(i[1])
 elif i[0]=="down":dp+=int(i[1])
 else:dp-=int(i[1])
print(dp*h)