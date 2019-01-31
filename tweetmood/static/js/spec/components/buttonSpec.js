describe("Button", function() {

  describe("render", function() {
    it("returns the button html", function() {
      var expectedResult = '<button id="button_loader" name="analyse" class="btn btn-custom btn-block mb-2" type="submit"><span id="button-text">Ask Holmes & Watson...</span><span id="button-spinner" class="" role="status" aria-hidden="false"></span></button>'
      expect(Button.render()).toEqual(expectedResult)
    })
  })

  describe("renderSpinnerClass", function() {
    it("returns the spinnner class information", function() {
      expect(Button.renderSpinnerClass()).toEqual("spinner-border spinner-border-sm")
    })
  })

  describe("renderLoadingText", function() {
    it("returns the loading text", function() {
      expect(Button.renderLoadingText()).toEqual('Hmmm...a 3 patch problem...')
    })
  })
})
