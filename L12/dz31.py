import re
import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, "r", encoding="utf-8") as html:
        doc = html.read()
        res = re.sub(r'\<[^>]*\>', '', doc)
        res = re.sub(r' {2,100}', '', res)
        print(res.split("\n"))
        s = res.split("\n")
        result = []
        for q in s:
            if q:
                result.extend(q + "\n")

    with open(result_file, "w", encoding="utf-8") as res_file:
        res_file.write("".join(result))
delete_html_tags(html_file="draft.html")
