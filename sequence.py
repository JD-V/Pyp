print("enter number :")
N= int(input())
for i in range(1,N):
    print ( (i*10**(i-9) if (i-9)>=0 else 0) +        (i*10**(i-8) if (i-8)>=0 else 0) +         (i*10**(i-7) if (i-7)>=0 else 0) +         (i*10**(i-6) if (i-6)>=0 else 0) +         (i*10**(i-5) if (i-5)>=0 else 0) +       (i*10**(i-4) if (i-4)>=0 else 0) +         (i*10**(i-3) if (i-3)>=0 else 0) +         (i*10**(i-2) if (i-2)>=0 else 0) +        (i*10**(i-1) if (i-1)>=0 else 0 )        )


        