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

  describe("renderHolmesResult", function() {
    it("adds Holmes results to html", function() {
      var data = { "pos" : 50, "neg" : 50, "pwid" : 25, "nwid" :25 }
      var result = resultsView.renderHolmesResult(data)
      var expectedResult = "<table class='table table-hover'><thead><tr><td style='width:25%'></td><td class='bg-danger' style='width:25%'><h3>-ve 50%</h3></td><td class='bg-success' style='width:25%'><h3>+ve 50%</h3></td><td style='width:25%'></td></tr></thead></table>"
      expect(result).toEqual(expectedResult)
    })
  })

})
