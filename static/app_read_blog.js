const menu_btn=document.getElementById("menu-btn")
const menu=document.querySelector('.menu')

menu_btn.addEventListener("click",function(){
    menu.classList.add('toggle')
})

document.getElementById("close").addEventListener("click",function(){
    document.querySelector(".menu").classList.remove("toggle")
})