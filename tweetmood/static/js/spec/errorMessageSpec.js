describe("ErrorMessage", function() {

  describe("render", function() {
    it("returns the html", function() {
      var expectedResult = '<h2 id="users-text">error</h2>'
      var result = ErrorMessage.render('error')
      expect(expectedResult).toEqual(result)
    })
  })

})
