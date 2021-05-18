# Print numbers using an indirect recursive call:
def printn(lr, ur):
    if lr <= ur:
        print(lr)
        lr += 1
        fun(lr, ur) #indirect recursive call

    else:
        return

def fun(lr, ur):
    if lr <= ur:
        print(lr)
        lr += 1
        printn(lr, ur) #indirect recursive call

    else:
        return

n = int(input("Enter number: "))
printn(1, n)