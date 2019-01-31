describe("HolmesResults", function() {

  describe("render", function() {
    it("returns the html", function() {
      var holmes_res = {"pos": 50, "neg": 50, "pwid": 25, "nwid": 25, "feeling": "ambivalent"}
      var expectedResult = "<table id='holmes-results' class='table table-hover'><thead><tr><td style='width:25%'></td><td class='bg-danger' style='width:25%'><h3>-ve 50%</h3></td><td class='bg-success' style='width:25%'><h3>+ve 50%</h3></td><td style='width:25%'></td></tr></thead></table>"
      var result = HolmesResults.render(holmes_res)
      expect(expectedResult).toEqual(result)
    })
  })

})
