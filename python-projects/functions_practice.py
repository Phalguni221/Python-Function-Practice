#function that prints "hello!"
def hello():

    print("hello!")

hello()

#function that packs items for beach trip
def pack( sunscreen, beachball, towel ):
    return[sunscreen, beachball, towel]

print(pack("sunscreen", "beachball", "towel"))


#function that will instruct to eat or not to eat lunch

def eat_lunch(my_lunchlist):
  if len(my_lunchlist) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lunchlist)):
      if i == 0:
        print(f"First I eat {my_lunchlist[0]}")
      else:
        print(f"Next I eat {my_lunchlist[i]}")

     

      
eat_lunch([])
eat_lunch(["banana","sandwich","cookie", "juice"])
