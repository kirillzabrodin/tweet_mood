(function(exports) {

  function HomepageView(form = new Form) {
    this.form = form
  }

  HomepageView.prototype = {
    render: function() {
      return this.form.render()
    }
  }

  exports.HomepageView = HomepageView
})(this)
