def check_palindrome(number):
    n=str(number)
    length=len(n)
    
    for i in range(int(length/2)):
        if n[i]==n[length-i-1]:
            continue
        else:
            return False

    return True
def check_primenumber(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2,int(n ** 0.5)+1):
        if n%i==0:
            return False
    return True

        
    
number=input()
N=int(number)
while(True):
    if(check_palindrome(N) and check_primenumber(N)):
        print(N)
        break
    N=N+1
       

