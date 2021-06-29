const hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"];

document.addEventListener("DOMContentLoaded", function () {
  const button = document.getElementById("btn");
  const color = document.querySelector(".color");

  button.onclick = function () {
    let hexColor = "#";

    for (let i = 0; i < 6; i++) {
      let randomNum = Math.floor(Math.random() * hex.length);
      hexColor += hex[randomNum];
    }
    color.textContent = hexColor;
    document.body.style.backgroundColor = hexColor;
  };
});
