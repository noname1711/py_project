from future.moves import tkinter
import math
def click(val):

    e = entry.get() 
    ans = " "
    try:
        if val == "C":
            e = e[0:len(e) - 1] 
            entry.delete(0, "end")
            entry.insert(0, e)
            return

    elif val == "CE":
        entry.delete(0, "end")
    elif val == "V":
        ans = math.sqrt(eval(e))

    elif val == "π":

        ans = math.pi

    elif val == "cos":

        ans = math.cos(math.radians (eval(e)))

    elif val == "sin":

        ans = math.sin(math.radians (eval(e)))

    elif val == "tan":

        ans = math.tan(math.radians (eval(e)))

    elif val == "2π":

        ans = 2 math.pi

    elif val == "cosh":

        ans = math.cosh(eval(e))

    elif val == "sinh":

        ans = math.sinh(eval(e))

    elif val == "tanh":

        ans = math.tanh(eval(e))

    elif val == chr(8731):

        ans = eval(e) ** (1/3)

    elif val == "x\u02b8":

        entry.insert("end", "**")

        return

    elif val == "x\u00B3":

        ans = eval(e) ** 3

    elif val == "x\u00B2":

        ans = eval(e) ** 2

    elif val == "ln":

        ans = math.log2(eval(e))

    elif val == "deg":

        ans = math.degrees (eval(e))

    elif val == "rad":

        ans = math.radians(eval(e))

    elif val == "e":

        ans = math.e

    elif val == "log10":

        ans = math.log10(eval(e))

    elif val == "x!":

        ans = math.factorial(eval(e))

    elif val == chr(247):
        entry.insert("end", "/")
        return

    elif val == "=":

        ans = eval(e)
    else:
        entry.insert("end", val)