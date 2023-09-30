def Hanoi (n,Origen=1,Auxiliar=2,Destino=3):
    if n==1:
        print (Origen,"a",Destino)
        
    else:
        Hanoi(n-1,Origen,Destino,Auxiliar)
        print(Origen,"a",Destino)
        Hanoi (n-1,Auxiliar,Origen,Destino)
    return 
Hanoi(3)
