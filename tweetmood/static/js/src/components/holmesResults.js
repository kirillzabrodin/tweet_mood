var HolmesResults = (function() {

  function render(holmes_res) {
    return `<table id='holmes-results' class='table table-hover'><thead><tr><td style='width:${holmes_res.pwid}%'></td><td class='bg-danger' style='width:${holmes_res.nwid}%'><h3>-ve ${holmes_res.neg}%</h3></td><td class='bg-success' style='width:${holmes_res.pwid}%'><h3>+ve ${holmes_res.pos}%</h3></td><td style='width:${holmes_res.nwid}%'></td></tr></thead></table>`
  }

  return {
    render: render
  }

})()
