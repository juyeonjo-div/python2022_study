def print_something(my_name, your_name):
    print("Hello{0}, My name is {1}".format(your_name,my_name))

print_something("Sungchul","TEAMLAB")
print_something(your_name="TEAMLAB", my_name="Sunghul")

def print_func(name, gender, age):
    print('이름:{0},age:{1},gender:{2}').format(name,age,gender))

    print_func('홍길동','남자',20)
    print_func(name='kim',age=30,gender='여자')

def func1(a, b=20, c=30):
        print('a={0}, b={1}, c={2}'.format(a,b,c))

func1(10,20,30)
func1(10,20)
func1(10)

def func2(a, b, c):
    print(a, b,c)

func2(1,2,3)
func2(1,2,3,4,)
func2(1,2,3,4,5,)

def kwargs_fuc(**kwargs):
    print(kwargs)
    print('first valuse is {first}'.format(**kwargs))
    print('second valuse is {second}'.format(**kwargs))
    print('third valuse is {thord}'.format(**kwargs))

kwargs_fuc(first=10, second=20, third=30)

{'first': 10, 'second' : 20, third: 30}
first values is 10
second values is 20
third values is 30

a='pytohn with bigdata'
print(a[2:5])

print(a[:5])
print(a[5:])
print(a[-3:])
print(a[::2])
print(a[::-1])

b='and IOT'
print(a+b)

c="*"

if 'IPT' in a:
    print(a)
else:
    print(b)

a+3.9

len(a)

print(b.upper())
print(b.lowr())
print(a.title())
print(a.capitalize())
print(a.count('a'))
print(a.rfind('with'))
print(a.isdigit())

b.strip()


f=open('data/yesterday.txt','r')
lines=f.readlines()
lines

contents=''
for line in lines:
    comtents+=line.strip()" "
contents

n=contents.lowr().count('yesterday')
print("Number of a word 'yesterday'",n)
Number of a word 'yesterday' 9

name="홍길동"
age=20
s1="내 이릉은 %s이고, 나이는 %d입니다"%(name,age)
s1

pname="사과"
price=3.5687

s2="제품명은 %10s이고, 단가는 %10.2f입니다"%(pname, price)
s2

s3="제품명은 {0}이고, 단가는 {1}입니다".format(pname,price)
s3

s4="제품명은 {0:10s}이고, 단가는 {1:10.2f}입니다".format(pname,price)
s4

s5="제품명은 {0:<10s}이고, 단가는 {1:<10.2f}입니다".format(pname,price)
s5

s6="제품명은 {0:10s}이고, 단가는 {1:10.2f}입니다".format(pname,price)
s6
