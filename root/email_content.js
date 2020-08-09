var catcher = document.getElementById("catcher");

/* Hijack form data, use AJAX to send */
catcher.addEventListener("submit", function(evnt) {
  showLoader();
  evnt.preventDefault();
  var formData = new FormData();
  let config = new Config();
  let request = new XMLHttpRequest();
  let subject_field = document.getElementById("subject_field").value;
  let content_field = document.getElementById("input_content").value;
  let targets_csv = document.getElementById("dealCsv").files[0];
  let custom_attachment = document.getElementById("my-custom-attachment")
    .files[0];
  let selected_header = document.querySelector(
    'input[name="selected_header"]:checked'
  );
  selected_header = selected_header ? selected_header.value:'';
  let submitBtn = document.getElementById("testBtn").value;

  formData.append("subject_field", subject_field);
  formData.append("content_field", content_field);
  formData.append("targets_csv", targets_csv);
  formData.append("custom-attachment", custom_attachment);
  formData.append("selected_header", selected_header);
  formData.append("submitBtn", submitBtn);
  config.mediaList.forEach(function(file) {
    formData.append("media", file);
  });

  request.open("POST", "/sendEmails");

  request.onload = res => {
    if (res.target.status == 200) {
      alert("All emails sent");
      catcher.reset();
      location.reload();
    }
  };

  request.send(formData);
});

/* Method to see the sample output */
function seeOutput() {
  let config = new Config();
  let output = document.getElementById("output_content");
  let input = document
    .getElementById("input_content")
    .value.split("\n")
    .join("<br>");
  output.style.display = "block";

  for (let i = 0; i < config.csvFormatedHeader.length; i++) {
    //Replace each ${} with respective sample data
    var searchString = input.search(config.csvFormatedHeader[i]); //Check if any ${} exist
    var changeVariable = input
      .split(config.csvFormatedHeader[i])
      .join(config.csvData[i]);
    input = changeVariable;
  }

  for (let i = 0; i < config.imgFormatedUrl.length; i++) {
    //Replace each ${} with respective sample data
    var searchImage = input.search(config.imgFormatedUrl[i]); //Check if any ${} exist
    var changeVariable = input
      .split(config.imgFormatedUrl[i])
      .join("<img src=" + config.imgUrl[i] + " style='max-width: 100%'>");
    input = changeVariable;
  }

  if (searchString || searchImage) {
    output.innerHTML = changeVariable;
  } else {
    output.innerHTML = input;
  }

  // change status to focus for input content
  document.getElementById("input_content").focus();
}

new UploadCsv();
