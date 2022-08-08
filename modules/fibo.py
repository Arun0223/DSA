def febonacci(n:int):
    '''It's a recursive function it will print febonacci series n times
    and it takes int as a arguments'''
    if n<=1:
        return 1
    else:
        return febonacci(n-1)+febonacci(n-2)