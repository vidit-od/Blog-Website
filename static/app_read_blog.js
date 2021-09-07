// declaration
const menu_btn=document.getElementById("menu-btn")
const menu=document.querySelector('.menu')

// open menu btn
menu_btn.addEventListener("click",function(){
    menu.classList.add('toggle')
})
// close menu btn
document.getElementById("close").addEventListener("click",function(){
    document.querySelector(".menu").classList.remove("toggle")
})