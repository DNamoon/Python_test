#Q1. 평균구하기

Korean_Score = 80
English_Score = 75
Math_Score = 55

average = (Korean_Score+English_Score+Math_Score)/3

print(average)

#Q2. 홀수/짝수 판별하기

a = 13

if a%2 == 0:
    print('짝수입니다.')
else :
    print('홀수입니다.')
    
#Q3. 주민번호 나누어보기

a_num = "881120-1068234"

print(a_num[0:6],a_num[7:14])

#Q4. 성별 나타내는 숫자 출력하기

pin ="881120-1068234"
if pin[7] == '1' or pin[7] == '3' :
    print("남자입니다.")
elif pin[7] == '2' or pin[7] == '4' :
    print("여자입니다.")
else :
    print("잘 못 입력하셨습니다.")

#Q5. replace

a = "a:b:c:d"
print(a.replace(":","#"))



b = "Life is Short"
print(b.replace("Life","Music"))


#Q6. 
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#Q7. 
a = ['Life','is','too','short']
print(' '.join(a))
