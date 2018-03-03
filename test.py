a=['276747;"0609801279";"0"']

new=[]
for item in a:
    new.extend(item.split(';'))
print(new[2].replace('"', ''))
