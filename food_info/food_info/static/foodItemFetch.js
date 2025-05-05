"use strict";

async function fetchFoodItems() {
    let response = await fetch('/api/items/');
    console.log(response);
    let result = await response.json();
    console.log(result);
    return result;
}