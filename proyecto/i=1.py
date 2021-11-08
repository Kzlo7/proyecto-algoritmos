def po(x,n):
    x1=x*x

    if(n==0):
        return 1
    else:
        if(n%2==0):
            
            return po((x1),(n/2))
        else:
            return x*po((x1),(n/2))
    return print(po(x,n))



