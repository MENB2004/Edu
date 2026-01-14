//Read number from user and display odd or even
var num1 = Number(prompt("Enter a number"));
var num2 = Number(prompt("Enter 2nd number"));
var num3 = Number(prompt("Enter 3rd number"));
if (num1 > num2 && num1 > num3) {
    document.writeln(num1, " is higher than ", num2, "and ", num3);
}
else if (num2 > num3) {
    document.writeln(num2, " is higher than ", num1, "and ", num3);
}
else {
    document.writeln(num3, " is higher than ", num1, "and ", num2);
}