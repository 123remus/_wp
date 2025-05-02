def classify_even_odd(num):
    result={'even':[],'odd':[]}
    for i in num:
        if i%2==0:
            result['even'].append(i)
        else:
            result['odd'].append(i)
    return result
print(classify_even_odd([5,7,51,36,8,54,33,12]))  