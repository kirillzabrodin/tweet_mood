describe("HomepageView", function() {

  var homepageView
  var form

  beforeEach(function() {
    form = jasmine.createSpyObj('form',['render'])
    homepageView = new HomepageView(form)
  })

  describe("render", function() {
    it("calls on the form to render", function() {
      homepageView.render()
      expect(form.render).toHaveBeenCalled()
    })
  })

})
