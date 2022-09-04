# 스크립트에서 지문만 추출해보자
# 지문의 규칙을 찾는다.
# 찾은 규칙을 정규표현식으로 작성한다.

import re
import unicodedata

with open('friends101.txt', 'r', encoding='utf-8') as f:
    script101 = f.read()
normal_script101 = unicodedata.normalize("NFKD", script101)  # 문자열의 '\xa0' 없애기

# 찾은 지문 패턴을 컴파일한다.
# 공백없이 '\('괄호로 시작하고 [A-Za-z]대문자나 소문자 영문이 나오고  (.+) 문자/숫자/공백 자유롭게 반복되다가 소문자 혹은 '.'으로 끝난다.
char = re.compile(r'\([A-Za-z].+?\)')  # '?\)' 괄호를 만나면 찾기를 끝내라(탐욕정지)
result = re.findall(char, normal_script101)  # char 저장된 패턴을 normal_script101 객체에서 찾아 result 변수에 반환한다.

for i in result:
    print(i)
