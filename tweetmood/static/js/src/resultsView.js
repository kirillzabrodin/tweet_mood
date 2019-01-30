(function(exports) {

  function ResultsView() {}

  ResultsView.prototype = {

    renderProgressBars: function(data) {
      var results = []
      for(var tone in data) {
        var toneName = tone
        var toneScore = data[tone]
        results.push(`<h1>${toneName} - ${toneScore}%</h1><div id='progress-results' class='progress'><div id='${toneName}' class='progress-bar-striped progress-bar-${toneName}' role='progressbar' style='width: ${toneScore}%' aria-valuenow='${toneScore}' aria-valuemin='0' aria-valuemax='100'></div>'</div>`)
      }
      return results.join("")
    },

    renderProgressDiv: function() {
      return '<div id="progress-results"></div>'
    },

    renderUsersInputText: function(text) {
      return `<h1 id="users-text">${text}</h1>`
    },

    renderHolmesResult: function(data) {
      return `<table class='table table-hover'><thead><tr><td style='width:${data.pwid}%'></td><td class='bg-danger' style='width:${data.nwid}%'><h3>-ve ${data.neg}%</h3></td><td class='bg-success' style='width:${data.pwid}%'><h3>+ve ${data.pos}%</h3></td><td style='width:${data.nwid}%'></td></tr></thead></table>`
    }
  }

  exports.ResultsView = ResultsView
})(this)
