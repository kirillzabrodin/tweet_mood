export class ResultsView {

  renderProgressBars(data) {
    let results = []
    for(var tone in data) {
      let toneName = tone
      let toneScore = data[tone]
      results.push(`<h1>${toneName} - ${toneScore}%</h1><div id='progress-results' class='progress'><div id='${toneName}' class='progress-bar progress-bar-${toneName}' role='progressbar' style='width: ${toneScore}%' aria-valuenow='${toneScore}' aria-valuemin='0' aria-valuemax='100'></div>'</div>`)
    }
    return results.join("")
  }

  renderProgressResultsDiv() {
    return '<div id="progress-results"></div>'
  }

  renderUsersInputText(text) {
    return `<h1 id="users-text">${text}</h1>`
  }

  renderProgressBarDiv() {
    return '<div id="progress-results"></div>'
  }
}

export default ResultsView
