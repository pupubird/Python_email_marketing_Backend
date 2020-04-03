class UploadCsv {
    constructor() {
        this.Config = new Config()
        let input = document.getElementById("dealCsv");
        input.addEventListener("change", (e) => {
            if (input.files && input.files[0]) {
            var myFile = input.files[0];
            var reader = new FileReader();

            reader.addEventListener("load", (e) => {
                let csvdata = e.target.result;
                this.createHeaderBtn(csvdata); // calling function for parse csv data
            });

            reader.readAsBinaryString(myFile);
            }
        });

    }
    createHeaderBtn(data) {
        let parsedata = [];

        let newLinebrk = data.split("\n");
        for (let i = 0; i < newLinebrk.length; i++) {
            parsedata.push(newLinebrk[i].split(","));
        }

        /* Generate button based on parsedata */
        for (let i = 0; i < parsedata[0].length; i++) {
            let button = document.createElement("input");
            let tempHeader = parsedata[0][i];
            let tempData = parsedata[1][i];
            tempHeader = tempHeader.split("\r").join("")
            tempHeader = tempHeader.split("\n").join("")
            let formatedHeader = "${" + tempHeader + "}";

            this.Config.csvHeader.push(tempHeader);
            this.Config.csvFormatedHeader.push(formatedHeader);
            this.Config.csvData.push(tempData);
            
            button.type = "button";
            button.id = i;
            button.value = tempHeader;
            button.onclick = function() {
            insertAtCaret("input_content", formatedHeader);
            seeOutput()
            };
            document.getElementById("varFromCsv").append(button);
        }
        return this.Config.csvData, this.Config.csvHeader, this.Config.csvFormatedHeader;
    };
}