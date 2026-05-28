#Type conversions

#int -> 
# float -> 
# complex -> 
# string -> 
# list -> 
# tuple -> 
# set -> 
# dict -> 
# bool -> 

data_types={ 'a':10, 'b':10.1, 'c':10+1j, 'd':"Hi", 'd_1':"10", "d_2": "10.2",
             'e':[1, 3, 4, 5, 6, 7, 9], 'e_1':['a','d','e','b','c'],
             "f":(1, 3, 4, 5, 6, 7, 9), 'f_1':('a','d','e','b','c'),
             "g":{1, 3, 4, 5, 6, 7, 9}, 'g_1':{'a','d','e','b','c'},
              'h':{'aa':1, 'bb':2, 'cc':3} }

# List of conversions
conversions = [("int", int),
    ("float", float),
    ("complex", complex),
    ("str", str),
    ("list", list),
    ("tuple", tuple),
    ("set", set),
    ("dict", dict),
    ("bool", bool)
]

# Try converting one by one
for i in data_types:
    print(f"\nfor {i} = {data_types[i]}")
    for name, func in conversions:
        try:
            if type(data_types[i]) == func :
                print(f"-SKIPPED -> Already {name} datatype")
                continue
            result = func(data_types[i])
            print(f"-YES -> {name} conversion successful: {result}")
        except Exception as e:
            print(f"-NO -> Cannot convert to {name}")
