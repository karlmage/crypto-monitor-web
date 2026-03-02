async function loadPrice() {
    const coinId = document.getElementById("coinId").value.trim();

    try {
        const res = await fetch(`/api/${encodeURIComponent(coinId)}/price`);
        const data = await res.json();
        document.getElementById("out").textContent = await data.price;
    } catch (err){
        document.getElementById("out").textContent = "Error loading price";
        console.error(err)
    }

}

document.getElementById("loadButton").addEventListener("click", loadPrice);
loadPrice();