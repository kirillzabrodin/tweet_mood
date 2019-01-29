describe("ResultsView", function() {

  var resultsView

  beforeEach(function() {
    resultsView = new ResultsView()
  })

  describe("renderProgressBars", function() {
    it("returns html of progress bars with data added", function() {
      var data = { "Joy" : 10, "Anger" : 0  }
      var result = resultsView.renderProgressBars(data)
      expectedResult = "<h1>Joy - 10%</h1><div id='progress-results' class='progress'><div id='Joy' class='progress-bar progress-bar-Joy' role='progressbar' style='width: 10%' aria-valuenow='10' aria-valuemin='0' aria-valuemax='100'></div>'</div><h1>Anger - 0%</h1><div id='progress-results' class='progress'><div id='Anger' class='progress-bar progress-bar-Anger' role='progressbar' style='width: 0%' aria-valuenow='0' aria-valuemin='0' aria-valuemax='100'></div>'</div>"
      expect(result).toEqual(expectedResult)
    })
  })

  describe("renderProgressResultsDiv", function() {
    it("returns progress results div html", function() {
      var result = resultsView.renderProgressDiv()
      var expectedResult = '<div id="progress-results"></div>'
      expect(result).toEqual(expectedResult)
    })
  })

  describe("renderUsersInputText", function() {
    it("adds user text to html", function() {
      var result = resultsView.renderUsersInputText('Brexit')
      var expectedResult = '<h1 id="users-text">Brexit</h1>'
      expect(result).toEqual(expectedResult)
    })
  })



})
