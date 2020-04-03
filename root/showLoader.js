function showLoader() {
  let blurBackground = document.createElement("div");
  let contain = document.createElement("div");
  let loader = document.createElement("div");
  let sending = document.createElement("p");
  let sendingMsg = document.createTextNode("Sending...");

  blurBackground.className = "blur_background";
  contain.className = "contain";
  loader.className = "loader";
  contain.style.color = "rgb(76, 102, 175)";

  sending.appendChild(sendingMsg);
  contain.appendChild(loader);
  contain.appendChild(sending);
  blurBackground.appendChild(contain);
  document.querySelector("body").appendChild(blurBackground);
}
