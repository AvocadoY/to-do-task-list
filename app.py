const arr=[]
const griddisplay= document.querySelector(".grid")
for(let i=1;i<10;i++){
    const x=document.createElement("div")
    x.setAttribute("class","squre")
    x.setAttribute("id",i)
    griddisplay.appendChild(x);
}

const squres= document.querySelectorAll(".squre")
const moles=document.querySelector(".mole")
const timeleft=document.querySelector("#time-left")
const score=document.querySelector("#score")
const best=document.querySelector("#best")

let result=0
let hitposition
let currenttime=60
let timerid=null
let bestscore=0


function randomsqure(){
    squres.forEach(squre => {
        squre.classList.remove("mole")
    })
    let randomposition=squres[Math.floor(Math.random()*9)]
    randomposition.classList.add("mole")
    hitposition = randomposition.id
}

squres.forEach(squre => {
    squre.addEventListener('mousedown', () => {
        if(squre.id==hitposition){
            result++
            score.textContent=result
            hitposition=null
        }
    })
})

function movemole(){
    timerid= setInterval(randomsqure,1000)
    //atach to button
}
movemole()

function countdown(){
    currenttime--
    timeleft.textContent=currenttime
    if( currenttime==0){
        clearInterval(countdowntimerid)
        clearInterval(timerid)//display best score, when timer done-refresh the pash
        alert("game over! your final score is"+result)
        
        bestscore,Math.max(bestscore ,result)
        best.textContent=bestscore

        //איך זה יכול להישאר אחרי ריענון?

    }
}
let countdowntimerid=setInterval(countdown,500)
