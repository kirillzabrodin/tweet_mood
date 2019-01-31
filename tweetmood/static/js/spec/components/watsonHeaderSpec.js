describe("WatsonHeader", function() {

  describe("render", function() {
    it("returns the html", function() {
      var expectedResult = '<h2 style="color:white;text-align:center">Meanwhile, Watson had a more nuanced take:</h2>'
      var result = WatsonHeader.render()
      expect(expectedResult).toEqual(result)
    })
  })

})
