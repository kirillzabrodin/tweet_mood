import Form from './components/form.js'

export class HomepageView {
  constructor(form = new Form) {
    this.form = form
  }

  render() {
    return this.form.render()
  }

}

export default HomepageView
