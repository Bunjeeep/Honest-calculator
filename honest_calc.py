# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
memory = 0.0
answer = 'y'
msg_index=0
result = 0


def calcl():
    print(msg_0)
    calc = input()
    calc = calc.split(' ')
    result = 0
    global x
    global y
    global oper
    x = calc[0]
    y = calc[2]
    if x == 'M':
        x = memory
    else:
        try:
            x = float(calc[0])
        except:
            x = calc[0]
    if y == 'M':
        y = memory
    else:
        try:
            y = float(calc[2])
        except:
            y = calc[2]
    oper = calc[1]


def eq_corr():
    global c2
    global c1
    c2 = (oper != '+' and oper != '-' and oper != '*' and oper != '/')
    c1 = (type(x) != int and type(x) != float) or (type(y) != int and type(y) != float)


def result_op():
    global result
    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/':
        result = x / y
    print(float(result))


def store():
    global memory
    global answer3
    answer2 = 'o'
    while not (answer2 == 'y' or answer2 == 'n'):
        print(msg_4)
        answer2 = input()
    if answer2 == 'y':
        if is_one_digit(result):
            global msg_index
            msg_index=10
            print(msg_10)
            answer3=input()
            while not(answer3=='y' or answer3=='n'):
                print(msg_10)
                answer3=input()
            while answer3=='y' and msg_index <12:
                msg_index=msg_index+1
                save_memory()
        else:
            memory = result
    else:
        memory = result


def save_memory():
    global answer3
    if msg_index==11:
        print(msg_11)
    elif msg_index==12:
        print(msg_12)
    answer3 = input()




def cont_calc():
    global answer
    answer = 'o'
    while not (answer == 'y' or answer == 'n'):
        print(msg_5)
        answer = input()


def v1_v2_v3():
    global v1
    global v2
    global v3
    v1 = x
    v2 = y
    v3 = oper
    msg=""
    if is_one_digit(v1) and is_one_digit(v2) or (v1==v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8
    if msg != "":
        print(msg_9+msg)


def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


while answer == 'y':
    calcl()
    eq_corr()
    while (c1 or c2) or (oper == '/' and y == 0):
        if c1 == True:
            print(msg_1)
            calcl()
        if c2 == True:
            print(msg_2)
            calcl()
        if oper == '/' and y == 0:
            v1_v2_v3()
            print(msg_3)
            calcl()
        eq_corr()
    v1_v2_v3()
    result_op()
    store()
    cont_calc()