def totalCountToFullFill(a,n,d):
         count=0
         totalValue=sum(a)
         remeanderValue=totalValue%n
         index=0
         while((index+d)<n):
                 if(a[index]>remeanderValue):
                         count=count+a[index]-remeanderValue
                         a[index+d]=a[index+d]+a[index]-remeanderValue
                 elif(a[index]<remeanderValue):
                         count=count+remeanderValue-a[index]
                         a[index+d]=a[index+d]-(remeanderValue-a[index])
                 index=index+1
         print(count)
          
def checkChefMover(a,n,d):
        for index in range(n):
                totalValue=0
                innerIndex=index
                counter=0
                while(innerIndex<n):
                        totalValue=totalValue+a[innerIndex]
                        innerIndex=innerIndex+d
                        counter=counter+1
                if(totalValue%counter != 0):
                        print("two-1",totalValue,counter)
                        return
        totalCountToFullFill(a,n,d)

def main():
        testCase=eval(input())
        for i in range(testCase):
                [n,d]=map(int,input().split())
                a=list(map(int,input().split()))
                totalValue=sum(a)
                meanValue=int(totalValue/n)
                remeanderValue=totalValue%n
                if(remeanderValue != 0):
                        print("one-1")
                        continue
                checkChefMover(a,n,d)
         
main()
