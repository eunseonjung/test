#입력
a, b= map(int, input().split())

#2개의 처리를 위해 큰 값 알기
if a>=b:
  big=a
else:
  big=b
    
#최대공약수
for i in range(big+1,1,-1):
  if (a%i==0) &(b%i==0):
    print(i)
    break

#최소공배수
for i in range(big+1,(a*b)+1):
  if (i%a==0) & (i%b==0):
    print(i)
    break

