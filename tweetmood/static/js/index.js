$(document).ready(function() {

  $('#text-form').submit(function(e) {
    var form = $(this)
    $.ajax({
      type: form.attr('method'),
      url: form.attr('action'),
      data: form.serialize(),
      success: function(data) {
        console.log("form submitted")
      }
    })
    e.preventDefault()
  })

})
