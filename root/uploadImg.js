let imageInput = document
  .getElementById("my-image")
  .addEventListener("change", uploadImg);

function uploadImg() {
  let config = new Config();
  /* Method to create Image button */
    for (let i = 0; i < this.files.length; i++) {
        if (this.files && this.files[i].name) {
        config.imgUrl.push(URL.createObjectURL(this.files[i])); // set src to blob url
        let button = document.createElement("input");
        let imgName = this.files[i].name;
        let formatedImageTag = "${[" + imgName + "]}";

        config.mediaList.push(this.files[i]);
        config.imgFormatedUrl.push(formatedImageTag);
        button.type = "button";
        button.id = imgName;
        button.value = imgName;
        button.onclick = function() {
            insertAtCaret("input_content", formatedImageTag);
            seeOutput()
        };
        document.getElementById("varFromCsv").append(button);
        }
    }
}
