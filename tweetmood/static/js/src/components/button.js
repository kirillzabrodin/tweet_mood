(function(exports) {

  function Button() {}

  Button.prototype = {
    render: function() {
      return '<button id="button_loader" name="analyse" class="btn btn-custom btn-block mb-2" type="submit"><span id="button-text">click to find out</span><span id="button-spinner" class="" role="status" aria-hidden="false"></span></button>'
    },

    renderSpinnerClass: function() {
      return "spinner-border spinner-border-sm"
    },

    renderLoadingText: function() {
      return 'loading...'
    }
  }

  exports.Button = Button
})(this)
