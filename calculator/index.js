let input = "";
let first = input;

document.getElementById("num0").onclick = function () {
  input += "0";
  document.getElementById("screeninput").innerHTML = input;
};
document.getElementById("num1").onclick = function () {
  input += "1";
  document.getElementById("screeninput").innerHTML = input;
};
document.getElementById("num2").onclick = function () {
  input += "2";
  document.getElementById("screeninput").innerHTML = input;
};
document.getElementById("num3").onclick = function () {
  input += "3";
  document.getElementById("screeninput").innerHTML = input;
};
document.getElementById("num4").onclick = function () {
  input += "4";
  document.getElementById("screeninput").innerHTML = input;
};
document.getElementById("num5").onclick = function () {
  input += "5";
  document.getElementById("screeninput").innerHTML = input;
};
document.getElementById("num6").onclick = function () {
  input += "6";
  document.getElementById("screeninput").innerHTML = input;
};
document.getElementById("num7").onclick = function () {
  input += "7";
  document.getElementById("screeninput").innerHTML = input;
};
document.getElementById("num8").onclick = function () {
  input += "8";
  document.getElementById("screeninput").innerHTML = input;
};
document.getElementById("num9").onclick = function () {
  input += "9";
  document.getElementById("screeninput").innerHTML = input;
};
document.getElementById("dot").onclick = function () {
  input += ".";
  document.getElementById("screeninput").innerHTML = input;
};
document.getElementById("clear").onclick = function () {
  input = "";
  document.getElementById("screeninput").innerHTML = input;
};

console.log(first);
