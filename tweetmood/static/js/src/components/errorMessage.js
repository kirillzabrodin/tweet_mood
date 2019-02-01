var ErrorMessage = (function() {

  function render(user_text) {
    return `<h2 id="users-text">${user_text}</h2>`
  }

  return {
    render: render
  }

})()
