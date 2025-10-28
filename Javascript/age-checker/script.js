// get elements from DOM/ HTML

let button = document.getElementById("checkBtn");
let result = document.getElementById("result");


//function to check age
function checkAge (){
    let ageInput = document.getElementById("ageInput").value;
    let age = Number(ageInput);

    if (ageInput.trim() === ""){
        result.textContent = "Please enter your age.";
        result.style.color = "red";
    }

    else if(isNaN(age)) {
        result.textContent = "Age must be a number.";
        result.style.color = "red";
    }

    else if(age < 13) {
        result.textContent = "You are a child.";
        result.style.color = "orange";
    }
    else if (age >=13 && age <20) {
        result.textContent = "You are a teenager.";
        result.style.color = "blue";
    }
                               
    else if (age >= 20 && age <60) {
        result.textContent = "You are an adult.";
        result.style.color = "green";
    }

    else if (age >= 60 && age < 120) {
        result.textContent = "You are a senior citizen.";
        result.style.color = "gray";
    }

    else {
        result.textContent = "What are you? Methuselah! Enter a reasonable age!!";
        result.style.color = "red";
    }

}

button.addEventListener("click", checkAge);

ageInputField.addEventListener("keydown", function(event){
    if (event.key === "Enter") {
        checkAge();
    }
})