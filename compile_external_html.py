import re
import os

ROOT = os.path.dirname(os.path.realpath(__file__)) + \
    '\\root\\'
OUTPUT = os.path.dirname(os.path.realpath(__file__)) + '\\static\\'


def replace_element(search_result, html_filename):
    filename = search_result.group().replace("\"", "")
    start, end = search_result.span()
    data = ""
    with open(ROOT+filename, 'r') as f:
        for line in f.readlines():
            data += line
        target = OUTPUT + \
            html_filename if os.path.isfile(
                OUTPUT+html_filename) else ROOT+html_filename
        with open(target, 'r') as g:
            html = ""
            for line in g.readlines():
                html += line

            css_result = re.search(f'<link.*"{filename}".*>', html)
            js_result = re.search(f'<script.*"{filename}".*>', html)

            result = css_result or js_result
            if not result:
                return
            start, end = result.span()
            with open(ROOT+filename, 'r') as h:
                h_string = ""

                for line in h.readlines():
                    h_string += line

                if '.css' in filename:
                    h_string = "<style>"+h_string+"</style>"
                elif '.js' in filename:
                    h_string = "<script>"+h_string+"</script>"

                html = html.replace(html[start:end], h_string)

                print("Compiling", ROOT+filename, "into",
                      OUTPUT+html_filename)
                with open(OUTPUT+html_filename, 'w') as j:
                    j.writelines(html)


def compile_html(html_filename):
    with open(ROOT+html_filename, 'r') as f:
        for line in f.readlines():
            start, end, result = '', '', ''
            css_tag = '<link'
            js_tag = '<script'
            if css_tag in line or js_tag in line:
                css_search_result = re.search('"\w{1,}.css"', line)
                js_search_result = re.search(
                    '"\w{1,}.js"', line)
                result = css_search_result or js_search_result

            if result:
                replace_element(result, html_filename)


def main():
    for filename in os.listdir(ROOT):
        if '.html' in filename:
            compile_html(filename)


if __name__ == "__main__":
    main()
