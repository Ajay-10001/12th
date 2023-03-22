def intopos(input) :
    oper = ["+","-","*","/"]
    prio = {"(":0,")":0,"+":1,"-":1,"*":2,"/":2,"**":3,"^":3}
    stack = []
    exp = ""
    for chr in input :
        if chr == "(" :
            stack.append(chr)
        elif chr == ")" :
            if stack and "(" in stack :
                ele = stack[-1]
                while ele != "(" :
                    ele = stack.pop()
                    exp += ele
                    ele = stack[-1]
                stack.pop()
            else :
                None
        elif chr in oper :
            while stack and prio[chr] <= prio[stack[-1]] :
                ele = stack.pop()
                exp += ele
            stack.append(chr)
        elif chr ==" " :
            None
        else :
            exp += chr
        #print("chr :",chr,"     stack :",stack,"     exp :",exp)
    while stack :
        ele = stack.pop()
        exp += ele
    while exp.endswith("(") :
        x = len(exp)
        exp = exp[:x-1:]
    print("Result : \n", exp)

VAL = 0
while VAL == 0 :
    x = input("Enter Your Infix Expression : \n")
    intopos(x)
    ch = input("Do You Want To Convert Again (Y/N) : ")
    if ch in "Nn" :
        VAL =1
