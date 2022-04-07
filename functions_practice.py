def hello():
    print("hello!")

hello()
    
def pack( sunscreen, beachball, towel ):
    return[sunscreen, beachball, towel]

print(pack("sunscreen", "beachball", "towel"))


def eat_lunch(my_list):
     if len(my_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_list)):
        if i == 0:
        print(f"First I eat {my_list[0]}")
       else: 
           print(f"Next I eat {my_list[i]}")
        

eat_lunch([])
eat_lunch(["dosa"])
eat_lunch(["dosa", "sandwich", "apples"])




      
