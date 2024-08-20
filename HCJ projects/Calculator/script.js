const display = document.getElementById("display")

function inputAppend(num) {
    display.value += num
}

function clearInput(){
    display.value = "";
}

function calculate() {
    try{
        display.value = eval(display.value)
    }
    catch(error){
        display.value = "Error"
    }
}