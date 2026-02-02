document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  const helloElement = document.querySelector('#hello');

  fetch(url)
    .then(response => response.json())
    .then(data => {
      helloElement.textContent = data.hello;
    });
});
