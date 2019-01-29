import ResultsView from './resultsView.js'
import Button from './components/button.js'
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
    let self = this
    $('#london-form').submit(function(e) {
      e.preventDefault()
      self.displayLoadingButton()
      let form = $(this)
        self.postFormData(form)
    })
  }

  postFormData(form) {
    let self = this
    $.ajax({
      type: form.attr('method'),
      url: form.attr('action'),
      data: form.serialize(),
      success: function(data) {
        self.hideInputForm()
        self.getResults(data)
      }
    })
  }

  getResults(data) {
    let self = this
    let url = "http://localhost:8000/result"
    $.get(url, function(data) {
      self.displayResults(data)
    })
  }

  displayResults(data) {
    let self = this
    let text = data.text
    let response_dict = data.response_dict
    $('#results').show()
    $('#results').append(self.resultsView.renderUsersInputText(text))
    $('#results').append(self.resultsView.renderProgressResultsDiv())
    $('#progress-results').append(self.resultsView.renderProgressBars(response_dict))
  }

  hideresults() {
    $('#results').hide()
  }

  hideInputForm() {
    $("#london-input-form").hide()
  }

  displayButton() {
    let self = this
    $('#london-form').append(self.homepageView.button.renderButton())
  }

  displayLoadingButton() {
    console.log('want to display loading button')
    $('#button-spinner').addClass(this.homepageView.form.button.renderSpinnerClass())
    $('#button-text').text(this.homepageView.form.button.renderLoadingText())
  }

}

export default Controller
