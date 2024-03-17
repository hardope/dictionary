const DOM = document
function get(selector) {
  return DOM.getElementById(selector)
}

DOM.addEventListener('DOMContentLoaded', () => {
    let word = get('word')
    word.innerHTML = `
    <h1> ----------********----------</h1>
    `        
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
});