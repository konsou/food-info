"use strict";

function renderFoodItemRow(item) {
    const newRow = document.createElement("tr");
    const nameCell = newRow.insertCell(0);
    const eanCell = newRow.insertCell(-1);
    const priceCell = newRow.insertCell(-1);
    const carbsCell = newRow.insertCell(-1);
    const proteinCell = newRow.insertCell(-1);
    const fatCell = newRow.insertCell(-1);
    const kcalCell = newRow.insertCell(-1);
    const proteinValueCell = newRow.insertCell(-1);
    const kcalValueCell = newRow.insertCell(-1);
    nameCell.innerHTML = `${item.name} ${item.weight} g`;
    eanCell.innerHTML = item.ean;
    priceCell.innerHTML = `${item.price.toFixed(2).toString().replace(".", ",")} €`;
    priceCell.classList.add('text-right');
    carbsCell.innerHTML = item.carbs_per_100g.toFixed(2);
    carbsCell.classList.add('text-right');
    proteinCell.innerHTML = item.protein_per_100g.toFixed(2);
    proteinCell.classList.add('text-right');
    fatCell.innerHTML = item.fat_per_100g.toFixed(2);
    fatCell.classList.add('text-right');
    kcalCell.innerHTML = item.kcal_per_100g.toFixed(2);
    kcalCell.classList.add('text-right');
    proteinValueCell.innerHTML = item.price_per_100g_protein.toFixed(2);
    proteinValueCell.classList.add('text-right');
    kcalValueCell.innerHTML = item.price_per_1000_kcal.toFixed(2);
    kcalValueCell.classList.add('text-right');

    return newRow;
}