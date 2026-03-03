import Utils from'./utils.js'

(async function() {
  const labels = Utils.days; //Later I'll make it take real-time date

  const data = {
    labels: labels,
    datasets: [{
      label: 'Price',
      data: [65, 59, 80, 81, 56, 55, 40], //Later I'll make it take historical data
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
}
)();
