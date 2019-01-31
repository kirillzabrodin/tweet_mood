(function(exports) {

  function ResultsView() {}

  ResultsView.prototype = {

    render: function(user_text, watson_res, holmes_res) {
      if (!holmes_res.feeling) {
        return ErrorMessage.render(user_text)
      } else {
        return [
          HolmesHeader.render(user_text, holmes_res),
          HolmesResults.render(holmes_res),
          WatsonHeader.render(),
          WatsonResults.render(watson_res)
        ].join("")
      }
    }

  }

  exports.ResultsView = ResultsView
})(this)
