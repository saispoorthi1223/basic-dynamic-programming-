def knapsack(wt,prof,W,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]>W:
        return knapsack(wt,prof,W,n-1)
    else:
        include=(prof[n-1]+knapsack(wt,prof,W-wt[n-1],n-1))
        exclude=knapsack(wt,prof,W,n-1)
        return max(include,exclude)
wt=[3,4,6,5]
prof=[5,8,3,1]
W=8
n=4
print(knapsack(wt,prof,W,n))
'''knapsack(8,4)
|-wt[3]=5<=8->we can include or exclude
|-ijnclude item 4:value
|-knapsack(3,3)
    |-wt[2]=6>3 ->skip ->knapsack(3,2)
        |-wt[1]=4>3->skip ->knapsack(3,1)
            |-wt[0]=3<=1 ->choose max(include,exclude)
            |-include:2+knapsack(0,0)=2
            |-exclude:knapsack(3,0)=0
            max=2
    |-total if we include the item 4=4+6
    |-exclude item 4:knapsack(8,3)
    |-wt[2]=6<8 choose max(include,exclude)
    |-include:1 +knapsack(2,2)
    |-wt[1]=4>2-> skip->knapsck(2,1)
    |-wt[0]=3>2 ->skip ->knapsack(2,0)=0
    include path=1+0=1
'''