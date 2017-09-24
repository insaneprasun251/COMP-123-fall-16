numBottles = input("How many bottles? ")

numBottles = int(numBottles)

for bottles in range(numBottles, 0 , -1):
    print(bottles, "bottles of beer on the wall,")
    print(bottles, "bottles of beer,")
    print("You take one down, you pass it around,")
    print(bottles - 1, "bottles of beer on the wall!")
    print()
print("No more bottles of beer on the wall!")