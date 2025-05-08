document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("id_image").onchange = foodItemFromForm;
});

async function foodItemFromForm(e) {
    e.preventDefault();
    let fileElem = document.getElementById("id_image");

    if (!fileElem.files.length) {
        return;
    }

    let reader = new FileReader();
    reader.readAsDataURL(fileElem.files[0]);
    reader.onloadend = async function (e) {
        const fileBase64 = e.target.result.split("base64,")[1];
        const requestBody = JSON.stringify({file: fileBase64});
        let response = await fetch('/api/from-image/', {
            method: 'POST',
            body: requestBody,
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            credentials: 'omit',
        });
        let result = await response.json();
        console.log(result);
        if (result.error){
            let errorContainer = document.getElementById("error-container");
            errorContainer.innerHTML = result.error;
            errorContainer.style.display = "block";
            return;
        }
        const newRow = renderFoodItemRow(result);
        document.getElementById("food-items").appendChild(newRow);
    };


}