import re

template = "${name} ${email} ${name} ${name} ${name}"
data = ["Rain", "rainchai4240@gmail.com"]
columns = ["name", "email"]
request = {
    "media": [
        {"filename": "1.png"}
    ]
}


def convert_into_html(template, data, columns, **kwargs):

    def get_media_file(media_name):
        # return the <img> tag for the media_name
        for i in range(len(kwargs['media_files']['media'])):
            if kwargs['media_files']['media'][i]['filename'] == media_name:
                media_name = media_name.replace(" ", "")
                output = '<p><img src="cid:'+media_name+'" width="500" height="500"></p>'
                return output

    output_data = {}
    for i in range(len(columns)):
        output_data[columns[i]] = data[i]

    lines = template.splitlines()
    output = []
    for line in lines:
        # search for ${ any words }
        results = re.findall("\${.+?}", line)
        for result in results:
            # remove ${ }
            required_data = re.sub("\${", "", result, 1)
            required_data = re.sub("}", "", required_data, 1)

            # if its a media, [] exists
            if re.search('[.*]', result):
                required_data = required_data.replace("[", "").replace("]", "")
                media = get_media_file(required_data)
                line = line.replace(result, media, 1)
                if not re.findall("\${[.+?]}", line):
                    output.append(line)

            # see if the template required data matches in the dictionary passed down
            if output_data.get(required_data, False) != False:
                line = line.replace(result, output_data[required_data], 1)
                # only append when there is no match anymore, to avoid duplicate
                if not re.findall("\${.+?}", line):
                    output.append(line)
    output_html = ""
    print(output)
    for line in output:
        output_html += line+"\n"
    return output_html


convert_into_html(template, data, columns, media_files=request)
