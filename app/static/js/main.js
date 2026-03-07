import { loadPrice } from "./loadPrice.js"
import { loadGraph } from "./loadGraph.js"

async function main(){
    const coinId = document.getElementById("coinId").value.trim();

    loadPrice(coinId);
    loadGraph(coinId);
}

document.getElementById("loadButton").addEventListener("click", main);
main();