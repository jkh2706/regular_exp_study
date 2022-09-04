# 등장인물 리스트를 만들어보자
import re
import unicodedata

with open('friends101.txt', 'r', encoding='utf-8') as f:
    script101 = f.read()

normal_script101 = unicodedata.normalize("NFKD", script101)  # 문자열의 '\xa0' 없애기

# 검색 패턴을 컴파일한 객체를 생성한다.
# 대문자로 시작하고 소문자 반복(+)되다가 ':'으로 끝나는 패턴
char = re.compile(r'[A-Z][a-z]+:')  
result = re.findall(char, script101)  # script101 객체에서 char객체의 패턴을 모두 찾아서 result에 리스트로 반환한다.


# 반복되는 리스트를 제거하기 위해 리스트를 집합(set)으로 변경한다.
result = set(result)

# 목록을 수정하기위해 다시 리스트로 만든다.
result = list(result)

# 이름 마지막에 콜론을 삭제한다. 문자열 슬라이싱을 사용
new_result = []
for i in result:
    i = i[:-1]
    new_result.append(i)

print(new_result)



