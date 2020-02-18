import re


def pass_data_into_template(data, columns):
    # create dict that matches columns
    columns = columns.split(',')
    data = data.split(',')

    output_data = {}
    for i in range(len(columns)):
        output_data[columns[i]] = data[i]
    with open("sample/template.txt", 'r') as f:
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
                if output_data.get(required_data, False) != False:
                    line = line.replace(result, output_data[required_data])
                    # only append when there is no match anymore, to avoid duplicate
                    if not re.findall("\${.+?}", line):
                        output.append(line)
                else:
                    # if the data is not found in dictionary, prompt error not found
                    raise KeyError(f"{result} not found in csv column")
        return output
