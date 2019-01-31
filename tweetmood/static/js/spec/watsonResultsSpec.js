describe("WatsonResults", function() {

  describe("render", function() {
    it("returns the html", function() {
      var data = { "Joy" : 10, "Anger" : 0  }
      expectedResult = "<div id='progress=results'><h1>Joy - 10%</h1><div id='progress-results' class='progress'><div id='Joy' class='progress-bar-striped progress-bar-Joy' role='progressbar' style='width: 10%' aria-valuenow='10' aria-valuemin='0' aria-valuemax='100'></div>'</div><h1>Anger - 0%</h1><div id='progress-results' class='progress'><div id='Anger' class='progress-bar-striped progress-bar-Anger' role='progressbar' style='width: 0%' aria-valuenow='0' aria-valuemin='0' aria-valuemax='100'></div>'</div></div>"
      var result = WatsonResults.render(data)
      expect(expectedResult).toEqual(result)
    })
  })

})
