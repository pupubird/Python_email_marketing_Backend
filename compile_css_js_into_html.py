import os
import re
ROOT = "./public"
TARGET = "./static"


def main():
    files = os.listdir(ROOT)

    htmls = []
    for file_name in files:
        if '.html' in file_name:
            htmls.append(file_name)
    for html in htmls:
        for file_name in files:
            insert_into_html(file_name, html)


def insert_into_html(file_name, html):
    name1 = file_name.split(".")[0]
    name2 = html.split(".")[0]

    if name1 != name2:  # return if its not the same
        return

    tag, target = "", ""

    if 'css' in file_name:
        tag = "style"
        target = "</head>"
    elif 'js' in file_name:
        tag = "script"
        target = "</body>"
    elif 'html' in file_name:
        return

    with open(ROOT+"/"+file_name, 'r') as f:
        output = ""
        for line in f.readlines():
            output += line
        output_template = f"<{tag}>{output}</{tag}>"

        files = os.listdir(TARGET)
        if html in files:
            g = open(TARGET+"/"+html, 'r')
            print("Compiling", TARGET+"/"+file_name, "into", html)
        else:
            g = open(ROOT+"/"+html, 'r')
            print("Compiling", ROOT+"/"+file_name, "into", html)

        html_string = ""
        for line in g.readlines():
            html_string += line

        index_head = html_string.index(target)
        html_string = html_string[:index_head] + \
            output_template + html_string[index_head:]

        with open(TARGET+"/"+html, 'w') as h:
            h.writelines(html_string)
        g.close()


if __name__ == "__main__":
    main()
