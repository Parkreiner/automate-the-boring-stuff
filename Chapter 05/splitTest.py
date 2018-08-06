test = "This is a string."
testArray = test.split(" ") # Returns four-element array

print(testArray)

if not testArray[4]:
    print("Test result: This does not work.")