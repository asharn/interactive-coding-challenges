def main():
	testCase=eval(input())
	for i in range(testCase):
	    [n,m]=map(int,input().split())
	    f=list(map(int,input().split()))
	    p=list(map(int,input().split()))
	    a=[0 for k in range(m+1)]
	    flag=False
	    #Condition for 0 pay value of basket
	    for j in range(n):
	        if(p[j]==0):
	            flag = True
	            if(f.count(f[j])>1):
	                #Condition to check 0 pay value of all basket of same type
	                for k in range(n):
	                    if(f[k]==f[j] and p[k]!=0):
	                        flag = False
	                        break
	            else:
	                #Condition for 0 pay value of basket of only one type
	                break
	    if(flag):
	        print('0')
	        continue
	    for j in range(n):
	        a[f[j]]=a[f[j]]+p[j]
	    output=2501
	    #print(a)
	    for j in range(m+1):
	        if(a[j] != 0 and a[j]<output):
	            output = a[j]
	    print(output)
main()

