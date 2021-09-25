const partOfSpeech = document.querySelector("#part-of-speech");
const formsInput = document.querySelector("#forms-input");
const formSearchButton = document.querySelector("#forms-button");

const formsTable = document.querySelector("#forms-table");

function getForms() {
    if (formsInput.value != "") {
        fetch(`${window.origin}/forms`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(parseFormsRequest()),
        })
        .then(response => response.json())
        .then(data => {
            formsInput.value = "";
            formsTable.innerHTML = data["forms"];
        })
    }
}

function parseFormsRequest() {
    return partOfSpeech.options[partOfSpeech.selectedIndex].value + ":" + formsInput.value;
}


// event listeners
formsInput.addEventListener("keyup", ({key}) => {
    if (key == "Enter") {
        getForms();
    }
});

formSearchButton.addEventListener("click", () => {
    getForms();
})