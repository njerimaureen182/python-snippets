wordlist=['cat','dog','rabbit']
alist=[]
for aword in wordlist:
    for aletter in aword:
        alist.append(aletter)
print(alist)