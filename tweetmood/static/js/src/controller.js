(function(exports) {

  function Controller() {

  }

  Controller.prototype = {
    displayHomepage: function() {
      this._hideresults()
    },

    _hideresults: function() {
      $('#results').hide()
    }
  }

  exports.Controller = Controller
})(this)
