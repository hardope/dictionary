document.addEventListener('DOMContentLoaded', function(){
     let num = 0;
     words = Request('127.0.0.1:5000/0');
     document.querySelector('h2').innerHTML = words
})