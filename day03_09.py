money = 0
c500 = 0
c100 = 0
c50 = 0
c1 = 0

money=int(input("How much is the exchanging money?"))

c500 = money/500
money %= 500

c100 = money/100
money %= 100

c50 = money/50
money %= 50

c10 = money/10
money %= 10

print("\n\\500 ==> x%d"%c500)
print("\\100 ==> x%d"%c100)
print("\\50 ==> x%d"%c50)
print("\\10 ==> x%d"%c10)
print("Lefted money ==> \\%d"%money)
