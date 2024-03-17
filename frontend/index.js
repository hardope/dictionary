const DOM = document
function get(selector) {
  return DOM.getElementById(selector)
}

DOM.addEventListener('DOMContentLoaded', () => {
    
    if (window.location.search) {
        let word = window.location.search.split('=')[1]
        let request = new XMLHttpRequest()
        request.open('GET', `https://mydictionary.pythonanywhere.com/get/${word}`, true)
        request.onload = function() {
            if (request.status == 200) {
                let data = JSON.parse(request.response)
                data = data
                let word = get('word')
                word.innerHTML = `<h3>${data[0]['word']}</h3>`
                for (i = 0; i < data.length; i++) {
                    word.innerHTML += `
                    <p>Definition - ${data[i]['definition']}</p>
                    <span>Word Class - ${data[i]['word_class']}</span><br>
                    `
                }

                word.innerHTML += `<span>Length - ${data[0]['length']}</span>`                
            } else {
                console.log('error')
                let word = get('word')
                word.innerHTML = `<h3>Word not found</h3>`
            }
        }
        request.send()
    } else {
    
        let request = new XMLHttpRequest()
        request.open('GET', 'https://mydictionary.pythonanywhere.com', true)
        request.onload = function() {
            let data = JSON.parse(request.response)
            data = data['word'][0]
            if (request.status >= 200 && request.status < 400) {
                let word = get('word')
                word.innerHTML = `
                <h3>${data['word']}</h3>
                <p>Definition - ${data['definition']}</p>
                <span>Word Class - ${data['word_class']}</span><br>
                <span>Length - ${data['length']}</span>
                `
            } else {
                console.log('error')
            }
        }
        request.send()
    }
});