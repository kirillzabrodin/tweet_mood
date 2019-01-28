import ResultsView from './resultsView.js'
import Button from './components/button.js'

export class Controller {
  constructor(resultsView = new ResultsView, button = new Button) {
    this.resultsView = resultsView
    this.button = button

    this.hideresults()
    this.listenForFormSubmit()
  }

  listenForFormSubmit() {
    let self = this;
    $('#text-form').submit(function(e) {
      e.preventDefault()
      self.displayLoadingButton()
      let form = $(this)
      $.ajax({
        type: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: function(data) {
          self.hideInputForm()
          self.displayResults(data)
        }
      })
    })
  }

  hideresults() {
    $('#results').hide()
  }

  hideInputForm() {
    $("#london-input-form").hide()
  }

  displayLoadingButton() {
    this.button.renderSpinner()
    this.button.renderLoading()
  }



  displayResults(data) {
    let self = this
    let url = "http://localhost:8000/result"
    $.get(url, function(data) {
      let text = data.text
      let response_dict = data.response_dict
      $('#results').show()
      $('#results').append(self.resultsView.renderUsersInputText(text))
      $('#results').append(self.resultsView.renderProgressResultsDiv())
      $('#progress-results').append(self.resultsView.renderProgressBars(response_dict))
    })
  }
}

export default Controller
