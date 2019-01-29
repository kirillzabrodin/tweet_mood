(function(exports) {

  function Button() {}

  Button.prototype = {
    render: function() {
      return '<button id="button_loader" name="analyse" class="btn btn-custom btn-block mb-2" type="submit"><span id="button-text">click to find out</span><span id="button-spinner" class="" role="status" aria-hidden="false"></span></button>'
    },

    renderSpinnerClass: function() {
      return "spinner-border spinner-border-sm"
    }
  }

  exports.Button = Button
})(this)



// export class Button {
//
//   renderSpinnerClass() {
//     return "spinner-border spinner-border-sm"
//   }
//
//   renderLoadingText() {
//     return 'loading...'
//   }
//
//   render() {
//     return '<button id="button_loader" name="analyse" class="btn btn-custom btn-block mb-2" type="submit"><span id="button-text">click to find out</span><span id="button-spinner" class="" role="status" aria-hidden="false"></span></button>'
//   }
//
// }
//
// export default Button
