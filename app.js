const drawBtn = document.getElementById("drawBtn");
const resultDiv = document.getElementById("result");
const spreadSelect = document.getElementById("spread");

drawBtn.addEventListener("click", () => {
    const spread = spreadSelect.value;
    resultDiv.innerHTML = "";

    let cardsToDraw = 1;
    if(spread === "three") cardsToDraw = 3;
    if(spread === "celtic") cardsToDraw = 10;

    for(let i=0; i<cardsToDraw; i++){
        const n = Math.floor(Math.random() * 78);
        const imgUrl = `cards/${n}.jpg`;
        const cardDiv = document.createElement("div");
        cardDiv.innerHTML = `<p>Карта №${n}</p><img src="${imgUrl}" alt="Tarot card">`;
        resultDiv.appendChild(cardDiv);
    }
});

// Гороскоп
const showBtn = document.getElementById("showHoroscope");
const horoscopeResult = document.getElementById("horoscopeResult");

showBtn.addEventListener("click", async () => {
    const sign = document.getElementById("sign").value;
    const response = await fetch('horoscopes.json');
    const data = await response.json();
    horoscopeResult.innerHTML = `<p>${data[sign]}</p>`;
});
