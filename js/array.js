let marks=[45,67,34,12]
let users=['arun','amal','anu','neena']
let stud1=['arun',47,'pass']

//access
console.log(marks[0]);
console.log(marks[1]);
console.log("marks array",marks);

//update
marks[0]=55
console.log("marks array after update",marks);

//new values will be added to index 4
marks[4]=100
console.log("marks array after new value",marks);
marks[10]=77
console.log("marks array after new value",marks);

//deletion
delete marks[0]
console.log("marks array after deletion",marks);

//push and pop
marks.pop()
console.log("marks array after pop", marks);
marks.push(15)
console.log("marks array after push", marks);

//shift and unshift
marks.shift()
console.log("marks array after shift", marks);
marks.unshift(20)
console.log("marks array after unshift", marks);

