//Changes the colour of each request status based on the text in the .status class field.
const request_status = document.querySelectorAll('.status'); 
request_status.forEach(request_status => {
  if (request_status.textContent.trim() === "Complete") {
    request_status.classList.add('green');
  } else if (request_status.textContent.trim() === "Incomplete") {
    request_status.classList.add('blue');
  }
});