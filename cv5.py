def my_max(numbers):
    if numbers == []:
        return print("in numbers is nothing")
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

def flatten(lists):
    new_list = []
    for l in lists:
        for k in l:
            new_list.append(k)
    return new_list

def dummy(text, rubbish):
    """
    dum = ""
    for t in text[:-1]:
        dum += t + rubbish
    dum += text[len(text)-1]
    return dum
    """
    return rubbish.join(text)
 
def reverse(text):                          
    a = list(text.upper())
    r = []
    for t in a[::-1]:
        r.append(t)
    return "".join(r)
        
def palindrom(text):
    if text.upper() == reverse(text):
        return True
    
        
