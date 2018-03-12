var formAction = 0;

function form(event){
    event.preventDefault();
    var question = document.querySelector("#form input[type='text']").value;
    var reponse = document.querySelector("#answer");


    if (question.indexOf("no") > -1) {
        reponse.innerHTML = "Ok. Feel free to look around.";
    } else if (question.indexOf("yes") > -1) {
        reponse.innerHTML = "Welcome! Click around and see what you can find!";
    } 
    document.querySelector("#form input[type='text']").value = " ";
}

window.onload = function() {
    document.querySelector("#form").addEventListener("submit", form);
}