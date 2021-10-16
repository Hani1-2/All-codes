from stackwithlist import mystack

def evaluate(expr):
    st=mystack()
    expr.reverse()
    for i in range(len(expr)):
        token=expr[i]
        if token=='^' or token=='*' or token=='/' or token=='+' or token=='-':
            val1=st.pop()
            val2=st.pop()
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
    if x==']' or x=='}' or x==')':
        return 0
    if x == '+' or x == '-':
        return 1
    if x == '*' or x == '/':
        return 2
    return 3 #highest precedence is of ^

def aishigherthanb(a,b):
    return precedence(a)>=precedence(b)

def infixtoprefix(expr):
    st=mystack()
    prefix=list()
    expr.reverse()
    for i in range(len(expr)):
        token=expr[i]
        if token==']' or token=='}' or token==')':
            st.push(token)
        elif token=='[' or token=='{' or token=='(':
            done=False
            while not done:
                if not st.isEmpty():
                    top=st.pop()
                    if top==']' or top=='}' or top==')':
                        done=True
                    else:
                        prefix.append(top)
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
                        prefix.append(top)
        else:
            prefix.append(token)
    while not st.isEmpty():
        top=st.pop()
        prefix.append(top)
    prefix.reverse()
    return prefix
myinfix=[2,'*',5,'+',7,'+','{',3,'^',2,'*',4,'+',5,'-',1,'}','*',3]
##
##myinfix=[2,'*',5,'+',7,'+','{',3,'^',2,'*',4,'+',5,'-',1,'}','*',3]
##myinfix = ['(',2,'+',5,')','*','(',9,'/',3,')']
print("infix=",myinfix)
myprefix=infixtoprefix(myinfix)
print("prefix=",myprefix)
value=evaluate(myprefix)
print("value=",value)
