# 숫자의 평균값 구하기
def avg_num(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args) #총합후 길이만큼 나누기

a = avg_num(1, 2, 3)
print("1, 2, 3의 평균은 %.2f 입니다." %a)

b = avg_num(1, 2, 3, 4)
print("1, 2, 3, 4의 평균은 %.2f 입니다." %b)

# 구구단 만들기
for i in range(2, 10):    # i * j = ij 의 곱하기 생성 
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}', end="")
    
# 별모양의 직삼각형 만들기        
star = input("별 트리 크기 입력 :")
star = int(star)
i = 0
while True :
    i += 1
    if i > star : break
    print("*" *i)  #별모양을 i의 크기만큼 출력
    
# 훌수 짝수 판별하기
def even_odd(dec):
    if dec % 2 == 1: #홀수 짝수 판별 후 출력
        print("%d는 홀수입니다." %dec)
    else:
        print("%d는 짝수입니다." %dec)
        
number = int(input("정수를 입력하세요 : "))
even_odd(number)
number2 = int(input("정수를 입력하세요 : "))
even_odd(num)
