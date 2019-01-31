var HolmesResults = (function() {

  function render(holmes_res) {
    return `<table class='table table-borderless table-hover'><thead><tr><td class='table-secondary' style='width:${holmes_res.pwid}%'></td><td class='table-danger' style='width:${holmes_res.nwid}%'><h3>-ve ${holmes_res.neg}%</h3></td><td class='table-success' style='width:${holmes_res.pwid}%'><h3>+ve ${holmes_res.pos}%</h3></td><td class='table-secondary' style='width:${holmes_res.nwid}%'></td></tr></thead></table>`
  }

  return {
    render: render
  }

})()
