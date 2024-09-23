calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    string1 = []
    len_ = len(string)
    up_ = string.upper()
    lo_ = string.lower()
    string1.append(len_)
    string1.append(up_)
    string1.append(lo_)
    string = tuple(string1)
    count_calls()
    return string

def is_contains(string, list_to_search):
    string = string.lower()
    for i in list_to_search:
        s = i.lower()
        is_true = False
        if s == string:
            is_true = True
            break
    count_calls()
    return is_true

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
