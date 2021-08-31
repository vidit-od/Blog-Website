// declaration
const catagory=document.querySelectorAll(".catagory")
const catagory_select=document.querySelector(".catagory_select")
let catagory_list=[]
const form=document.querySelector(".form")
const submit=document.querySelector(".submit")
const blog=document.querySelectorAll(".blog")
const blogs=document.querySelector(".blogs")
const scroll_to_top=document.querySelector(".scroll_to_top")
const pages=document.querySelector(".page")


// loading content on page
window.addEventListener('DOMContentLoaded',function(){
    // from the list of blogs, find all the unique catagories of blog and save it in catagory_list
    for (i=0;i<catagory.length;i++){
        if (i==0){
            catagory_list.push(catagory[i].innerHTML)
        }
        else if(!(catagory_list.includes(catagory[i].innerHTML))){
            catagory_list.push(catagory[i].innerHTML)
        }
    }
    // adding the empty option. for no filter
    let line=`<option value=""></option>`
    // creating options according to the list formed above
    for(i=0;i<catagory_list.length;i++){
        line=line+`<option value="${catagory_list[i]}">${catagory_list[i]}</option>`
    }
    // deploy all the possible catagories
    catagory_select.innerHTML=line

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
        console.log(current_page)
        // lower limit :((current_page-1)*max_blogs)+1
        // upper limit :current_page*max_blogs

        page_content=''
        for(i=0;i<blog.length;i++){
            if((i>=((current_page-1)*max_blogs))&&(i<current_page*max_blogs+1)){
                page_content=page_content+'<div class="blog">'+blog[i].innerHTML+'</div>'
            }
        }
        blogs.innerHTML=page_content
    }
})

// // for submit button of filter menu
// submit.addEventListener("click",function(){
//     // taking all the data according to which we will filter
//     const input_catagory= document.getElementById("catagory_select").value
//     const input_author=document.getElementById("author").value
//     let content=""
//     let loop = 0
//     // const blogs contains a list of all blogs in latest to oldest order
//     // if person wants latest to top order then we will traverse list from 0 to end
//     // total 4 catagories possible, filter nothing, filter acc to catagory , filter acc to author , filter acc to both
//     // using if and else if to find correct catagory and adding its inner html in content
//     // in end if content empty means no blog found according to the filter asked....so display no content
//     // else if content is not empty ... use its code as new inner html
//         for(i=0;i<blog.length;i++){
//             if(input_catagory=="" && input_author==""){
//                 loop=1
//                 content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
//             }
//             else if(input_catagory=="" && input_author !=""){
//                 loop=2
//                 if(blog[i].children[0].children[1].children[0].innerHTML==input_author){
//                     content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
//                 }
//             }
//             else if(input_catagory!="" && input_author==""){
//                 loop=3
//                 if(blog[i].children[0].children[1].children[2].innerHTML==input_catagory){
//                     content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
//                 }
//             }
//             else{
//                 loop=4
//                if((blog[i].children[0].children[1].children[2].innerHTML==input_catagory) && (blog[i].children[0].children[1].children[0].innerHTML==input_author)){
//                 content=content+'<div class="blog">'+blog[i].innerHTML+'</div>'
//                }
//             }
            
//         }
//         if (content==""){
//             content=`<h3> No Results Found For this Filter </h3>`
//         }
//         if (loop==1){
//             document.querySelector(".section-title").innerHTML=' Recently Published'
//         }
//         else{
//             document.querySelector(".section-title").innerHTML=' Filtered Results'
//         }
//         blogs.innerHTML=content
// })

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
document.getElementById("menu").addEventListener("click",function(){
    document.querySelector(".menu").classList.add("toggle")
})