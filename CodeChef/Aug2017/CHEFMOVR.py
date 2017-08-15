def checkChefMover(a,n,d):
        for index in range(n):
                

def main():
	testCase=eval(input())
	for i in range(testCase):
	    [n,d]=map(int,input().split())
	    a=list(map(int,input().split()))
	    totalValue=sum(a)
	    meanValue=int(totalValue/n)
	    remeanderValue=totalValue%n
	    if(remeanderValue != 0):
                    print("-1")
                    continue
            checkChefMover(a,n,d)
main()
