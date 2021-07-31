def f():
    global s
    print("1st print : ", s)
    s = "I love python!"
    print("2nd print : ", s)


s = "Python is great!"
f()
print("3rd print : ", s)
