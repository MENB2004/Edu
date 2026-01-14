var num = Number(prompt("Enter a number"));
if(num>0 && num<1000)
{
    document.writeln("No Discount. If they purchase more than 1000, they will get a discount");
    document.writeln("They need to pay ", num);
    document.writeln("If they purchase more than 1000, they will get a discount");
}
else if(num>1000 &&num<3000)
{
    document.writeln("They have a discount of 5%. They need to pay only ", num-num*0.05);
}
else if(num>3000 && num<6000)
{
    document.writeln("They have a discount of 10%. They need to pay only ", num-num*0.1);
}
else
{
    document.writeln("They have a discount of 15%. They need to pay only ", num-num*0.15);
}