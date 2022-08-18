menu = "1번 메뉴 : 아이스아메리카노\n2번 메뉴 : 얼그레이\n3번 메뉴 : 카푸치노\n4번 메뉴 : 복숭아티"

menu1="""
1번 메뉴 : 아이스아메리카노
2번 메뉴 : 얼그레이
3번 메뉴 : 카푸치노
4번 메뉴 : 복숭아티
"""

print(menu)
print(menu1)

menu1="1번 메뉴 : 아이스아메리카노"
menu2="2번 메뉴 : 얼그레이"
menu3="3번 메뉴 : 카푸치노"
menu4="4번 메뉴 : 복숭아티"

menu=menu1+menu2+menu3+menu4
print(menu)

newmenu = menu1+"\n"+menu2+"\n"+menu3+"\n"+menu4+"\n"
print(newmenu)
newmenu *= 2
print(newmenu)
