def Val_change(argv, Code, N = 1, F=0 , E=-1 ):
    # argv의 리스트 타입인지 확인하여 리스트 타입이 아닌경우 리스트로 변경
    argv = list_check(argv)

    # 각각 분할된 리스트를 N단위로 합침
    argv = Val_Number(argv, N)

    # 변환 범위, 초기값 전 범위
    F = Limit_Num(argv,F)
    E = Limit_Num(argv,E)

    # 확인용
    # print("argv: ", argv)
    # print("Code: ", Code)
    # print("F: ", F, " E: ", E)

    # 들어온 코드를 범위에 맞춰 해당위치 코드를 argv에 넣음
    for i in range(F, E):
        if int(argv[i]) <= len(Code):
            argv[i] = Code[int(argv[i])]
    Temp =""
    for i in argv:
        Temp = Temp + str(i)

    # print("Temp:", Temp)
    return Temp

def Limit_Num(args, num):
    if len(args) < num or num < 0:
        num = len(args)
    return num

def Val_Number(args, n):
    Data_List = []
    if(type(args) == list):
        for i in range(0, len(args), n):
            Temp = ""
            for j in range(i, i + n):
                if(j<len(args)):
                    Temp = Temp + args[j]
            Data_List.append((Temp))
    return Data_List

def list_check(argv):
    if type(argv) != 'list':
        argv = list(argv)
    return argv

def Str_Int(argv):
    argv = list_check(argv)
    for i in range(0,len(argv)):
        argv[i]=str(ord(argv[i])-48)
    return argv


# if __name__ == "__main__":

    # Name = list(range(48, 123))
    # Year = ['J', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    # Month = ['', 'L', 'A', 'S', 'E', 'R', 'O', 'P', 'T', '2', 'K', 'N', 'D']
    #
    # a ='1'
    #
    # print(list(range(1,1)))
    # print("a   :", list(a))
    #
    # a = Str_Int(a)
    # print("a2  :",a)
    # print("Name:", Name)
    #
    # val = Val_change(a, Year, 1 , 2,3)
    #
    # print("Val :",val)
    # print(type(val))

