const catagory=document.querySelectorAll(".catagory")
const catagory_select=document.querySelector(".catagory_select")
let catagory_list=[]
const submit=document.getElementById("submit")
window.addEventListener('DOMContentLoaded',function(){
    for (i=0;i<catagory.length;i++){
        if (i==0){
            catagory_list.push(catagory[i].innerHTML)
        }
        else if(!(catagory_list.includes(catagory[i].innerHTML))){
            console.log(catagory[i])
            catagory_list.push(catagory[i].innerHTML)
        }
    }
    let line=`<option value=""></option>`
    for(i=0;i<catagory_list.length;i++){
        line=line+`<option value="${catagory_list[i]}">${catagory_list[i]}</option>`
    }
    console.log(catagory_select.innerHTML)
    catagory_select.innerHTML=line
})