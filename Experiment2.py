A = int(input('Enter Prime Number 1: '))
B = int(input('Enter Prime Number 2: '))

a = int(input('Enter Private KeyA for Alice: '))
m = int(pow(B,a,A))

b = int(input('Enter Private KeyB for Bob: '))
n = int(pow(B,b,A))

ka = int(pow(n,a,A))

kb = int(pow(m,b,A))

print('Secret key for the Alice is : %d'%(ka))
print('Secret Key for the Bob is : %d'%(kb))