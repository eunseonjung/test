#입력
for _ in range(3):
#처리
  #개수 세기-리스트.count("1") 방법
  li_num=[]
  a1, a2, a3, a4= input().split()
  li_num.append(a1)
  li_num.append(a2)
  li_num.append(a3)
  li_num.append(a4)

  #1 개수 읽기
  count_ones=li_num.count("1")
#조건 & 출력  
  #등 한 개->걸->C
  if count_ones ==1:
    print('C')
  #등 두 개->개->B
  elif count_ones ==2:
    print('B')
  #등 세 개->도->A
  elif count_ones ==3:
    print('A')
  #등 네 개->모->E
  elif count_ones==4:
    print('E')
  #등 0개 ->윷->D
  elif count_ones==0:
    print('D')
