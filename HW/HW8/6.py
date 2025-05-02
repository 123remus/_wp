def count_chars(char):
    result = {} 
    for i in char:
        if i in result:
            result[i] += 1  # 已經有這個字元，就加 1
        else:
            result[i] = 1   # 第一次出現這個字元，設為 1

    return result 
print(count_chars("hello"))  