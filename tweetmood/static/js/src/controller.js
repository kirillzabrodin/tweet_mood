(function(exports) {

  function Controller(resultsView = new ResultsView, homepageView = new HomepageView) {
    this.resultsView = resultsView
    this.homepageView = homepageView
  }

  Controller.prototype = {
    displayHomepage: function() {
      $('#app').html(this.homepageView.render())
      this._listenForFormSubmit()
    },

    _listenForFormSubmit: function() {
      var form = $('#london-form')
      form.submit((e) => {
        e.preventDefault()
        this._displayLoadingButton()
        this._postFormData(form)
      })
    },

    _postFormData: function(form) {
      $.ajax({
        type: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: (data) => {
          $(form).hide()
          this._displayResults(data)
        }
      })
    },

    _displayResults: function(data) {
      var text = data.response
      var res_dict = data.response_dict || {}
      var holmes_res = data.holmes_result || {}
      $('#app').html(this.resultsView.render(text, res_dict, holmes_res))
    },

    _displayLoadingButton: function() {
      $('#button-spinner').addClass(this.homepageView.form.button.renderSpinnerClass())
      $('#button-text').text(this.homepageView.form.button.renderLoadingText())
    }

  }

  exports.Controller = Controller
})(this)
