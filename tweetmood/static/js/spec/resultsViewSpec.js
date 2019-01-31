describe("ResultsView", function() {

  var resultsView
  var userText
  var watsonRes
  var holmesRes

  describe("render", function() {

    describe("when holmes has feeling", function() {

      beforeEach(function() {
        userText = "foo"
        watsonRes = {"joy": 10, "anger": 0}
        holmesRes = {"pos": 50, "neg": 50, "pwid": 25, "nwid": 25, "feeling": "ambivalent"}
        resultsView = new ResultsView()
      })

      it("calls HolmesHeader.render", function() {
        spyOn(HolmesHeader, "render")
        resultsView.render(userText, watsonRes, holmesRes)
        expect(HolmesHeader.render).toHaveBeenCalledWith(userText, holmesRes)
      })

      it("calls HolmesResults.render", function() {
        spyOn(HolmesResults, "render")
        resultsView.render(userText, watsonRes, holmesRes)
        expect(HolmesResults.render).toHaveBeenCalledWith(holmesRes)
      })

      it("calls WatsonHeader.render", function() {
        spyOn(WatsonHeader, "render")
        resultsView.render(userText, watsonRes, holmesRes)
        expect(WatsonHeader.render).toHaveBeenCalledWith()
      })

      it("calls WatsonResults.render", function() {
        spyOn(WatsonResults, "render")
        resultsView.render(userText, watsonRes, holmesRes)
        expect(WatsonResults.render).toHaveBeenCalledWith(watsonRes)
      })

      it("does not call ErrorMessage.render", function() {
        spyOn(ErrorMessage, "render")
        resultsView.render(userText, watsonRes, holmesRes)
        expect(ErrorMessage.render).not.toHaveBeenCalledWith(userText)
      })
    })

    describe("when holmes does not have feeling", function() {
      beforeEach(function() {
        userText = "foo"
        watsonRes = {"joy": 10, "anger": 0}
        holmesRes = {}
        resultsView = new ResultsView()
      })

      it("does not call HolmesHeader.render", function() {
        spyOn(HolmesHeader, "render")
        resultsView.render(userText, watsonRes, holmesRes)
        expect(HolmesHeader.render).not.toHaveBeenCalledWith(userText, holmesRes)
      })

      it("does not call HolmesResults.render", function() {
        spyOn(HolmesResults, "render")
        resultsView.render(userText, watsonRes, holmesRes)
        expect(HolmesResults.render).not.toHaveBeenCalledWith(holmesRes)
      })

      it("does not call WatsonHeader.render", function() {
        spyOn(WatsonHeader, "render")
        resultsView.render(userText, watsonRes, holmesRes)
        expect(WatsonHeader.render).not.toHaveBeenCalledWith()
      })

      it("does not call WatsonResults.render", function() {
        spyOn(WatsonResults, "render")
        resultsView.render(userText, watsonRes, holmesRes)
        expect(WatsonResults.render).not.toHaveBeenCalledWith(watsonRes)
      })

      it("calls ErrorMessage.render", function() {
        spyOn(ErrorMessage, "render")
        resultsView.render(userText, watsonRes, holmesRes)
        expect(ErrorMessage.render).toHaveBeenCalledWith(userText)
      })
    })
  })

})
