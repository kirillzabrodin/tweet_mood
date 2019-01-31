describe("Button", function() {

  var button

  beforeEach(function() {
    button = new Button()
  })

  describe("render", function() {
    it("returns the button html", function() {
      var expectedResult = '<button id="button_loader" name="analyse" class="btn btn-custom btn-block mb-2" type="submit"><span id="button-text">Ask Holmes & Watson...</span><span id="button-spinner" class="" role="status" aria-hidden="false"></span></button>'
      var result = button.render()
      expect(expectedResult).toEqual(result)
    })
  })

  describe("renderSpinnerClass", function() {
    it("returns the spinnner class information", function() {
      expect(button.renderSpinnerClass()).toEqual("spinner-border spinner-border-sm")
    })
  })

  describe("renderLoadingText", function() {
    it("returns the loading text", function() {
      expect(button.renderLoadingText()).toEqual('Hmmm...a 3 patch problem...')
    })
  })
})
