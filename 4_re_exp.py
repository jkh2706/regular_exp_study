# 특정단어를 포함하는 예문만 모아 파일로 정리하자
import re
import unicodedata

# 한줄에 들어간 하나의 문장을 리스트로 만든다.
with open('friends101.txt', 'r', encoding='utf-8') as f:
    sentences = f.readlines()
#normal_script101 = unicodedata.normalize('NFKD', script101)

# 대사만 추려낸다. 사람이름:... 규칙을 정규표현식으로 나타낸다.
# for i in sentences:
#     if re.match(r'[A-Za-z]+:', i) and re.search('would', i):  # 정규표현식을 만족하는 리스트속의 원소들만 출력한다.
#         print(i)

# 추려낸 대사들 중에서 다시 'would'단어를 포함하는 대사만 추려낸다. 위 조건에 추가한다.
# would 객체를 만들어 결과를 저장한다.
would = [i for i in sentences if re.match(r'[A-Za-z]+:', i) and re.search('would', i)] # list comprehension
print(would)

# 추출한 문장으로 'would.txt' 파일을 만들어 저장한다.
with open('would.txt', 'w', encoding='utf-8') as w:
    w.writelines(would)  # 한줄씩 파일에 쓴다.