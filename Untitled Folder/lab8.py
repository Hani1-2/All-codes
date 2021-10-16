from stackwithlist import mystack
#### Algo 8.1
def evaluate(expr):
    st=mystack()
    for i in range(len(expr)):
        token=expr[i]
        if token=='^' or token=='*' or token=='/' or token=='+' or token=='-':
            val2=st.pop()
            val1=st.pop()
            if token=='^':
                res=pow(val1,val2)
            elif token=='*':
                res=val1*val2
            elif token=='/':
                res=val1//val2 #we are working with integer math
            elif token=='+':
                res=val1+val2
            else:
                res=val1-val2
            st.push(res)
        else:
            st.push(token)
    return st.pop()

def precedence(x):
    if x=='[' or x=='{' or x=='(':
        return 0
    if x == '+' or x == '-':
        return 1
    if x == '*' or x == '/':
        return 2
    return 3 #highest precedence is of ^

def aishigherthanb(a,b):
    return precedence(a)>precedence(b)

def aislessorequalthanb(a,b):
    return precedence(a)<=precedence(b)
### Algo 8.2 
def infixtopostfix(expr):
    st=mystack()
    postfix=list()
    for i in range(len(expr)):
        token=expr[i]
        if token=='[' or token=='{' or token=='(':
            st.push(token)
        elif token==']' or token=='}' or token==')':
            done=False
            while not done:
                if not st.isEmpty():
                    top=st.pop()
                    if top=='[' or top=='{' or top=='(':
                        done=True
                    else:
                        postfix.append(top)
                else:
                        done=True
        elif token=='^' or token=='*' or token=='/' or token=='+' or token=='-':
            done=False
            while not done:
                if st.isEmpty():
                    st.push(token)
                    done=True
                else:
                    top=st.pop()
                    if aishigherthanb(token,top):
                        st.push(top)
                        st.push(token)
                        done=True
                    else:
                        postfix.append(top)
        else:
            postfix.append(token)
    while not st.isEmpty():
        top=st.pop()
        postfix.append(top)
    return postfix

myinfix=[1, 4,18,6,'/',3,'+','+', 5,'/','+']
#myinfix=[2,'*',4,'-',9,'+',5,'^',2]
print("infix=",myinfix)
mypostfix=infixtopostfix(myinfix)
print("postfix=",mypostfix)
##value=evaluate(myinfix)
##print("value=",value)
#####myinfix=[2,'*',4,'-',9,'+',5,'^',2]

#Algo 8.3 
import operator
def operate(token,opr,opd):
    operators= {")":0,"(":0,"-":1,"+":1,"*":2,"^":3}
    operations = {"^":pow,"*":operator.mul,"/":operator.truediv,"+":opoerator.add,"-":operator.sub}
    if token == "(":
        opr.push(token)
        return
    else:
        t_prec = operator[token]
        topOp = opr.pop()
        s_pres = operators[topOp]
        while t_prec<=s_prec:
            if topOp=="+" or topOp=="*" or topOp=="/":
                b = int(opd.pop())
                a = int(opd.pop())
                res = operations[topOp](a,b)
                opd.push(res)
            else:
                if topOp=="(":
                    opr.push(topOp)
                    return
            if opr.isEmpty():
                break
            t_prec = operators[token]
            topOp = opr.pop()
            s_prec = operators[topOp]
    opr.push(token)
    return

def eval_infix():
    tokens = input("Enter space separated  values with proper paranthesis: ")
    if token[0]!="(":
        tokens = "(" + tokens + " )"
        tokens = tokens.split(" ")
        opr = mystack()
        opd = mystack
        operators = ["+","-","*","^","(",")"]
        opr.push("(")
        for token in tokens:
            if token not in operators:
                opd.push(token)
            else:
                operate(token,opr,opd)
        values = opd.pop()
        return value










##def infix(expr):
##    st_opr=mystack()
##    st_opt=mystack()
##    for i in range(len(expr)):
##        token=expr[i]
##        if token=='^' or token=='*' or token=='/' or token=='+' or token=='-':
##            if st_opr.isEmpty():
##                st_opt.append(token)
##            elif token=='^' or token=='*' or token=='/' or token=='+' or token=='-' :
##                topOp = st_opt.pop()
##                token_pre = precedence(token)
##                topOp_pre = precedence(topOp)
##                if aislessorequalthanb(token_pre,topOp_pre):
##                    val1 = st_opr.pop()
##                    val2 = st_opr.pop()
##                    if topOp=='^':
##                        res=pow(val1,val2)
##                    elif topOp=='*':
##                        res=val1*val2
##                    elif topOp=='/':
##                        res=val1//val2 #we are working with integer math
##                    elif topOp=='+':
##                        res=val1+val2
##                    else:
##                        res=val1-val2
##                    st_opr.push(res)
##                    st_opr.push(token)
##        else:
##            st_opr.push(token)
##    return st_opr.pop()

##
##myinfix=[2,'*',4,'-',9,'+',5,'^',2]
##print('infix:',infix(myinfix))


