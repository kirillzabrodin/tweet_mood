describe("ResultsView", function() {

  var resultsView

  beforeEach(function() {
    resultsView = new ResultsView()
  })

  describe("_renderHolmesHeader", function() {
    it("calls HolmesHeader.render", function() {
      spyOn(HolmesHeader, "render")
      resultsView._renderHolmesHeader("text", "holmes results")
      expect(HolmesHeader.render).toHaveBeenCalledWith("text", "holmes results")
    })
  })

  describe("_renderHolmesResult", function() {
    it("calls HolmesResults.render", function() {
      spyOn(HolmesResults, "render")
      resultsView._renderHolmesResult("holmes results")
      expect(HolmesResults.render).toHaveBeenCalledWith("holmes results")
    })
  })

  describe("_renderWatsonHeader", function() {
    it("calls WatsonHeader.render", function() {
      spyOn(WatsonHeader, "render")
      resultsView._renderWatsonHeader("data")
      expect(WatsonHeader.render).toHaveBeenCalledWith("data")
    })
  })

  describe("_renderWatsonResults", function() {
    it("calls WatsonResults.render", function() {
      spyOn(WatsonResults, "render")
      resultsView._renderWatsonResult("watson results")
      expect(WatsonResults.render).toHaveBeenCalledWith("watson results")
    })
  })

  describe("_renderErrorMessage", function() {
    it("calls ErrorMessage.render", function() {
      spyOn(ErrorMessage, "render")
      resultsView._renderErrorMessage("error")
      expect(ErrorMessage.render).toHaveBeenCalledWith("error")
    })
  })

})
