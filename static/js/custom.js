function loadData(weatherData) {
    let row = document.querySelector('#card-row')
    let card = document.querySelector('#card');
    let cardName = document.querySelector('#city-name');
    cardName.textContent = weatherData["city"];
    row.appendChild(card);

}