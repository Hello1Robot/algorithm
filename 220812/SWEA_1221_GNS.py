T = int(input())
for test_case in range(1, T+1):
    # 값을 넣을 초기 딕셔너리 생성
    num_dict = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    # 문제번호와 갯수가 주어지므로 받아옴 (유의미하진 않음)
    N, M = input().split()
    # 문자열 잘라서 리스트로 받아옴
    str_list = input().split()
    # 리스트 확인하면서 딕셔너리에 값 추가
    for st in str_list:
        num_dict[st] += 1
    print(N)
    # 아이템즈 이용해서 키값과 밸류 다 뽑아내고
    # 밸류 값만큼 키값 반복해서 프린트하기
    for ky, vl in num_dict.items():
        for _ in range(vl):
            print(ky, end=' ')

    print()