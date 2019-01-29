(function(exports) {

  function ResultsView() {}

  ResultsView.prototype = {
    renderProgressBars: function(data) {
      var results = []
      for(var tone in data) {
        var toneName = tone
        var toneScore = data[tone]
        results.push(`<h1>${toneName} - ${toneScore}%</h1><div id='progress-results' class='progress'><div id='${toneName}' class='progress-bar progress-bar-${toneName}' role='progressbar' style='width: ${toneScore}%' aria-valuenow='${toneScore}' aria-valuemin='0' aria-valuemax='100'></div>'</div>`)
      }
      return results.join("")
    },

    renderProgressDiv: function() {
      return '<div id="progress-results"></div>'
    },

    renderUsersInputText: function(text) {
      return `<h1 id="users-text">${text}</h1>`
    }
  }

  exports.ResultsView = ResultsView
})(this)

//   renderUsersInputText(text) {
//     return `<h1 id="users-text">${text}</h1>`
//   }
//
//   renderProgressBarDiv() {
//     return '<div id="progress-results"></div>'
//   }
// }
//
// export default ResultsView
