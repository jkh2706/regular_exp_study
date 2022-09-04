import re
import unicodedata



# f = codecs.open('re_exp/friends101.txt', 'r', encoding='utf-8')
# script101 = f.read()

with open('friends101.txt', 'r', encoding='utf-8') as f:
    script101 = f.read()

normal_script101 = unicodedata.normalize("NFKD", script101)  # 문자열의 '\xa0' 없애기


line = re.findall(r'Monica:.+', normal_script101)  # Monica 대사만 골라내서 리스트로 반환한다.

# 모니카의 대사만 따로 정라하여 텍스프 파일로 만들어 보자
monica = ''  # 리스트를 텍스프파일로 저장하기위해 문자열형태의 빈 객체를 만든다.
for i in line:
    monica += i + "\n" # 리스트로 되어았는 모니카의 대사를 전부다 문자열로 더하고 한요소가 더해지면 줄을 바꾼다.

# monica 객체의 내용을 텍스트파일을 만들어 거기에 쓴다.    
with open('Monica.txt', 'w', encoding='utf-8') as m:
    m.write(monica) 


