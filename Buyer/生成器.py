def fun():
    x = 0
    i = 0
    j = 0
    while True:
        send_key = yield x
        if send_key.isalpha():
            i += 1
            print("全部是字母有%s次"%i)
        else:
            j += 1
            print("不全是字母有%s次"%j)
import random
example = "adsdaddasdsdeedsd3ddsd"

def get_string(k):
    f = fun()
    next(f)
    for i in range(k):
        string = "".join(random.sample(example,5))
        print(string)
        f.send(string)

get_string(100)