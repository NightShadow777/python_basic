def popular_words(text, keywords):
    text_list = text.split()
    res_dict = {}
    for text in text_list:
        for keyword in keywords:
            if keyword == text.lower():
                #print(text_list)
                n = text_list.count(text)
                res_dict[keyword] = n
            else:
                if not res_dict.get(keyword):
                    res_dict[keyword] = 0
    return res_dict

print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
print(popular_words('''Interesting Facts For Curious Minds gives you the answer to all these and many many more questions that I know have crossed your mind from time to time . This book is divided into 63 chapters by topic for your convenience, bringing you a nice mix of science, history, pop culture, and all sorts of stuff in between. Each chapter contains 25 concise yet engaging factoids that are sure to make you think and at times laugh. ''', ['many', 'time', 'book', 'read']))