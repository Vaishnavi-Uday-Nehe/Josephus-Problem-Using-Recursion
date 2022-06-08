def josephus_problem(n,k):
    if n==1:
        return 0
    else:
        return (josephus_problem(n-1,k) +k) % n

print(josephus_problem(5,3))















