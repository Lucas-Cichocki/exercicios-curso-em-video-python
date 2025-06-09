v = []

for i in range(5):
    r = int(input('Digite o numero '))
    
    if i == 0:
        v.append(r)
    
    elif r > v[-1]:
        v.append(r)

    else:
        pos = 0
        while pos < len(v):
            if r <= v[pos]:
                v.insert(pos, r)
                break
            pos += 1

print(v)