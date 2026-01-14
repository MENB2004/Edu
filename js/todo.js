const additem = () => {

    //Step1. Read user input from textbox
    let userinput = document.querySelector("#inp").value

    //Step2. Create list item
    let listitem = document.createElement("li")
    listitem.textContent = userinput

    //Step3. Target the List
    let list = document.querySelector("#todo")

    //Step4. Add item to the list
    list.appendChild(listitem)
    console.log(listitem);
}
let btn = document.querySelector("#btn")
//document.getElementId("btn")
btn.addEventListener("click", additem)
