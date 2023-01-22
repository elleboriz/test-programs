/*
*Solution for value screen overlaping through javascript*


Fixing the problem of values of calculator screen overlaping 
either by setting a format for value above screen size or by
limiting the size of the number the calculator should support .
*/
let cal_screen="" ;

let input_one ;
let input_two ;
let operation ;
let result ;

// Funtions for evaluation of the diffrent operations
// returns: evaluated result

function add(x,y){
   sol = x + y;
   return toString(sol);
 }
function subtract(x,y){
  return x - y;
}
function multiply(x,y){
  return x * y;
}
function divide(x,y){
  result = x / y;
  result = Math.round(result * 10) / 10;
  return result;
}
function add(x,y) {
  return x+y;
} 

//  equal button implementation for diffent oprator results

document.getElementById("equal").onclick = function () {
  if (operation == "+"){
  input_two = Number(cal_screen);
  console.log(operation);  
  console.log(input_one);
   cal_screen = add(input_one,input_two);
  }
  else if(operation == "-") {
    input_two = Number(cal_screen);
    console.log(operation);  
    console.log(input_one);
     cal_screen = subtract(input_one,input_two);
  }
  else if(operation == "x") {
    input_two = Number(cal_screen);
    console.log(operation);  
    console.log(input_one);
     cal_screen = multiply(input_one,input_two);
  }
  else if(operation == "/") {
    input_two = Number(cal_screen);
    console.log(operation);  
    console.log(input_one);
     cal_screen = divide(input_one,input_two);
  }
  else{
    cal_screen = "Error"
  }
  document.getElementById("screeninput").innerHTML =cal_screen;
}


// decleration of diffrent numerical buttons bottuns


document.getElementById("num0").onclick = function () {
  cal_screen += "0";
  document.getElementById("screeninput").innerHTML = cal_screen;
}
document.getElementById("num1").onclick = function () {
  cal_screen += "1";
  document.getElementById("screeninput").innerHTML = cal_screen;
}
document.getElementById("num2").onclick = function () {
  cal_screen += "2";
  document.getElementById("screeninput").innerHTML = cal_screen;
}
document.getElementById("num3").onclick = function () {
  cal_screen += "3";
  document.getElementById("screeninput").innerHTML = cal_screen;
}
document.getElementById("num4").onclick = function () {
  cal_screen += "4";
  document.getElementById("screeninput").innerHTML = cal_screen;
}
document.getElementById("num5").onclick = function () {
  cal_screen += "5";
  document.getElementById("screeninput").innerHTML = cal_screen;
}
document.getElementById("num6").onclick = function () {
  cal_screen += "6";
  document.getElementById("screeninput").innerHTML = cal_screen;
}
document.getElementById("num7").onclick = function () {
  cal_screen += "7";
  document.getElementById("screeninput").innerHTML = cal_screen;
}
document.getElementById("num8").onclick = function () {
  cal_screen += "8";
  document.getElementById("screeninput").innerHTML = cal_screen;
}
document.getElementById("num9").onclick = function () {
  cal_screen += "9";
  document.getElementById("screeninput").innerHTML = cal_screen;
}
document.getElementById("dot").onclick = function () {
  cal_screen += ".";
  document.getElementById("screeninput").innerHTML = cal_screen;
}


document.getElementById("clear").onclick = function () {
  
  cal_screen = "";
  input_one = 0 ;
  input_two = 0 ;
  document.getElementById("screeninput").innerHTML = cal_screen;
}

//decleration for diffrent operator buttons


document.getElementById("divide").onclick = function () {
  operation = "/";
  input_one = Number(cal_screen);
  cal_screen = '';
   
  document.getElementById("screeninput").innerHTML = cal_screen;
}
document.getElementById("multiply").onclick = function () {
  operation = "x";
  input_one = Number(cal_screen);
  cal_screen = '';
   
  document.getElementById("screeninput").innerHTML = cal_screen;
}
document.getElementById("subtract").onclick = function () {
  operation = "-";
  input_one = Number(cal_screen);
  cal_screen = '';
   
  document.getElementById("screeninput").innerHTML = cal_screen;
}

document.getElementById("add").onclick = function () {
  operation = "+";
  input_one = Number(cal_screen);
  cal_screen = '';
   
  document.getElementById("screeninput").innerHTML = cal_screen;
}






