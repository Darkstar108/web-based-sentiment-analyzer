function drawGraph(polarity, subjectivity, label) {  
    let ctx = document.getElementById('myChart').getContext('2d');
    let scatterChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: label,
                pointRadius: 10,
                backgroundColor: 'rgba(255, 0, 0, 0.5)',
                borderColor: 'rgba(255, 0, 0, 1)',
                data: [{
                    x: polarity,
                    y: subjectivity
                }]
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    type: 'linear',
                    position: 'bottom',
                    scaleLabel: {
                        display: true,
                        labelString: 'Polarity',
                        fontSize: 16,
                        fontFamily: "Segoe UI"
                    },
                    ticks: {
                        min: -1.0,
                        max: 1.0
                    }
                }],
                yAxes: [{
                    type: 'linear',
                    scaleLabel: {
                        display: true,
                        labelString: 'Subjectivity',
                        fontSize: 16,
                        fontFamily: "Segoe UI"
                    },
                    ticks: {
                        min: -0.5,
                        max: 0.5
                    }
                }],
                responsive: true,
                maintainAspectRatio: false
            }
        }
    });
}