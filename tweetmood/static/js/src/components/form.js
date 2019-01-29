import Button from './button.js'

export class Form {
  constructor(button = new Button) {
    this.button = button
  }
  render() {
    return '<div class="row col-md-6 offset-md-3 text-center"><form id="london-form" class="form-inline" action="/analysis" method="post"><h1>How does London feel about <input class="form-control" id="city-form-input" type="text" name="text" value=""> right now?</h1>' + this.button.render() + '</form></div>'
  }
}
export default Form
