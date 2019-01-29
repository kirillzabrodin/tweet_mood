import ResultsView from './resultsView.js'
import HomepageView from './homepageView.js'

export class Controller {
  constructor(resultsView = new ResultsView, homepageView = new HomepageView) {
    this.resultsView = resultsView
    this.homepageView = homepageView
  }

  displayHomepage() {
    this.hideresults()
    $('#london-input-form').html(this.homepageView.render())
    this.listenForLondonFormSubmit()
  }

  listenForLondonFormSubmit() {
    $('#london-form').submit((e) => {
      e.preventDefault()
      this.displayLoadingButton()
      this.postFormData($('#london-form'))
    })
  }

  postFormData(form) {
    $.ajax({
      type: form.attr('method'),
      url: form.attr('action'),
      data: form.serialize(),
      success: (data) => {
        this.hideInputForm()
        this.getResults(data)
      }
    })
  }

  getResults(data) {
    let url = "http://localhost:8000/result"
    $.get(url, (data) => {
      this.displayResults(data)
    })
  }

  displayResults(data) {
    let text = data.text
    let response_dict = data.response_dict
    $('#results').show()
    $('#results').append(this.resultsView.renderUsersInputText(text))
    $('#results').append(this.resultsView.renderProgressResultsDiv())
    $('#progress-results').append(this.resultsView.renderProgressBars(response_dict))
  }

  hideresults() {
    $('#results').hide()
  }

  hideInputForm() {
    $("#london-input-form").hide()
  }

  displayButton() {
    $('#london-form').append(this.homepageView.button.renderButton())
  }

  displayLoadingButton() {
    $('#button-spinner').addClass(this.homepageView.form.button.renderSpinnerClass())
    $('#button-text').text(this.homepageView.form.button.renderLoadingText())
  }

}

export default Controller
