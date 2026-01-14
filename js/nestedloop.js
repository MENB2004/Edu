/*for(let i=10;i>=5;i--)
{
    for(let j=1;j<=3;j++)
    {
        console.log("hello");
    }
}*/

//pattern

for(let i=1;i<=5;i++)
{
    for(let j=1;j<=i;j++)
    {
        document.writeln("*");
    }
     document.writeln("<br>");
}

document.writeln("<br>");

for(let i=5;i>=1;i--)
{
    for(let j=1;j<=i;j++)
    {
        document.writeln("#");
    }
     document.writeln("<br>");
}

document.writeln("<br>");

for(let i=1;i<=5;i++)
{
    
    for(let j=1;j<=i;j++)
    {
        document.writeln(`${i}`);
    }
     document.writeln("<br>");
}