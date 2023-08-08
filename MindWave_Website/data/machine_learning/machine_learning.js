const ml = [
    {
        "name" : "Churn Prediction",
        "description" : "sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum ",
        "url_link" : "https://google.com"
    },
    {
        "name" : "Churn Prediction",
        "description" : "sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum ",
        "url_link" : "https://google.com"
    }
]

var projectcontainer = document.getElementById("container");
for(var i = 0;i<2;i++){
projectcontainer.innerHTML = `<div class="container 2/6 bg-blue-200" id="projectcontainer">
<div class="flex flex-col">
  <div class="h-1/6 font-bold p-1 text-center" id="headingofproject">$(ml[i].name)</div>
  <div class="text-center p-2" id="projectdescription">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Placeat facere aut unde, eveniet consectetur minus libero ab eius maiores alias fuga corrupti, esse a tempora, cupiditate fugit? Quis, veritatis odit!</div>
  <center><div class="text-blue-800 bg-blue-100 text-center w-36 p-2 mb-2 rounded-full hover:bg-red-700 hover:text-white">Checkout Project<i class="fas fa-arrow-alt-left"></i></div></center>
</div>
</div>`
}