
pattern='}'
f = open('cfout.py', 'r')
g = open('tempo.py', 'w')
l=f.readlines()
f.close()
for ind in range(len(l)):
    if pattern in l[ind]:
        l[ind-1]=   l[ind-1] + "}" + "\n"
        l[ind] = l[ind].replace('}','')
        g.write("\n")
for field in l:
    g.write(field)
g.close()


