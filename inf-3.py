m = float(input())
l = float(input())
k = m/l**2
if k > 40:
    print("Ожирение третьей степени")
elif k > 35:
    print("Ожирение второй степени")
elif k > 30:
    print("Ожирение первой степени")
elif k > 25:
    print("Предожирение")
elif k > 18.5:
    print("Норма")
elif k > 16 or k == 16:
    print("Дефицит массы тела")
else:
    print("Ярко выраженный дефицит массы тела")