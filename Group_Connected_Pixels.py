#Algorithm written by Nishant Garg, former Junior Research Fellow, Observational Astronomy, S.N. Bose National Centre for Basic Sciences

#input coords as a list of tuples of coordinates to group together
coords = []

def find_neighbour(a,b):
    temp_list=[]
    for value2 in b:
        if value2==[a[0]+1,a[1]]:
            temp_list.append(value2)
        elif value2==[a[0]-1,a[1]]:
            temp_list.append(value2)
        elif value2==[a[0],a[1]+1]:
            temp_list.append(value2)
        elif value2==[a[0],a[1]-1]:
            temp_list.append(value2)
        elif value2==[a[0]-1,a[1]-1]:
            temp_list.append(value2)
        elif value2==[a[0]-1,a[1]+1]:
            temp_list.append(value2)
        elif value2==[a[0]+1,a[1]-1]:
            temp_list.append(value2)
        elif value2==[a[0]+1,a[1]+1]:
            temp_list.append(value2)
        else:
            pass
    return temp_list
    
main_list=[]
n=0
while coords!=[]:
    perm_list=[]
    perm_list.append(coords[0])
    flag=0
    i=0
    while flag!=1:
        element=perm_list[i]
        neighbours=find_neighbour(element,coords)
        values_to_be_removed=[]
        for neighbour in neighbours:
            if neighbour in perm_list:
                values_to_be_removed.append(neighbour)
        if values_to_be_removed!=[]:
            for x in values_to_be_removed:
                neighbours.remove(x)
        if neighbours!=[]:
            perm_list=perm_list+neighbours
        coords.remove(element)
        i=i+1
        if i>len(perm_list)-1:
            flag=1
    print(perm_list)
    main_list.append(perm_list)

for group in main_list:
    print(group)
    print('\n')
