(function(exports) {

  function Controller(homepageView = new HomepageView) {
    this.homepageView = homepageView
  }

  Controller.prototype = {
    displayHomepage: function() {
      this._hideresults()
      $('#london-input-form').html(this.homepageView.render())
      this._listenForLondonFormSubmit()
    },

    _listenForLondonFormSubmit: function() {
      var self = this
      $('#london-form').submit(function(e) {
        e.preventDefault()
        console.log('fuck off jasmine')
        self.displayLoadingButton()
        // self.postFormData($('#london-form'))
      })
    },

    displayLoadingButton: function() {

    },

    _hideresults: function() {
      $('#results').hide()
    }


  }

  exports.Controller = Controller
})(this)
