let priceChart = null;

export async function loadGraph(coinId) {

  try {
      const res = await fetch(`/api/${encodeURIComponent(coinId)}/price_graph`);
      const json_data = await res.json();

      const labels = json_data.day;
      const prices = json_data.price;

      if (priceChart) {
          priceChart.data.labels = labels;
          priceChart.data.datasets[0].data = prices;
          priceChart.update();
          return;
      }

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
          responsive: false
        }
      };

      priceChart = new Chart(document.getElementById("priceGraph"), config)

  } catch (err){
        console.error(err)
  }
}
