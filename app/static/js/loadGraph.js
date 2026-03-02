const labels = Utils.hours({count: 24});

const data = {
  labels: labels,
  datasets: [{
    label: 'Price',
    data: [65, 59, 80, 81, 56, 55, 40], //Later I'll make it take historical data
    fill: true,
    borderColor: 'rgb(75, 192, 192)',
    fillColor: 'rgb(75, 192, 192)',
    tension: 0.1
  }]
};

const config = {
  type: 'line',
  data: data,
};