a = int(input())
result = 0
for i in range(a):
    poly = str(input())
    if poly == 'Tetrahedron':
        result+=4
    if poly == 'Cube':
        result+=6
    if poly == 'Octahedron':
        result+=8
    if poly == 'Dodecahedron':
        result+=12
    if poly == 'Icosahedron':
        result+=20
print(result)
    
    