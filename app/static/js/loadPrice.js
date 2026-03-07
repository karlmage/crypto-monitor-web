export async function loadPrice(coinId) {

    try {
        const res = await fetch(`/api/${encodeURIComponent(coinId)}/price`);
        const data = await res.json();
        document.getElementById("out").textContent = await data.price;
    } catch (err){
        document.getElementById("out").textContent = "Error loading price";
        console.error(err)
    }

}