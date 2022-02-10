initialise_table()
getLeaderboardDataJSON().then(data => {
    show_leaderboard(data);
})

async function getLeaderboardDataJSON() {
    const response = await fetch('/leaderboard_data');
    const data = await response.json();
    return data;
  }

function initialise_table(){
    let leaderboard_div = document.getElementById('leaderboard')
    let show_today_button = document.createElement('button')
    show_today_button.setAttribute('id', 'show-today-button')
    show_today_button.appendChild(document.createTextNode('Today'))
    leaderboard_div.appendChild(show_today_button)

    let table = document.createElement('table')

    for(let i = 1; i <= 6; i++){
        let tr = document.createElement('tr')
        let id = i+"guess"
        tr.setAttribute('id', id)
        let td = document.createElement('td')
        td.appendChild(document.createTextNode(i))
        table.appendChild(tr)
        tr.appendChild(td)
    }
    leaderboard_div.appendChild(table)
}

function show_leaderboard(data){
    let users = data.data;

    for(let i = 0; i < users.length; i++){
        let user_initials = users[i][0]
        let user_guesses = users[i][1]
        let id = user_guesses + "guess"
        console.log(id)
        let tr = document.getElementById(id)
        let td = document.createElement('td')
        td.appendChild(document.createTextNode(user_initials))
        tr.appendChild(td)
    }  
}