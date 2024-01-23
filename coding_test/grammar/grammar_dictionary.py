def dictionary_example():
    # 사전 자료형은 키와 값의 쌍을 데이터로 가지며, 원하는 "변경 불가능한 자료형" 키로 사용
    # 파이썬의 사전 자료형은 해시테이블을 이용하므로 O(1) 시간에 처리할 수 있다.

    print("dictionary_example")
    data = dict()
    data['사과'] = 'APPLE'
    data['바나나'] = 'Banana'
    data['코코넛'] = 'Coconut'

    print(data)

    if '사과' in data:
        print(data['사과'])


    # 키 or 값만 뽑기
    key_list = data.keys()
    value_list = data.values()

    for key in key_list:
        print(key)

    for value in value_list:
        print(value)

if __name__ == '__main__':
    dictionary_example()
