// declaration
const catagory=document.querySelectorAll(".catagory")
const catagory_select=document.querySelector(".catagory_select")
let catagory_list=[]
const form=document.querySelector(".form")
const blog=document.querySelectorAll(".blog")
const blogs=document.querySelector(".blogs")
const scroll_to_top=document.querySelector(".scroll_to_top")
const pages=document.querySelector(".page")

// loading content on page
window.addEventListener('DOMContentLoaded',function(){
    // when website loads we dont want scroll to top button, we want it after certain scroll
    scroll_to_top.classList.add("hide")
    

    // creating the pages functionality on blogs's home page ; mange blogs cause large scroll times which is inefficient
    max_blogs=4
    if(blog.length>max_blogs){
        remain=blog.length/max_blogs
        remain=Math.ceil(remain)

        content=""
        for(i=1;i<=remain;i++){
            content=content+`<p>${i}</p>`
        }
        pages.innerHTML=content

        let current_page=parseInt(window.location.pathname.slice(12,))
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
})

// appear a scrool to top button if scrolled below certain level
window.addEventListener("scroll",function(){
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