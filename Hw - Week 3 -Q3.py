
A = int(input("GIVE ME NUMBER : "))
B = int(input("GIVE ME NUMBER : "))
C = int(input("GIVE ME NUMBER : "))
D = int(input("GIVE ME NUMBER : "))
E = int(input("GIVE ME NUMBER : "))

if A == B or A == C or A == D or A == E:
    print("Duplicate")
elif B == C or B == D or B == E or C == D or C == E or D == E:
    print("Duplicate")
else:
    print("All unique")