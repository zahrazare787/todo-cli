number = int(input("یک عدد وارد کنید: "))
if number % 2 == 0:
    print("عدد زوج است")
else:
    print("عدد فرد است")
num1 = int(input("عدد اول را وارد کنید: "))
num2 = int(input("عدد دوم را وارد کنید: "))
if num1 > num2:
    print("عدد اول بزرگتر است")
elif num1 < num2:
    print("عدد دوم بزرگتر است")
else:
    print("هر دو عدد برابرند")
sum = 0
for i in range(1, 101):
    sum += i
print("مجموع اعداد از ۱ تا ۱۰۰ برابر است با:", sum)
