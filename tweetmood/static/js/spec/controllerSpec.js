describe("Controller", function() {

  var controller
  var resultsView
  var homepageView

  beforeEach(function() {
    controller = new Controller()
  })

  describe("displayHomepage", function() {
    it("hids the results section", function() {
      spyOn($.fn, "hide")
      controller.displayHomepage()
      expect($.fn.hide).toHaveBeenCalled()
    })
  })

})
