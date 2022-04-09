#name_args
def name_args(**kwargs):
    for i in kwargs.keys():
        print(f"{i}:{kwargs[i]}")
name_args(stuff1="one", stuff2 ='two', stuff3 = "three", stuff4=5)

#all_true
def all_true(iter):
    return all (iter)

def all_true(iterable):
    return all(iterable)

print(all_true([True,(True),False]))
print(all_true((True, False)))
print(all_true("True"))
print(all_true("A"))

#one_true
def one_true(iterable):
    return any(iterable)

print(one_true([False,(True),False]))




    
