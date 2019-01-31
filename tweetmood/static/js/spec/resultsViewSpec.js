describe("ResultsView", function() {

  var resultsView

  beforeEach(function() {
    resultsView = new ResultsView()
  })

  describe("renderHolmesHeader", function() {
    it("returns Holmes Header information in html", function() {
      var text = 'Test'
      var data = { "pos" : 50, "neg" : 50, "pwid" : 25, "nwid" : 25, "feeling" : "ambivalent" }
      var result = resultsView.renderHolmesHeader(text, data)
      var expectedResult = '<h2 id="users-text">Holmes has deduced that London feels ambivalent about Test:</h2>'
      expect(result).toEqual(expectedResult)
    })
  })

  describe("renderHolmesResult", function() {
    it("adds Holmes results to html", function() {
      var data = { "pos" : 50, "neg" : 50, "pwid" : 25, "nwid" : 25, "feeling" : "ambivalent" }
      var result = resultsView.renderHolmesResult(data)
      var expectedResult = "<table class='table table-hover'><thead><tr><td style='width:25%'></td><td class='bg-danger' style='width:25%'><h3>-ve 50%</h3></td><td class='bg-success' style='width:25%'><h3>+ve 50%</h3></td><td style='width:25%'></td></tr></thead></table>"
      expect(result).toEqual(expectedResult)
    })
  })

  describe("renderWatsonHeader", function() {
    it("returns Watson Header information in html", function() {
      var result = resultsView.renderWatsonHeader()
      var expectedResult = '<h2>Meanwhile, Watson had a more nuanced take:</h2>'
      expect(result).toEqual(expectedResult)
    })
  })

  describe("renderProgressBars", function() {
    it("returns html of progress bars with data added", function() {
      var data = { "Joy" : 10, "Anger" : 0  }
      var result = resultsView.renderProgressBars(data)
      expectedResult = "<h1>Joy - 10%</h1><div id='progress-results' class='progress'><div id='Joy' class='progress-bar-striped progress-bar-Joy' role='progressbar' style='width: 10%' aria-valuenow='10' aria-valuemin='0' aria-valuemax='100'></div>'</div><h1>Anger - 0%</h1><div id='progress-results' class='progress'><div id='Anger' class='progress-bar-striped progress-bar-Anger' role='progressbar' style='width: 0%' aria-valuenow='0' aria-valuemin='0' aria-valuemax='100'></div>'</div>"
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



})
