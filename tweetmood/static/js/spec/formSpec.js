describe("Form", function() {

  var form
  var button

  beforeEach(function() {
    button = jasmine.createSpyObj('button',['render']);
    form = new Form(button)
  })

  describe("render", function() {
    it("returns renders the forms's html", function() {
      expect(form.render()).toEqual('<div class="row col-md-6 offset-md-3 text-center"><form id="london-form" class="form-inline" action="/analysis" method="post"><h1>How does London feel about <input class="form-control" id="city-form-input" type="text" name="text" value=""> right now?</h1>undefined</form></div>')
    })

    it("calls the button to render in the form", function() {
      form.render()
      expect(button.render).toHaveBeenCalled();
    })
  })

})
