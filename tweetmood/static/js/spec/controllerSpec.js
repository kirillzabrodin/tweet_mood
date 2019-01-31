describe("Controller", function() {

  var controller
  var homepageView

  beforeEach(function() {
    homepageView = jasmine.createSpyObj('homepageView', ['render'])
    resultsView = jasmine.createSpyObj('resultsView', ['render'])
    controller = new Controller(resultsView, homepageView)
  })

  describe("displayHomepage", function() {
    it("renders the homepage view", function() {
      spyOn($.fn, "html")
      controller.displayHomepage()
      expect($.fn.html).toHaveBeenCalledWith(homepageView.render())
    })

    it("listens for form submit", function() {
      spyOn(controller, "_listenForFormSubmit")
      controller.displayHomepage()
      expect(controller._listenForFormSubmit).toHaveBeenCalled()
    })
  })

})
