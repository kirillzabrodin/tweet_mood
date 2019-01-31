var WatsonResults = (function() {

  var results = []

  function render(watson_res) {
    for(var tone in watson_res) {
      var toneName = tone
      var toneScore = watson_res[tone]
      results.push(`<h1>${toneName} - ${toneScore}%</h1><div id='progress-results' class='progress'><div id='${toneName}' class='progress-bar-striped progress-bar-${toneName}' role='progressbar' style='width: ${toneScore}%' aria-valuenow='${toneScore}' aria-valuemin='0' aria-valuemax='100'></div>'</div>`)
    }
    return [
      "<div id='progress=results'>",
      results.join(""),
      '</div>'
    ].join("")
  }

  return {
    render: render
  }

})()
