describe("Form", function() {

  describe("render", function() {
    it("returns renders the forms's html", function() {
      spyOn(Button, "render").and.returnValue("<button></button>")
      var expectResult = '<div id="input-form" class="row col-md-6 offset-md-3 text-center"><form id="london-form" class="form-inline" action="/analysis" method="post"><h1>How does London feel about <input class="form-control" id="city-form-input" type="text" name="text" value=""> right now?</h1><button></button></form></div>'
      expect(Form.render()).toEqual(expectResult)
    })

    it("calls the button to render in the form", function() {
      spyOn(Button, "render")
      Form.render()
      expect(Button.render).toHaveBeenCalled();
    })
  })

})
