(function(exports) {

  function ResultsView() {}

  ResultsView.prototype = {

    render: function(user_text, watson_res, holmes_res) {
      if (holmes_res.feeling) {
        return [
          HolmesHeader.render(user_text, holmes_res),
          HolmesResults.render(holmes_res),
          WatsonHeader.render(),
          WatsonResults.render(watson_res)
        ].join("")
      }
      else {
        return ErrorMessage.render(user_text)
      }
    }

  }

  exports.ResultsView = ResultsView
})(this)
