dict1={' ':1,'a':1,'b':2,'c':3,'d':1,'e':2,'f':3,'g':1,'h':2,'i':3,'j':1,'k':2,'l':3,'m':1,'n':2,'o':3,'p':1,'q':2,'r':3,'s':4,'t':1,'u':2,'v':3,'w':1,'x':2,'y':3,'z':4}
case=0
result=[]
size=int(input("Enter size of line:"))
for i in range(size):
    words=input("Enter words:")
    for j in words:
        char=dict1[j]
        case=case+char
    result.append(case)
    case=0
j=1
for i in result:
  print('Case',j,':',i)
  j=j+1

