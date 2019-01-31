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

    _renderHolmesHeader: function(user_text, data) {
      return `<h2 id="users-text">Holmes has deduced that London feels ${data.feeling} about ${user_text}:</h2>`
    },

    _renderHolmesResult: function(holmes_res) {
      return `<table class='table table-hover'><thead><tr><td style='width:${holmes_res.pwid}%'></td><td class='bg-danger' style='width:${holmes_res.nwid}%'><h3>-ve ${holmes_res.neg}%</h3></td><td class='bg-success' style='width:${holmes_res.pwid}%'><h3>+ve ${holmes_res.pos}%</h3></td><td style='width:${holmes_res.nwid}%'></td></tr></thead></table>`
    },

    _renderWatsonHeader: function(data) {
        return '<h2>Meanwhile, Watson had a more nuanced take:</h2>'
    },

    _renderWatsonResult: function(watson_res) {
      var results = []
      for(var tone in watson_res) {
        var toneName = tone
        var toneScore = watson_res[tone]
        results.push(`<h1>${toneName} - ${toneScore}%</h1><div id='progress-results' class='progress'><div id='${toneName}' class='progress-bar-striped progress-bar-${toneName}' role='progressbar' style='width: ${toneScore}%' aria-valuenow='${toneScore}' aria-valuemin='0' aria-valuemax='100'></div>'</div>`)
      }
      return [
        '<div id="progress=results">',
        results.join(""),
        '</div>'
      ].join("")
    },

    _renderErrorMessage: function(user_text) {
      return `<h2 id="users-text">${user_text}</h2>`
    }

  }

  exports.ResultsView = ResultsView
})(this)
