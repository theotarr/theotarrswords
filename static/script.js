const latinToEnglishSearch = document.querySelector("#latin");
const latinToEnglishButton = document.querySelector("#latin-button");
const latinDefinition = document.querySelector("#latin-def");

const englishToLatinSearch = document.querySelector("#english");
const englishToLatinButton = document.querySelector("#english-button");
const englishDefinition = document.querySelector("#english-def");




function latin_to_english() {
    if (latinToEnglishSearch.value != "") {
        fetch(`${window.origin}/la_to_en`, {
            method: "POST",
            cache:"no-cache",
            credentials: "include",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(latinToEnglishSearch.value),
        })
        .then(response => response.json())
        .then(data => {
            latinToEnglishSearch.value = "";
            latinDefinition.innerHTML = formatDefinition(data["translation"]);
        })
    }
}

function english_to_latin() {
    if (englishToLatinSearch.value != "") {
        fetch(`${window.origin}/en_to_la`, {
            method: "POST",
            cache:"no-cache",
            credentials: "include",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(englishToLatinSearch.value),
        })
        .then(response => response.json())
        .then(data => {
            englishToLatinSearch.value = "";
            englishDefinition.innerHTML = formatDefinition(data["translation"]);
        })
    }
}

function formatDefinition(text) {
    text = text.split("\n");
    let definition = "";

    text.forEach(element => {
        if (element.endsWith(";")) {
            element = "<strong>" + element + "</strong><br><br><hr>";
        }
        definition += element + "<br>";
    });
    definition = definition.slice(0, -13);
    return definition.replace("<br>", "");
}



// event listeners
latinToEnglishSearch.addEventListener("keyup", ({key}) => {
    if (key == "Enter" && latinToEnglishSearch.value != "") {
        latin_to_english();
    }
});

latinToEnglishButton.addEventListener("click", () => {
    if (latinToEnglishSearch.value != "") {
        latin_to_english();
    }
})


englishToLatinSearch.addEventListener("keyup", ({key}) => {
    if (key == "Enter" && englishToLatinSearch.value != "") {
        english_to_latin();
    }
});

englishToLatinButton.addEventListener("click", () => {
    if (englishToLatinSearch.value != "") {
        english_to_latin();
    }
})