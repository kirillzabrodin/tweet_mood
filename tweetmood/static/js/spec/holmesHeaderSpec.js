describe("HolmesHeader", function() {

  var holmesHeader

  beforeEach(function() {
    holmesHeader = new HolmesHeader()
  })

  describe("render", function() {
    it("returns the html", function() {
      var holmes_res = {"feeling" : "happy"}
      var expectedResult = '<h2 id="users-text", style="color:white;text-align:center">Holmes has deduced that London feels happy about life:</h2>'
      var result = holmesHeader.render('life', holmes_res)
      expect(expectedResult).toEqual(result)
    })
  })

})
