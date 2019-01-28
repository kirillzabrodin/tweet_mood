export class Button {
  constructor() {}

  renderSpinner() {
    $('#button-spinner').addClass("spinner-border spinner-border-sm")
  }

  renderLoading() {
    $('#button-text').text('loading...')
  }

}

export default Button
