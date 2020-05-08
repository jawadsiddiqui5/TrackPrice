// content.js
var tpBox = document.createElement("div");
tpBox.style.width="450px";
tpBox.style.border="1px solid black";

var trackPriceText = document.createElement('p');
trackPriceText.innerHTML = 'Track Price';
trackPriceText.style.color = "blue";

var desc =  document.createElement('p');
trackPriceText.style.color = "green";
trackPriceText.style.margin = 0;
desc.innerHTML  = "Congratulations! You are getting the best price";

var priceHist =  document.createElement('p');

priceHist.innerHTML = '<a href="#" style="margin:0;padding:0">Check price history</a>';
priceHist.style.margin = 0;

tpBox.appendChild(trackPriceText);
tpBox.appendChild(desc);
tpBox.appendChild(priceHist);
// tpBox.innerHTML = trackPriceText + desc + priceHist; 

document.getElementById("priceblock_ourprice").appendChild(tpBox);
