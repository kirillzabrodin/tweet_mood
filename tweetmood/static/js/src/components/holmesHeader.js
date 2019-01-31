(function(exports) {

  function HolmesHeader() {}

  HolmesHeader.prototype = {
    render: function(user_text, holmes_res) {
      return `<h2 id="users-text", style="color:white;text-align:center">Holmes has deduced that London feels ${holmes_res.feeling} about ${user_text}:</h2>`
    },
  }

  exports.HolmesHeader = HolmesHeader
})(this)
