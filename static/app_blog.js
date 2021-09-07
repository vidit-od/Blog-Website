// declaration
const catagory=document.querySelectorAll(".catagory")
const catagory_select=document.querySelector(".catagory_select")
const form=document.querySelector(".form")
const blog=document.querySelectorAll(".blog")
const blogs=document.querySelector(".blogs")
const scroll_to_top=document.querySelector(".scroll_to_top")
const pages=document.querySelector(".page")
const page_left=document.querySelector(".page_left")
const page_right=document.querySelector(".page_right")

// universal variables
let current_page=1
let catagory_list=[]
let max_blogs=4
    
// loading content on page
window.addEventListener('DOMContentLoaded',function(){
    // when website loads we dont want scroll to top button, we want it after certain scroll
    scroll_to_top.classList.add("hide")
    

    // creating the pages functionality on blogs's home page ; more blogs cause large scroll times which is inefficient
    blog_assignment(current_page,max_blogs)
})

// appear a scrool to top button if scrolled below certain level
window.addEventListener("scroll",function(){
    if(window.pageYOffset>150){
        document.querySelector('.menu-btn_second').classList.add('appear')
    }
    else{
        document.querySelector('.menu-btn_second').classList.remove('appear')
    }
    if(window.pageYOffset>300){
        scroll_to_top.classList.remove("hide")
    }
    else{
        scroll_to_top.classList.add("hide")
    }
})


// to close menu bar
document.getElementById("close").addEventListener("click",function(){
    document.querySelector(".menu").classList.remove("toggle")
})

// to open menu bar
document.querySelector(".menu-btn").addEventListener("click",function(){
    document.querySelector(".menu").classList.add("toggle")
})
document.querySelector(".menu-btn_second").addEventListener("click",function(){
    document.querySelector(".menu").classList.add("toggle")
})

// go to previous page
page_left.addEventListener("click",function(){
    if(current_page!=1){
        current_page=current_page-1
    }
    blog_assignment(current_page,max_blogs)
})
// go to next page
page_right.addEventListener("click",function(){
    if(current_page!=Math.ceil(blog.length/max_blogs)){
        current_page+=1
    }
    blog_assignment(current_page,max_blogs)
})

function blog_assignment(current_page,max_blogs){
    if(blog.length>max_blogs){
        remain=blog.length/max_blogs
        remain=Math.ceil(remain)
        content=""
        for(i=1;i<=remain;i++){
            if(i==current_page){
                content=content+`<p     style="color:green">${i}</p>`    
            }
            else{
                content=content+`<p>${i}</p>`
            }
        }
        pages.innerHTML=content

        // lower limit :((current_page-1)*max_blogs)+1
        // upper limit :current_page*max_blogs

        page_content=''
        for(i=0;i<blog.length;i++){
            if((i>=((current_page-1)*max_blogs))&&(i<current_page*max_blogs)){
                page_content=page_content+'<div class="blog">'+blog[i].innerHTML+'</div>'
            }
        }
        blogs.innerHTML=page_content
    }
    else{
        document.querySelector(".pages").style.opacity=0
    }
}