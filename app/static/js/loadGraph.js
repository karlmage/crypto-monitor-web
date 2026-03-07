export async function loadGraph(coinId) {

  try {
      const res = await fetch(`/api/${encodeURIComponent(coinId)}/price_graph`);
      const json_data = await res.json();

      const data = {
        labels: json_data.day,
        datasets: [{
          label: 'Price',
          data: json_data.price,
          fill: true,
          tension: 0.1
        }]
      };

      const config = {
        type: 'line',
        data: data,
        options:{
          responsive: true
        }
      };

      new Chart(document.getElementById("priceGraph"), config)

  } catch (err){
        console.error(err)
  }
}
