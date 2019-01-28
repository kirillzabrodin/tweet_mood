export class Form {
  render() {
    return '<div class="row col-md-6 offset-md-3 text-center"><form id="london-form" class="form-inline" action="/analysis" method="post">{% csrf_token %}<h1>How does London feel about <input class="form-control" id="city-form-input" type="text" name="text" value=""> right now?</h1></form></div>'
  }
}
export default Form
