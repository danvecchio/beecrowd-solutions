runs = int(input())

for i in range(runs):
    hash_map={}
    x,y = map(int,input().split())
    hash_map[(3*x)**2 + y**2] = 'Rafael'
    hash_map[2*(x**2)+(5*y)**2] = 'Beto'
    hash_map[-100*x+y**3] = 'Carlos'
    key = max(hash_map)
    print(hash_map[key],'ganhou')


