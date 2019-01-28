$(document).ready(function() {

  $('#results').hide()

  $('#text-form').submit(function(e) {
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

  function displayResults(data) {
    var url = "http://localhost:8000/result"
    $.get(url, function(data) {
      displayUsersInputText(data.text)
      displayProgressBars(data.response_dict)
    })
  }

  function displayUsersInputText(text) {
    $("#users-text").html(text)
  }

  function hideInputForm() {
    $("#london-input-form").hide()
  }

  function displayProgressBars(data) {
    $("#joy").attr('style', 'width: ' + data['Joy'] + '%' ).attr('aria-valuenow', data['Joy'])
    $("#anger")
    $("#sadness")
    $("#analytical")
    $("#fear")
    $("#disgust")
    $("#confident")
    $("#tentative")
  }
})
