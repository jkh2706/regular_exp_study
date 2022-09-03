# 등장인물 리스트를 만들어보자
import re
import unicodedata

with open('re_exp/friends101.txt', 'r', encoding='utf-8') as f:
    script101 = f.read()

normal_script101 = unicodedata.normalize("NFKD", script101)  # 문자열의 '\xa0' 없애기

# 검색 패턴을 컴파일한 객체를 생성한다.
# 대문자로 시작하고 소문자 반복(+)되다가 ':'으로 끝나는 패턴
char = re.compile(r'[A-Z][a-z]+:')  
result = re.findall(char, script101)  # script101 객체에서 char객체의 패턴을 모두 찾아서 result에 리스트로 반환한다.
print(result)