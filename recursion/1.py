
def printn(name,n):
    if n==5:
     return
    else :   
      print(name)
      n=n+1
      printn(name)
      
name='prithvi'
n=int(input("Enetr a number:"))
printn(name,n)      