var Form = (function() {

  function render() {
    return '<div class="row col-md-6 offset-md-3 text-center"><form id="london-form" class="form-inline" action="/analysis" method="post"><h1>How does London feel about <input class="form-control" id="city-form-input" type="text" name="text" value=""> right now?</h1>' + Button.render() + '</form></div>'
  }

  return {
    render: render
  }

})()

// (function(exports) {
//
//   function Form(button = new Button) {
//     this.button = button
//   }
//
//   Form.prototype = {
//     render: function() {
//       return '<div class="row col-md-6 offset-md-3 text-center"><form id="london-form" class="form-inline" action="/analysis" method="post"><h1>How does London feel about <input class="form-control" id="city-form-input" type="text" name="text" value=""> right now?</h1>' + this.button.render() + '</form></div>'
//     }
//   }
//
//   exports.Form = Form
// })(this)
