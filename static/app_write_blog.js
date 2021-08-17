const today_id=document.getElementById('today')
const fields = document.querySelectorAll('.fields')
const catagory =document.querySelector('.catagory')
let catagories =['coding','general','hello']

window.addEventListener('DOMContentLoaded',function(){
    for(i=0;i<catagories.length;i++){
        if(i==0){
            line=`
            <option value="${catagories[i]}">${catagories[i]}</option>`
        }
        else{
            line=line+`<option value="${catagories[i]}">${catagories[i]}</option>`
        }
    }
    catagory.innerHTML=line
})