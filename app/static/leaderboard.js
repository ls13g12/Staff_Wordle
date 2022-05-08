var config = null

function update_chart_title(title){
    var chart_title = document.getElementById('chart-title')
    chart_title.textContent = title
}

function load_today_chart(){
    getLeaderboardDataJSON('today').then(chart_data => {
        update_chart(chart_data);
        update_chart_title("Today's Results")
    })
}

function load_week_chart(){
    getLeaderboardDataJSON('week').then(chart_data => {
        update_chart(chart_data);
        update_chart_title("Average Result This Week")
    })
}

function load_month_chart(){
    getLeaderboardDataJSON('month').then(chart_data => {
        update_chart(chart_data);
        update_chart_title("Average Result This Month")
    })
}

function load_all_time_chart(){
    getLeaderboardDataJSON().then(chart_data => {
        update_chart(chart_data);
        update_chart_title("All Time Average Result")
    })
}

async function getLeaderboardDataJSON(filter=null) {
    const response = await fetch(`/api/leaderboard?filter=${filter}`)
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
                    max: 7,
                    ticks: {
                        color: "#C0FFFF",
                        stepSize: 1,
                        font: {
                            size: 16
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
    let chart_height = number_y_values * 30 + 120
    let leaderboard_div = document.getElementById('leaderboard')
    leaderboard_div.style.height = chart_height+"px"
}
