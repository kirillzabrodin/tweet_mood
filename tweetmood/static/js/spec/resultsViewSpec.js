describe("ResultsView", function() {

  var resultsView

  beforeEach(function() {
    resultsView = new ResultsView()
  })

  describe("_renderHolmesHeader", function() {
    it("returns Holmes Header information in html", function() {
      var text = 'Test'
      var data = { "pos" : 50, "neg" : 50, "pwid" : 25, "nwid" : 25, "feeling" : "ambivalent" }
      var result = resultsView._renderHolmesHeader(text, data)
      var expectedResult = '<h2 id="users-text">Holmes deduced that London feels ambivalent about Test:</h2>'
      expect(result).toEqual(expectedResult)
    })
  })

  describe("_renderHolmesResult", function() {
    it("adds Holmes results to html", function() {
      var data = { "pos" : 50, "neg" : 50, "pwid" : 25, "nwid" : 25, "feeling" : "ambivalent" }
      var result = resultsView._renderHolmesResult(data)
      var expectedResult = "<table class='table table-borderless table-hover'><thead><tr><td class='table-secondary' style='width:25%'></td><td class='table-danger' style='width:25%'><h3>-ve 50%</h3></td><td class='table-success' style='width:25%'><h3>+ve 50%</h3></td><td class='table-secondary' style='width:25%'></td></tr></thead></table>"
      expect(result).toEqual(expectedResult)
    })
  })

  describe("_renderWatsonHeader", function() {
    it("returns Watson Header information in html", function() {
      var result = resultsView._renderWatsonHeader()
      var expectedResult = '<h2>Meanwhile, Watson had a more nuanced take:</h2>'
      expect(result).toEqual(expectedResult)
    })
  })

  describe("_renderProgressBars", function() {
    it("returns html of progress bars with data added", function() {
      var data = { "Joy" : 10, "Anger" : 0  }
      var result = resultsView._renderProgressBars(data)
      expectedResult = "<h1>Joy - 10%</h1><div id='progress-results' class='progress'><div id='Joy' class='progress-bar-striped progress-bar-Joy' role='progressbar' style='width: 10%' aria-valuenow='10' aria-valuemin='0' aria-valuemax='100'></div>'</div><h1>Anger - 0%</h1><div id='progress-results' class='progress'><div id='Anger' class='progress-bar-striped progress-bar-Anger' role='progressbar' style='width: 0%' aria-valuenow='0' aria-valuemin='0' aria-valuemax='100'></div>'</div>"
      expect(result).toEqual(expectedResult)
    })
  })

  describe("_renderProgressResultsDiv", function() {
    it("returns progress results div html", function() {
      var result = resultsView._renderProgressDiv()
      var expectedResult = '<div id="progress-results"></div>'
      expect(result).toEqual(expectedResult)
    })
  })

  describe("_renderErrorMessage", function() {
    it("returns an error message in html", function() {
      var result = resultsView._renderErrorMessage("Error")
      var expectedResult = '<h2 id="users-text">Error</h2>'
      expect(result).toEqual(expectedResult)
    })
  })

})
