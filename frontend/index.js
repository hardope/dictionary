const DOM = document
function get(selector) {
  return DOM.getElementById(selector)
}

DOM.addEventListener('DOMContentLoaded', () => {
    let request = new XMLHttpRequest()
    request.open('GET', 'https://mydictionary.pythonanywhere.com', true)
    request.onload = function() {
        let data = JSON.parse(this.response)
        if (request.status >= 200 && request.status < 400) {
            let word = get('word')
            word.innerHTML = `<h2>${data.word.word}</h2>`
        } else {
            console.log('error')
        }
    }
    request.send()
});