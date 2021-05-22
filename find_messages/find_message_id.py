import sys
import os




ids1 = []
paths1 = {}
for (r,s,f) in os.walk(sys.argv[1]):
    for i in f:
        path  = os.path.join(r,i)
        with open(path, 'rb') as read_obj:
            for line in read_obj:
                if line.startswith(b"Message-ID"):
                    ids1.append(line)
                    paths1[line]=path
                    #print(line)


ids2 = []

for (r,s,f) in os.walk(sys.argv[2]):
    for i in f:
        path  = os.path.join(r,i)
        with open(path, 'rb') as read_obj:
            for line in read_obj:
                if line.startswith(b"Message-ID"):
                    ids2.append(line)


for item in set(ids1)-set(ids2):
    print(f"{paths1[item]} {item}")
    pass

