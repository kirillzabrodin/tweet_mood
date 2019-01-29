describe("Home page", function() {
  it("contains title", function(){
		cy.visit('localhost:8000');
    cy.get("title")
    cy.should('contain', 'tweetmood');
	})
  it("loads home page correctly", function() {
    cy.visit("localhost:8000");
  })
  it("contains the first part of title", function() {
    cy.get("h1")
    cy.should('contain', "How does London feel about")
  })
  it("contains the second part of title below text box", function() {
    cy.get("h1")
    cy.should('contain', "right now?")
  })
  it("contains button", function() {
    cy.get("button")
    cy.should('contain', "click to find out")
  })
  it("allows you to type input", function() {
    cy.visit('localhost:8000')
    cy.get("form")
    cy.get('Input[name="text"]')
    .type('I am very happy about cypress testing')
    .should('have.value', 'I am very happy about cypress testing')

})
it("allows you to type input", function() {
  cy.visit('localhost:8000')
  cy.get("form")
  cy.get('Input[name="text"]')
  .type('I am very happy about cypress testing')
  cy.get('button')
  .click()
})
it("contains the input as the title", function() {
  cy.get("h1")
  cy.should('contain', "I am very happy about cypress testing")
})
it("contains Joy title", function() {
  cy.get("h2")
  cy.should('contain', "Joy")
})
it("contains Anger title", function() {
  cy.get("h2")
  cy.should('contain', "Anger")
})
it("contains Sadness title", function() {
  cy.get("h2")
  cy.should('contain', "Sadness")
})
it("contains Analytical title", function() {
  cy.get("h2")
  cy.should('contain', "Analytical")
})
it("contains Fear title", function() {
  cy.get("h2")
  cy.should('contain', "Fear")
})
it("contains Disgust title", function() {
  cy.get("h2")
  cy.should('contain', "Disgust")
})
it("contains title after submitting", function(){
  cy.visit('localhost:8000');
  cy.get("title")
  cy.should('contain', 'tweetmood');
})
});
