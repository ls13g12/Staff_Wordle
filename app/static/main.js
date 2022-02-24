const tileDisplay = document.querySelector('.tile-container')
const keyboard = document.querySelector('.key-container')
const messageDisplay = document.querySelector('.message-container')
const messageText = document.querySelector('.message-text')

let wordle

const getWordle = () => {
    fetch('/get_word')
        .then(response => response.json())
        .then(json => {
            if (json['data'] == null){
                showMessage("You have completed today's word! \n Come back tomorrow")
                isGameOver = true
            }
            else{
                showMessage("The timer has been removed.")
                wordle = json['data'].toUpperCase()
            }
        })
        .catch(err => console.log(err))
}
getWordle()


const keys = [
    'Q',
    'W',
    'E',
    'R',
    'T',
    'Y',
    'U',
    'I',
    'O',
    'P',
    'A',
    'S',
    'D',
    'F',
    'G',
    'H',
    'J',
    'K',
    'L',
    'ENTER',
    'Z',
    'X',
    'C',
    'V',
    'B',
    'N',
    'M',
    '«',
]
const guessRows = [
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', '']
]
let currentRow = 0
let currentTile = 0
let isGameOver = false

guessRows.forEach((guessRow, guessRowIndex) => {
    const rowElement = document.createElement('div')
    rowElement.setAttribute('id', 'guessRow-' + guessRowIndex)
    guessRow.forEach((_guess, guessIndex) => {
        const tileElement = document.createElement('div')
        tileElement.setAttribute('id', 'guessRow-' + guessRowIndex + '-tile-' + guessIndex)
        tileElement.classList.add('tile')
        rowElement.append(tileElement)
    })
    tileDisplay.append(rowElement)
})

keys.forEach(key => {
    const buttonElement = document.createElement('button')
    buttonElement.textContent = key
    buttonElement.setAttribute('id', key)
    buttonElement.addEventListener('click', () => handleClick(key))
    keyboard.append(buttonElement)
})

const handleClick = (letter) => {
    if (!isGameOver) {
        if (letter === '«') {
            deleteLetter()
            return
        }
        if (letter === 'ENTER') {
            checkRow()
            return
        }
        addLetter(letter)
    }
}

const addLetter = (letter) => {
    if (currentTile < 5 && currentRow < 6) {
        const tile = document.getElementById('guessRow-' + currentRow + '-tile-' + currentTile)
        tile.textContent = letter
        guessRows[currentRow][currentTile] = letter
        tile.setAttribute('data', letter)
        currentTile++
    }
}

const deleteLetter = () => {
    if (currentTile > 0) {
        currentTile--
        const tile = document.getElementById('guessRow-' + currentRow + '-tile-' + currentTile)
        tile.textContent = ''
        guessRows[currentRow][currentTile] = ''
        tile.setAttribute('data', '')
    }
}
/*
const checkWord = () => {
    word = ""
    const rowTiles = document.querySelector('#guessRow-' + currentRow).childNodes
    rowTiles.forEach(tile => {
        word += tile.getAttribute('data')
    })
    return isWord(word)
}
*/

const checkRow = () => {
    const guess = guessRows[currentRow].join('')
    if (currentTile > 4) {  
        flipTile()
        if (wordle == guess) {
            update_database(wordle)
            isGameOver = true
            showMessage('Well done! Go to the leaderboard page\n to see how you rank')
            return
        } else {
            if (currentRow >= 5) {
                currentRow++
                update_database(wordle)
                isGameOver = true
                showMessage(`Game Over! The word is ${wordle}. Try again tomorrow!`)
                return
            }
            if (currentRow < 5) {
                currentRow++
                currentTile = 0
            }
        }
    }  
}

const showMessage = (message) => {
    messageText.textContent = message
}

const addColorToKey = (keyLetter, color) => {
    const key = document.getElementById(keyLetter)
    key.classList.add(color)
}

const flipTile = () => {
    const rowTiles = document.querySelector('#guessRow-' + currentRow).childNodes
    //answer wordle
    let checkWordle = wordle
    //user guessed word
    let checkGuessedWord = ""
    const guess = []
    
    //setup object to count letters remaining in the guess to be checked
    //this allows for single green and single yellow tiles
    var guessLetterCount = {}

    rowTiles.forEach(tile => {
        guess.push({letter: tile.getAttribute('data'), color: 'grey-overlay'})
        //user guessed word added
        checkGuessedWord += tile.getAttribute('data')
    })

    guess.forEach(guess => guessLetterCount[guess.letter] = (guessLetterCount[guess.letter] || 0) + 1)

    guess.forEach((guess, index) => {
        if (guess.letter == wordle[index]) {
            guess.color = 'green-overlay'
            checkWordle = checkWordle.substring(0, index) + '-' + checkWordle.substring(index + 1)
            checkGuessedWord = checkGuessedWord.substring(0, index) + '-' + checkGuessedWord.substring(index + 1)
            guessLetterCount[guess.letter]--
        }
    })

    guess.forEach((guess, index) => {
        if(checkGuessedWord[index] != '-'){
            if (checkWordle.includes(guess.letter)){
                if(guessLetterCount[guess.letter] > 0 ){
                    guess.color = 'yellow-overlay'
                    checkWordle = checkWordle.replace(guess.letter, '-')
                    guessLetterCount[guess.letter]--
                }
            }
        }
    })

    rowTiles.forEach((tile, index) => {
        setTimeout(() => {
            tile.classList.add('flip')
            tile.classList.add(guess[index].color)
            addColorToKey(guess[index].letter, guess[index].color)
        }, 500 * index)
    })
}

async function update_database(wordle) {
    let wordle_data = {
        'wordle': wordle,
        'guesses': currentRow + 1
    }
    let response = await fetch('/update_database', {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(wordle_data),
        cache: "no-cache",
        headers: new Headers({
          "content-type": "application/json"
      })
    })
    let response_data = await response.json()
    return response_data.status_code
}

/*

function isWord(word){
    word = word.toLowerCase()
    if (wordList.includes(word)){
        return true
    }
    return false
}
*/