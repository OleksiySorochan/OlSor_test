def popular_lit(st):
    if type(st) == type('st'):
        res = 0
        lit = ''
        for l in st:
            if res < st.count(l):
                lit = l
                res = st.count(l)
        return f"The most popular litera is: {lit}, used {res} times"
    else:
        return "only 'str' type argument"


text = "Lorem Ipsum is simply dummy text"
print(popular_lit(text))