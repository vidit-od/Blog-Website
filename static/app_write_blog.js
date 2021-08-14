const today_id=document.getElementById('today')
const fields = document.querySelectorAll('.fields')
const catagory =document.querySelector('.catagory')
let catagories =["",'coding','general']

window.addEventListener('DOMContentLoaded',function(){
    const today= new Date().toDateString().substr(3,15)
    fields[2].innerHTML=`<label> Date</label><input type='text' name="date" id="today" value ="${today}" disabled>`
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