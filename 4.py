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
