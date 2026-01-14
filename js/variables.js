//ES6-const,let
num1 = 10;
console.log(num1);
let num2 = 20;
const num3 = 30;
num1 = 11
num2 = 21
//num3 = 31
var num1=20
//let num2=30
//const num3=40
//2.only var allows redecleration

if(true)
{
    var x =10
    let y=20
    const z=30
    console.log("Inside the block");
    console.log("x",x);
    console.log("y",y);
    console.log("z",z);
}
console.log("Outside the block");
console.log("x",x);
console.log("y",y);
console.log("z",z);