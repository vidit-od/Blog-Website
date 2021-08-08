
// varible declaration
const content= document.querySelector('.content')
const scroll_up=document.querySelector('.above')
const scroll_down=document.querySelector('.below')
const movement=document.querySelector('.movement')
let position=0

window.addEventListener('DOMContentLoaded',function(){
    // creating a list of all the sections in page
    // this list will be used for smooth scroll
    window.navigation=content.children
    console.log(navigation)
    movement.children[0].classList.add('remove')
    scroll_down.innerHTML=`<a href="#${navigation[1].id}"><button> V </button></a>`
    
})
window.addEventListener('scroll',function(){
    window.pageYOffset
    if(window.pageYOffset>=600){
        movement.children[0].classList.remove('remove')
    }
    else{
        movement.children[0].classList.add('remove')
    }
})
scroll_up.addEventListener('click',function(){
    position=position-1
    if(position<0){
        position=0
    }
    console.log(navigation[position].id)
    position_check()
    
    scroll_down.innerHTML=`<a href="#${navigation[position].id}"><button> v </button></a>`

    scroll_down.innerHTML=`<a href="#${navigation[position+1].id}"><button> v </button></a>`
})

scroll_down.addEventListener('click',function(){
    position=position+1
    if(position>navigation.length-1){
        position=navigation.length-1
    }
    console.log(navigation[position].id)
    position_check()
    

    scroll_up.innerHTML=`<a href="#${navigation[position-1].id}"><button> ^ </button></a>`
    scroll_down.innerHTML=`<a href="#${navigation[position].id}"><button> v </button></a>`
})
function position_check(){
    if (position==0){
        movement.children[0].classList.add('remove')
        movement.children[1].classList.remove('remove')
    }
    else if(position==navigation.length-1){
        movement.children[0].classList.remove('remove')
        movement.children[1].classList.add('remove')
        
    }
    else{
        movement.children[0].classList.remove('remove')
        movement.children[1].classList.remove('remove')
    }

}