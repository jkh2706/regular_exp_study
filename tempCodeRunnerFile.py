for i in sentences:
    if re.match(r'[A-Za-z]+:', i) and re.search('would', i):  # 정규표현식을 만족하는 리스트속의 원소들만 출력한다.
        print(i)
