fee_collected=[4500,4200,3000,3500,2800,3500]
//find total fee collected
let totalfee=0
for(let i=0;i<fee_collected.length;i++)
{
    totalfee=totalfee+fee_collected[i]
}
console.log("totalfee = ",totalfee);

//"for of loop" used with array to access without depending on index
for(fee of fee_collected)
{
    console.log(fee);
}