
// varible declaration
// buttons
const content= document.querySelector('.content')
const scroll_up=document.querySelector('.above')
const scroll_down=document.querySelector('.below')
const movement=document.querySelector('.movement')
const hit_blogs=document.querySelector('.hit_blogs')
const menu_btn=document.getElementById("menu-btn")
const menu=document.querySelector('.menu')

// universal variables
let position=0
let max_height=0
let height_list=[]

// when page loads
window.addEventListener('DOMContentLoaded',function(){
    // creating a list of all the sections in page
    // this list will be used for smooth scroll
    window.navigation=content.children

    scroll_up.innerHTML=`<div class="above"><a href="#top"><button> ^ </button></a></div>`

    scroll_down.innerHTML=`<div class="above"><a href="#${navigation[1].id}"><button> V </button></a></div>`

    offset_check()
})

// dynamic page offset allocation;
// the hit blog page's height is dynamic; so we have to allocate next page according to height of this page
window.addEventListener('resize',function (){
    offset_check()
})

// whenever we scroll; first offset check to get position of all pages
// then find current position; fand which page we are on
// set previous page value = current page -1 
// set next page value=current page +1
window.addEventListener('scroll',function(){
    offset_check()
    for(i=0;i<navigation.length;i++){
        if(Math.round(window.pageYOffset)<height_list[i]){
        up=i-1
        if(up==-1){
            up=0
        }
        down=i+1
        if(down==navigation.length){
            down=navigation.length-1
        }
        scroll_up.innerHTML=`<div class="above"><a href="#${navigation[up].id}"><button> ^ </button></a></div>`

            
        scroll_down.innerHTML=`<div class="above"><a href="#${navigation[down].id}"><button> V </button></a></div>`
        return 0
        }
    }
})

// to open side menu
menu_btn.addEventListener("click",function(){
    menu.classList.add('toggle')
})

// to close side menu
document.getElementById("close").addEventListener("click",function(){
    document.querySelector(".menu").classList.remove("toggle")
})

// the off set check function
// gives a list of height of each page 
function offset_check(){
    max_height=0
    for(i=0;i<navigation.length;i++){
        max_height=max_height+navigation[i].offsetHeight
        height_list[i]=max_height
    }
    
    for(i=0;i<navigation.length;i++){
        if(i!=0){
            navigation[i].style.top=height_list[i-1]
        }
    }
}