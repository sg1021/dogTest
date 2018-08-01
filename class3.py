import math

T1 = 0.05
T2 = 0.005
w1 = [0.1,0.3,0.5,1,3,5,10,20,30,50,100,200,300,500,1000]#変数

for i in w1:
    P1 = 1/(1 + i**2 * T1**2)
    P2 = (i**4 * T1**2 * T2**2) + (i**2 * T1**2) + (i**2 * T2**2) + 1

    G = P1 * math.sqrt(P2)

    G1 = 20 * math.log10(G)
    print("これは",i)
    print("ゲイン=",G)
    print("20log =",G1)

    P3 = (i*(T2 - T1))/(i**2 * T1*T2 + 1)
    a = math.atan(P3)
    sita = math.degrees(a)
    print("位相=",sita)
    print("\n")

