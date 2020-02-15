import os

files = os.listdir("./public")

htmls = []
for html_name in files:
    if '.html' in html_name:
        htmls.append(html_name)

for html in htmls:
    html_name = html.split(".")[0]
    print(html_name)
