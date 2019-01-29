(function(exports) {

  function Controller(homepageView = new HomepageView) {
    this.homepageView = homepageView
  }

  Controller.prototype = {
    displayHomepage: function() {
      this._hideresults()
      $('#london-input-form').html(this.homepageView.render())
    },

    _hideresults: function() {
      $('#results').hide()
    }
  }

  exports.Controller = Controller
})(this)
