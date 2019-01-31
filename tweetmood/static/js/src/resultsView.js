(function(exports) {

  function ResultsView() {}

  ResultsView.prototype = {

    render: function(user_text, watson_res, holmes_res) {
      if (holmes_res.feeling) {
        return [
          this._renderHolmesHeader(user_text, holmes_res),
          this._renderHolmesResult(holmes_res),
          this._renderWatsonHeader(),
          this._renderWatsonResult(watson_res)
        ].join("")
      }
      else {
        return this._renderErrorMessage(user_text)
      }
    },

    _renderHolmesHeader: function(user_text, holmes_res) {
      HolmesHeader.render(user_text, holmes_res)
    },

    _renderHolmesResult: function(holmes_res) {
      HolmesResults.render(holmes_res)
    },

    _renderWatsonHeader: function(data) {
      WatsonHeader.render(data)
    },

    _renderWatsonResult: function(watson_res) {
      WatsonResults.render(watson_res)
    },
    // done
    _renderErrorMessage: function(user_text) {
      ErrorMessage.render(user_text)
    }

  }

  exports.ResultsView = ResultsView
})(this)
