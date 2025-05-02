def dict_to_string(d):
    text = ""  # 用來存最後的字串

    for key in d:
        value = d[key]
        pair = str(key) + ":" + str(value)  # 把 key 和 value 變成字串加在一起

        if text == "":
            text = pair  # 第一次就直接放進去
        else:
            text = text + ", " + pair  # 之後都加逗號和空格再接上去

    return text
print(dict_to_string({'a': 1, 'b': 2}))