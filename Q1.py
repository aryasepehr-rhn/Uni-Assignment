#محاسبه حقوق خالص 



salary = float(input("حقوق ماهانه را وارد کنید: "))

tax = salary * 0.10

net_salary = salary - tax

print("------ ماشین حساب مالیاتی ------")
print("حقوق ماهانه:", salary)
print("مبلغ مالیات:", tax)
print("حقوق خالص:", net_salary)