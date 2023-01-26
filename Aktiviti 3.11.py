
print("Jawab soalan-soalan berikut.\na = 12,b = 5, c = 2")
a = 12
b = 5
c = 2

s1 = str("True")
s2 = str("False") 
s3 = str("True")
s4 = str("True")
s5 = str("False")

bil_betul = 0
bil_salah = 0

print("1.a > b \n2.a % b= 0 \n3.12 // 5 = c\n4.a > b > c\n5. b < 2 < a ")


j1 = input("Jawapan soalan 1: ") 
j2 = input("Jawapan soalan 2: ") 
j3 = input("Jawapan soalan 3: ") 
j4 = input("Jawapan soalan 4: ") 
j5 = input("Jawapan soalan 5: ") 

if s1 != j1 :
    bil_salah += 1
    bil_betul += 0
else:
    bil_betul += 1
    bil_salah += 0

if s2 != j2:
    bil_salah += 1
    bil_betul += 0
else:
    bil_betul += 1
    bil_salah += 0

if s3 != j3:
    bil_salah += 1
    bil_betul += 0
else:
    bil_betul += 1
    bil_salah += 0

if s4 != j4:
    bil_salah += 1
    bil_betul += 0
else:
    bil_betul += 1
    bil_salah += 0

if s5 != j5:
    bil_salah += 1
    bil_betul += 0
else:
    bil_betul += 1
    bil_salah += 0

print("Anda telah menjawab",bil_betul,"dengan betul dan ",bil_salah,"soalan dengan salah.")
if bil_salah > 0:
    print("Sila buat ulang kaji")
else:
    print("Tahniah,anda telah menjawab semua soalan dengan betul.")
