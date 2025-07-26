'''
UNBOUNDED KNAPSACK
given a knapsack weight,say capacity and a set of n items with certain value vali and weight wti, The task is to fill 
the knapsack in such a way that we can get the maximum profit.this is different from the Classical Knapsack Problem here 
we are allowed to use an unlimited number of instnces of an item

#example
 input: capacity=100,val[]=[1,30],wt[]=[1,50]
 output=100
 
 # using recursion

def knapsack(i,capacity,val,wt):
    if i==len(val):
        return 0
    take=0
    if wt[i]<=capacity:
        take=val[i]+knapsack(i,capacity-wt[i],val,wt)
    noTake=knapsack(i+1,capacity,val,wt)
    return max(take,noTake)
def knap(capacity,val,wt):
    return knapsack(0,capacity,val,wt)
val=[1,1]
wt=[2,1]
capacity=3
print(knap(capacity,val,wt))
'''
#memorization
def knapsack(i,capacity,val,wt,memo):
    if i==len(val):
        return 0
    if memo[i][capacity]!=-1:
        return memo[i][capacity]
    take=0
    if wt[i]<=capacity:
        take=val[i]+knapsack(i,capacity-wt[i],val,wt,memo)
    noTake=knapsack(i+1,capacity,val,wt,memo)
    memo[i][capacity]=max(take,noTake)
    return memo[i][capacity]
def knap(capacity,val,wt):
    memo=[[-1 for _ in range(capacity+1)] for _ in  range(len(val))]
    return knapsack(0,capacity,val,wt,memo)

val=[1,1]
wt=[2,1]
capacity=3
print(knap(capacity,val,wt))