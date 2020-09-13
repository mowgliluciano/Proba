
#parovi(a,b,c,d)=>listaParova iz intervala ([a,b],[c,d])

a = int(input("a = "));
b = int(input("b = "));
c = int(input("c = "));
d = int(input("d = "));


parovi = [(i,j) for i in range(a,b) for j in range(c,d)]

print(parovi)
