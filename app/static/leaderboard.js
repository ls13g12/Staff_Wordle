getTodayLeaderboardDataJSON().then(chart_data => {
    initialise_chart(chart_data);
})

function load_today_chart(){
    getTodayLeaderboardDataJSON().then(chart_data => {
        update_chart(chart_data);
    })
}

function load_week_chart(){
    getWeekLeaderboardDataJSON().then(chart_data => {
        console.log(chart_data)
        update_chart(chart_data);
    })
}

function load_month_chart(){
    getMonthLeaderboardDataJSON().then(chart_data => {
        console.log(chart_data)
        update_chart(chart_data);
    })
}

var config = null
var myChart = document.getElementById('myChart')

async function getTodayLeaderboardDataJSON() {
    const response = await fetch('/today_leaderboard_data')
    const data = await response.json()
    set_chart_config(data)  
  }

  async function getWeekLeaderboardDataJSON() {
    const response = await fetch('/week_leaderboard_data')
    const data = await response.json()
    var chart_data = set_chart_config(data) 
    return chart_data
  }

  async function getMonthLeaderboardDataJSON() {
    const response = await fetch('/week_leaderboard_data')
    const data = await response.json()
    var chart_data = set_chart_config(data) 
    return chart_data
  }



function initialise_chart(){
    myChart = new Chart(
        document.getElementById('myChart'),
        config
    );
}

function update_chart(){
    myChart = Chart.getChart('myChart');
    if (myChart) {
        myChart.destroy()
    }
    myChart = new Chart(
        document.getElementById('myChart'),
        config
    );
}

function set_chart_config(data){
    const chart_data = {
        labels : data.initials,
        datasets: [{
            data: data.guesses,
            backgroundColor: [
                'rgba(255, 255, 255, 1)'
            ],
            barThickness: 20,  // number (pixels) or 'flex'
            maxBarThickness: 40, // number (pixels)
            barPercentage: 0.8
        }]
    }
    config = {
        type: 'bar',
        data: chart_data,
        responsive: true,
        options: {
            maintainAspectRatio: false,
            indexAxis: 'y',
            plugins:{
                legend:{
                    display: false
                }
            },
            scales: {
                y: {
                    ticks: {
                        font: {
                            size: 14
                        }
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Number of Guesses'
                    },

                    min: 0,
                    max: 6,
                    ticks: {
                        stepSize: 1,
                        font: {
                            size: 14
                        }
                    }
                }
            }
        }
    };
    return chart_data

}
