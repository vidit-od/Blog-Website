const catagory=document.querySelectorAll(".catagory")
const catagory_select=document.querySelector(".catagory_select")
let catagory_list=[]
const form=document.querySelector(".form")
const submit=document.querySelector(".submit")
const blog=document.querySelectorAll(".blog")
const blogs=document.querySelector(".blogs")
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

submit.addEventListener("click",function(){
    const input_catagory= document.getElementById("catagory_select").value
    const input_sort=document.getElementById("sort").value
    const input_author=document.getElementById("author").value
    let content=""
    let loop = 0
    if(input_sort=="Latest at Top"){
        for(i=0;i<blog.length;i++){
            if(input_catagory=="" && input_author==""){
                loop=1
                content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
            }
            else if(input_catagory=="" && input_author !=""){
                loop=2
                if(blog[i].children[0].children[1].children[0].innerHTML==input_author){
                    content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
                }
            }
            else if(input_catagory!="" && input_author==""){
                loop=3
                if(blog[i].children[0].children[1].children[2].innerHTML==input_catagory){
                    content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
                }
            }
            else{
                loop=4
               if((blog[i].children[0].children[1].children[2].innerHTML==input_catagory) && (blog[i].children[0].children[1].children[0].innerHTML==input_author)){
                content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
               }
            }
            
        }
        if (content==""){
            content=`<h3> No Results Found For this Filter </h3>`
        }
        if (loop==1){
            document.querySelector(".section-title").innerHTML=' Recently Published'
        }
        else{
            document.querySelector(".section-title").innerHTML=' Filtered Results'
        }
        blogs.innerHTML=content
    }
    else{
        for(i=blog.length-1;i>=0;i--){
            if(input_catagory=="" && input_author==""){
                loop=1
                content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
            }
            else if(input_catagory=="" && input_author !=""){
                loop=2
                if(blog[i].children[0].children[1].children[0].innerHTML==input_author){
                    content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
                }
            }
            else if(input_catagory!="" && input_author==""){
                loop=3
                if(blog[i].children[0].children[1].children[2].innerHTML==input_catagory){
                    content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
                }
            }
            else{
                loop=4
                if((blog[i].children[0].children[1].children[2].innerHTML==input_catagory) && (blog[i].children[0].children[1].children[0].innerHTML==input_author)){
                content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
               }
            }
        }
        if (content==""){
            content=`<h3> No Results Found For this Filter </h3>`
        }
        if (loop==1){
            document.querySelector(".section-title").innerHTML=' Recently Published'
        }
        else{
            document.querySelector(".section-title").innerHTML=' Filtered Results'
        }
        blogs.innerHTML=content
    }
})