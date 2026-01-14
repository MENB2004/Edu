/*let i=1
while(i<=10)
{
    document.writeln(`<h3>${i}</h3>`)
    i++
}

//Read a number(n) from user and find sum of 1 to n
let n=1
let num = Number(prompt("Enter a number"));
let sum=0;
while(n<=num)
{
    sum=sum+n
    n++
}
document.writeln(sum)*/

//Read a number(n) from user and find sum of even numbers from 1 to n
let n = 1
let num = Number(prompt("Enter a number"));
let sum = 0;
while (n <= num) {

    if (n % 2 == 0) {
        sum = sum + n
        n++
    }
    else {
        n++
    }
}
document.writeln(sum)