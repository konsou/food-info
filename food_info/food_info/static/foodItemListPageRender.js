async function renderPage(){
    const items = await fetchFoodItems();
    const table = document.getElementById("food-items");
    items.forEach((item) => { table.appendChild(renderFoodItemRow(item)); });
}

document.addEventListener("DOMContentLoaded", renderPage);