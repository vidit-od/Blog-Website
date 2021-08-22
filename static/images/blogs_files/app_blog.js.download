let catagory=document.querySelectorAll(".catagory")
let catagory_list=[]
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
    console.log(catagory_list)
})