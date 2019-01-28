$(document).ready(function() {

  $('#results').hide()

  $('#text-form').submit(function(e) {
    displayLoadingButton()
    var form = $(this)
    $.ajax({
      type: form.attr('method'),
      url: form.attr('action'),
      data: form.serialize(),
      success: function(data) {
        hideInputForm()
        displayResults(data)
      }
    })
    e.preventDefault()
  })

  function displayLoadingButton() {
    showSpinner()
    showLoading()
  }

  function showSpinner() {
    $('#button-spinner').addClass("spinner-border spinner-border-sm")
  }

  function showLoading() {
    $('#button-text').text('loading...')
  }

  function displayResults(data) {
    var url = "http://localhost:8000/result"
    $.get(url, function(data) {
      $('#results').show()
      displayResultsContainer()
      displayUsersInputText(data.text)
      displayProgressBars(data.response_dict)
    })
  }

  function displayResultsContainer() {
    $('#results').html(renderResultsContainer())
  }

  function displayUsersInputText(text) {
    $("#results").prepend(renderUserInputText(text))
  }

  function hideInputForm() {
    $("#london-input-form").hide()
  }

  function displayProgressBars(data) {
    for(var tone in data) {
      var toneName = tone
      var toneScore = data[tone]
      $('#progress-results').append(`<h1>${toneName} - ${toneScore}%</h1><div id='progress-results' class='progress'><div id='${toneName}' class='progress-bar progress-bar-${toneName}' role='progressbar' style='width: ${toneScore}%' aria-valuenow='${toneScore}' aria-valuemin='0' aria-valuemax='100'></div>'</div>`)
    }
  }

  function renderUserInputText(text) {
    return `<h1 id="users-text">${text}</h1>`
  }

  function renderResultsContainer() {
    return '<div id="progress-results"></div>'
  }

})
