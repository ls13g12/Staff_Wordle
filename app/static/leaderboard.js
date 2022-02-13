var config = null

function load_today_chart(){
    getTodayLeaderboardDataJSON().then(chart_data => {
        update_chart(chart_data);
        var chart_title = document.getElementById('chart-title')
        chart_title.textContent = "Today's Results"
    })
}

function load_week_chart(){
    getWeekLeaderboardDataJSON().then(chart_data => {
        update_chart(chart_data);
    })
}

function load_month_chart(){
    getMonthLeaderboardDataJSON().then(chart_data => {
        update_chart(chart_data);
    })
}

function load_all_time_chart(){
    getAllLeaderboardDataJSON().then(chart_data => {
        update_chart(chart_data);
    })
}

async function getTodayLeaderboardDataJSON() {
    const response = await fetch('/today_leaderboard_data')
    const data = await response.json()
    var chart_data = set_chart_config(data) 
    return chart_data 
}

async function getWeekLeaderboardDataJSON() {
    const response = await fetch('/week_leaderboard_data')
    const data = await response.json()
    var chart_data = set_chart_config(data) 
    return chart_data
}

async function getMonthLeaderboardDataJSON() {
    const response = await fetch('/month_leaderboard_data')
    const data = await response.json()
    var chart_data = set_chart_config(data) 
    return chart_data
}

async function getAllLeaderboardDataJSON() {
    const response = await fetch('/all_leaderboard_data')
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
    set_chart_height(data.initials)
    const chart_data = {
        labels : data.initials,
        datasets: [{
            data: data.guesses,
            backgroundColor: [
                '#C0FFFF'
            ],
            dataPointMaxWidth: 20,
            maxBarThickness: 20, // number (pixels)
            barPercentage: 0.9
        }]
    }
    config = {
        type: 'bar',
        data: chart_data,
        height: 20 * data.guesses + 100,
        options: {
            responsive: true,
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
                        color: "#C0FFFF",
                        font: {
                            size: 16
                        }
                    }
                },
                x: {
                    title: {
                        color: "#C0FFFF",
                        display: true,
                        text: 'Number of Guesses',
                        font: {
                            size: 16
                        }
                    },

                    min: 0,
                    max: 6,
                    ticks: {
                        color: "#C0FFFF",
                        stepSize: 1,
                        font: {
                            size: 18
                        }
                    }
                }
            }
        }
    };
    return chart_data

}

function set_chart_height(initials){
    let number_y_values = initials.length
    let chart_height = number_y_values * 35 + 60
    let leaderboard_div = document.getElementById('leaderboard')
    leaderboard_div.style.height = chart_height+"px"
}
