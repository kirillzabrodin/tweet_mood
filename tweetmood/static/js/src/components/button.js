var Button = (function() {

  function render() {
    return '<button id="button_loader" name="analyse" class="btn btn-custom btn-block mb-2" type="submit"><span id="button-text">Ask Holmes & Watson...</span><span id="button-spinner" class="" role="status" aria-hidden="false"></span></button>'
  }

  function renderSpinnerClass() {
    return "spinner-border spinner-border-sm"
  }

  function renderLoadingText() {
    return 'Hmmm...a 3 patch problem...'
  }

  return {
    render: render,
    renderSpinnerClass: renderSpinnerClass,
    renderLoadingText: renderLoadingText
  }

})()


// (function(exports) {
//
//   function Button() {}
//
//   Button.prototype = {
//     render: function() {
//       return '<button id="button_loader" name="analyse" class="btn btn-custom btn-block mb-2" type="submit"><span id="button-text">Ask Holmes & Watson...</span><span id="button-spinner" class="" role="status" aria-hidden="false"></span></button>'
//     },
//
//     renderSpinnerClass: function() {
//       return "spinner-border spinner-border-sm"
//     },
//
//     renderLoadingText: function() {
//       return 'Hmmm...a 3 patch problem...'
//     }
//   }
//
//   exports.Button = Button
// })(this)
