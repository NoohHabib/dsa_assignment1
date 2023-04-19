str = "ab+c*"
stack = []
for i in str:
    if i.isalnum():
        stack.append(i)
    else:
        oprnd2=stack.pop()
        oprnd1=stack.pop()
        res=i+oprnd1+oprnd2
        stack.append(res)
print(stack[-1])
