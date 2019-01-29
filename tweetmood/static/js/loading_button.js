window.addEventListener('load', function(){
  console.log(document.getElementById("button_loader"))
  document.getElementById("button_loader").addEventListener("click", function(){
    document.getElementById("button_loader").innerHTML = "Loading...";
  });
});
