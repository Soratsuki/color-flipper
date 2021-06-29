const colors = ["green", "red", "rgba(133,122,200)", "#f15025"];

document.addEventListener("DOMContentLoaded", function () {
  const button = document.getElementById("btn");
  const color = document.querySelector(".color");

  button.onclick = function () {
    //get random number between 0 and 3 for colors[i]
    const randomNum = Math.floor(Math.random() * colors.length);
    document.body.style.backgroundColor = colors[randomNum];
    color.textContent = colors[randomNum];
  };
});
