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
    if(input_sort=="Latest at Top"){
        for(i=0;i<blog.length;i++){
            if(input_catagory=="" && input_author==""){
                content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
            }
            else if(input_catagory=="" && input_author !=""){

            }
            else if(input_catagory!="" && input_author==""){
                if(blog[i].children[0].children[1].children[2].innerHTML==input_catagory){
                    content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
                }
            }
            else{
                
            }
            
        }
        blogs.innerHTML=content
    }
})