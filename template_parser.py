import re


def pass_data_into_template(data):
    with open("template.txt", 'r') as f:
        # get all the line in the text file
        lines = f.readlines()
        output = []
        for line in lines:
            # search for ${ any words }
            results = re.findall("\${.+?}", line)
            for result in results:
                # remove ${ }
                required_data = re.sub("\${", "", result, 1)
                required_data = re.sub("}", "", required_data, 1)

                # see if the template required data matches in the dictionary passed down
                if data.get(required_data, False) != False:
                    line = line.replace(result, data[required_data])
                    # only append when there is no match anymore, to avoid duplicate
                    if not re.findall("\${.+?}", line):
                        output.append(line)
                else:
                    # if the data is not found in dictionary, prompt error not found
                    raise KeyError(f"{result} not found in csv column")
        print(output)


pass_data_into_template(
    {"name": "rain", "phone": "0177098867", "email": "rainchai4240@gmail.com"})
