const captureContainer = document.getElementById('capture')
const startStopBtn = document.querySelector('#startStopBtn')
const resetBtn = document.querySelector('#resetBtn')
const captureBtn = document.querySelector('#captureBtn')
const timerScreen = document.querySelector('#timer')
const milSec = document.querySelector('sup')

//Stopwatch time initializations

let milsec = 0
let sec = 0
let min = 0
let hrs = 0



//variables for run pause conditions
let timerStatus = false ;
let timerInterval  ;

//stopWatch Html run operation function
function stopWatch(){
    milsec++
    if(milsec === 100){
        milsec = 0
        sec++
        if(sec ===60){
            sec =0
            min++
            if(min===60){
                min = 0
                hrs++
            }
        }
}

timerScreen.innerHTML = `${hrs}:${min}:${sec}    <sup>:  ${milsec} </sup>`
}   


//Stopwatch pause run conditions

startStopBtn.addEventListener('click', function(){
    if(!timerStatus){
        timerInterval = window.setInterval(stopWatch,10)
        
        document.getElementById('startStopBtn').innerHTML = `Pause`;
        startStopBtn.style.backgroundColor = "gold";
        startStopBtn.style.borderColor = "gold" ;
        timerStatus = true
    }
    else{
        window.clearInterval(timerInterval);
        document.getElementById('startStopBtn').innerHTML = `Run`;
        startStopBtn.style.backgroundColor = "green";
        startStopBtn.style.borderColor = "green" ;
        timerStatus = false;
    }
})

// capture laps
let laps = 1
captureBtn.addEventListener('click',()=>{
    let captureData = timerScreen.innerText
    captureContainer.innerHTML += `<p>Lap${laps} -  ${captureData}</p>`;
    laps++
})


resetBtn.addEventListener('click',()=>{
    window.clearInterval(timerInterval);
        document.getElementById('startStopBtn').innerHTML = `Run`;
        startStopBtn.style.backgroundColor = "green";
        startStopBtn.style.borderColor = "green" ;
        timerStatus = false;
    milsec = 0
    sec = 0
    min = 0
    hrs = 0
    timerScreen.innerHTML = `${hrs}:${min}:${sec}    <sup>:  ${milsec} </sup>`
    captureContainer.innerHTML = `<p id="capture-head">Laps</p>`;
})