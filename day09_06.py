ss='파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠. ^^'
print(ss.count('공부'))
print(ss.find('공부'))
print(ss.rfind('공부'))
print(ss.rfind('공부',5))
print(ss.find('없다'))
print(ss.index('공부'))
print(ss.startswith('파이썬'))
print(ss.endswith('^^'))
print(ss.startswith('파이썬',5))
print("")

index = 0
while(1):
    print(ss.index('공부',index+1))
    index=ss.index('공부',index+1)
    if((ss.index('공부',index+1))==NULL):
        break;

print(ss.index('공부',21))
    
