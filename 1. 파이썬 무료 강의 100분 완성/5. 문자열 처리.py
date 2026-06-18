# 인덱스와 슬라이싱
lang = "PYTHON"
print(lang[0])     
print(lang[-1])   
print(lang[1:5]) 
print(lang[1:])    

# 문자열 메소드
letter = "How are you?"
print(letter.lower())       
print(letter.upper())       
print(letter.capitalize())  
print(letter.title())       
print(letter.swapcase())   
print(letter.split())      
print(letter.count("How"))  

s = "나도 고등학교"
print(s.startswith("나도"))
print(s.endswith("학교"))   
print(s.replace("고등학교", "고교"))
print(s.find("학교"))      

# 문자열 포맷팅
python = "파이썬"
java = "자바"
print("{} {}".format(python, java))
print("{1} {0}".format(python, java))
print(f"{python} {java}")

# 탈출 문자
print("나는 속으로 \"엄청 어려운데\"라고 생각했다") 
print("C:\\Users\\Nadocoding") 
print("첫 줄\n두 번째 줄") 