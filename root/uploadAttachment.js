document.getElementById("my-attachment").addEventListener("change", function() {
  config = new Config();
  for (let i = 0; i < this.files.length; i++) {
    config.mediaList.push(this.files[i]);
  }
  return config.mediaList;
});

document
  .getElementById("my-custom-attachment")
  .addEventListener("change", function() {
    let config = new Config()
    let upload_custom_attachment = document.getElementById(
      "upload_custom_attachment"
    );
    let radio_div = document.createElement("div");
    for (let i = 0; i < config.csvHeader.length; i++) {
      let radio = document.createElement("input");
      let radio_label = document.createElement("label");
      let radio_text = document.createTextNode(config.csvHeader[i]);
      radio.type = "radio";
      radio.id = "radio_" + config.csvHeader[i];
      radio.name = "selected_header";
      radio.value = config.csvHeader[i];
      radio_label.setAttribute("for", config.csvHeader[i]);
      radio_label.className = "smaller_text";
      radio_label.appendChild(radio_text);
      radio_div.appendChild(radio);
      radio_div.appendChild(radio_label);
      
      upload_custom_attachment.append(radio_div);
    }
  });
