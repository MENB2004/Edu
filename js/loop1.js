/*
for(init;cond;upd)
{
    body of the loop
}
for (let i = 1; i <= 10; i++) {
    document.write(`<h3>${i}</h3>`)
}*/

//print 100 to 1

/*for (let i = 100; i >= 1; i--) {
    document.write(`<h3>${i}</h3>`)
}

//even number between 100 to 1

for (let i = 100; i >= 1; i--) {
if(i%2==0)
{
    document.writeln(`<h3>${i}</h3>`)
}
}*/

//even numbers between 100 and 1 except multpiles of 4 and 5

/*for (let i = 100; i >= 1; i--) {
if(i%2==0 && i%4!=0 && i%5!==0)
{
    document.writeln(`<h3>${i}</h3>`)
}
}*/

for(let i=1;i<=10;i++)
{
    if(i==5)
        break
    document.writeln(`<h3>${i}</h3>`)
}