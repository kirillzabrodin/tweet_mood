(function(exports) {

  function Controller(resultsView = new ResultsView, homepageView = new HomepageView) {
    this.resultsView = resultsView
    this.homepageView = homepageView
  }

  Controller.prototype = {
    displayHomepage: function() {
      var self = this
      this._hideresults()
      $('#london-input-form').html(this.homepageView.render())
      this._listenForLondonFormSubmit()
    },

    _listenForLondonFormSubmit: function() {
      var self = this
      $('#london-form').submit(function(e) {
        e.preventDefault()
        self._displayLoadingButton()
        self._postFormData($('#london-form'))
      })
    },

    _postFormData: function(form) {
      $.ajax({
        type: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: (data) => {
          this._hideInputForm()
          this._displayResults(data)
        }
      })
    },

    // _getResults: function(data) {
    //   var url = "/result"
    //   $.get(url, (data) => {
    //     this._displayResults(data)
    //   })
    // },

    _displayResults: function(data) {
      var self = this
      var text = data.text
      var response_dict = data.response_dict
      $('#results').show()
      $('#results').html(self.resultsView.renderUsersInputText(text))
      $('#results').append(self.resultsView.renderProgressDiv())
      $('#progress-results').append(self.resultsView.renderProgressBars(response_dict))
    },

    _displayLoadingButton: function() {
      var self = this
      $('#button-spinner').addClass(self.homepageView.form.button.renderSpinnerClass())
      $('#button-text').text(self.homepageView.form.button.renderLoadingText())
    },

    _hideInputForm: function() {
      $("#london-input-form").hide()
    },

    _hideresults: function() {
      $('#results').hide()
    }

  }

  exports.Controller = Controller
})(this)
