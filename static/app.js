
// varible declaration
const content= document.querySelector('.content')
const scroll_up=document.querySelector('.above')
const scroll_down=document.querySelector('.below')
const movement=document.querySelector('.movement')
const hit_blogs=document.querySelector('.hit_blogs')
let position=0
let max_height=0
let height_list=[]
window.addEventListener('DOMContentLoaded',function(){
    // creating a list of all the sections in page
    // this list will be used for smooth scroll
    window.navigation=content.children

    scroll_up.innerHTML=`<div class="above"><a href="#top"><button> ^ </button></a></div>`

    scroll_down.innerHTML=`<div class="above"><a href="#${navigation[1].id}"><button> V </button></a></div>`

    offset_check()
})

// dynamic page offset allocation
window.addEventListener('resize',function (){
    offset_check()
})
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

        // if(i==0){
        //     scroll_up.classList.add('.remove')
        // }
        // else if(i==navigation.length-1){
        //     scroll_down.classList.add('.remove')
        // }
        // else{
        //     scroll_up.classList.remove('.remove')
        //     scroll_down.classList.remove('.remove')    
        // }
        scroll_up.innerHTML=`<div class="above"><a href="#${navigation[up].id}"><button> ^ </button></a></div>`

            
        scroll_down.innerHTML=`<div class="above"><a href="#${navigation[down].id}"><button> V </button></a></div>`
        return 0
        }
    }
})
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