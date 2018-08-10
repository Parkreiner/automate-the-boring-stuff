'''
Just trying to implement the methods so that I understand how they work
'''
def my_startswith(s_main, s_sub):
    if s_main[0:len(s_sub)] == s_sub:
        return True
    return False

def my_endswith(s_main, s_sub):
    if s_main[len(s_main) - len(s_sub):] == s_sub:
        return True
    return False

print(my_startswith("Example string", "Example"))
print(my_endswith("Cool beans", "beans"))