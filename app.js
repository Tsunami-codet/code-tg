document.getElementById("draw1").addEventListener("click", function () {
    const n = Math.floor(Math.random() * 78); // 78 карт
    const imgUrl = `https://YOUR_IMAGE_HOST/${n}.jpg`;
    document.getElementById("result").innerHTML =
        `<p>Выпала карта №${n}</p><img src="${imgUrl}" alt="Tarot card">`;
});
