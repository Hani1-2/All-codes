from stackwithlist import mystack

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
#myinfix=[1, 4,18, 6 , '/',3,' +',' +', 5,' /','+']
#myinfix=[2,'*',4,'-',9,'+',5,'^',2]
##myinfix=['[',2,'*',4,'-','(',9,'+',5,')',']','^',2]
myinfix=[2,'^',3,'*',7,'+','(',5,'-',4,')','*',15,'/',3,'-',8]
#myinfix = ['(','(','a','-','b','*',')','-','(','d','-','e','-','f',')',')',')',')','/','(','(','g','-','h',')','*','i']
##myinfix=[2,'*',5,'+',7,'+','{',3,'^',2,'*',4,'+',5,'-',1,'}','*',3]
##myinfix = ['(',2,'+',5,')','*','(',9,'/',3,')']
print("infix=",myinfix)
mypostfix=infixtopostfix(myinfix)
print("postfix=",mypostfix)
value=evaluate(mypostfix)
print("value=",value)
##mypostfix=[7,5,'-',4,6,8,'+','*','+']
##value=evaluate(mypostfix)
##print("value=",value)
##myinfix=['(',3,'-',8,')','*',7,'+','(',8,'/',2,')','-',9]
##print("infix=",myinfix)
##mypostfix=infixtopostfix(myinfix)
##print("postfix=",mypostfix)
