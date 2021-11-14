window.onscroll = function() {myFunction()};

//progress bar

function myFunction() {
  var winScroll = document.body.scrollTop ;
  var height = document.body.scrollHeight ;
  var scrolled = (winScroll /728) * 100;
  document.getElementById("psbar").style.width = scrolled + "%";
  document.getElementById("a").innerHTML=winScroll  ;
};


//courosone


var TxtRotate = function(el, toRotate, period) {
    this.toRotate = toRotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 2000;
    this.txt = '';
    this.tick();
    this.isDeleting = false;
  };
  
  TxtRotate.prototype.tick = function() {
    var i = this.loopNum % this.toRotate.length;
    var fullTxt = this.toRotate[i];
  
    if (this.isDeleting) {
      this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
      this.txt = fullTxt.substring(0, this.txt.length + 1);
    }
  
    this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';
  
    var that = this;
    var delta = 300 - Math.random() * 100;
  
    if (this.isDeleting) { delta /= 2; }
  
    if (!this.isDeleting && this.txt === fullTxt) {
      delta = this.period;
      this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
      this.isDeleting = false;
      this.loopNum++;
      delta = 500;
    }
  
    setTimeout(function() {
      that.tick();
    }, delta);
  };
  
  window.onload = function() {
    var elements = document.getElementsByClassName('txt-rotate');
    for (var i=0; i<elements.length; i++) {
      var toRotate = elements[i].getAttribute('data-rotate');
      var period = elements[i].getAttribute('data-period');
      if (toRotate) {
        new TxtRotate(elements[i], JSON.parse(toRotate), period);
      }
    }
    // INJECT CSS
    var css = document.createElement("style");
    css.type = "text/css";
    css.innerHTML = ".txt-rotate > .wrap { border-right: 0.08em solid #666 }";
    document.body.appendChild(css);
  };
      

  function linkAction(Id){
    navLink = document.querySelectorAll('.nav-link');

    menu = document.getElementById(Id);
    navLink.forEach(n => n.classList.remove('active'));
    menu.classList.add('active');

    const navMenu = document.getElementById('navMenu')
    navMenu.classList.remove('show')
    flag = false
} 



$(document).ready(function(){
  // This button will increment the value
  $('[data-quantity="plus"]').click(function(e){
      // Stop acting like a button
      e.preventDefault();
      // Get the field name
      fieldName = $(this).attr('data-field');
      // Get its current value
      var currentVal = parseInt($('input[name='+fieldName+']').val());
      // If is not undefined
      if (!isNaN(currentVal)) {
          // Increment
          $('input[name='+fieldName+']').val(currentVal + 1);
      } else {
          // Otherwise put a 0 there
          $('input[name='+fieldName+']').val(0);
      }
  });
  // This button will decrement the value till 0
  $('[data-quantity="minus"]').click(function(e) {
      // Stop acting like a button
      e.preventDefault();
      // Get the field name
      fieldName = $(this).attr('data-field');
      // Get its current value
      var currentVal = parseInt($('input[name='+fieldName+']').val());
      // If it isn't undefined or its greater than 0
      if (!isNaN(currentVal) && currentVal > 0) {
          // Decrement one
          $('input[name='+fieldName+']').val(currentVal - 1);
      } else {
          // Otherwise put a 0 there
          $('input[name='+fieldName+']').val(0);
      }
  });
});


function addCart(name,price) {
    if(sessionStorage.getItem("item_count") === null)
    {
      sessionStorage.setItem("item_count", 1);
      sessionStorage.setItem("item1",name);
      sessionStorage.setItem("item1_price",price);
    }
    else
    {
      var item = parseInt(sessionStorage.getItem("item_count"));
      sessionStorage.setItem("item_count",item+1);
      var item_name = "item"+ item.toString();
      sessionStorage.setItem(item_name,name);
      var iten_price = "item"+ item.toString()+"_price";
      sessionStorage.setItem(iten_price,price);
    }
}      

function viewCart(){
  console.log("in view cart");
  var div = document.getElementById("view");
  var text = "<div class=\"row pt-2\"> <div class=\"col-8 text-center\">Food Item</div> <div class=\"col-3 text-center\">Price</div></div>";
  var item =parseInt(sessionStorage.getItem("item_count"));
  var total=0;
  for (let i = 1; i <= item; i++) {
    text = text + "<hr>";
    text = text + "<div class=\"row pt-2 pb-2\">";
    text = text + "    <div class=\"col-4\">";
    text = text + "        <img class=\"card-img\" style=\"height: 75px; width: 50%;border-radius: 5%; \" src=\"static/image/r1.jpg\" onerror=\"this.src='../static/img/alt.png';\" >";
    text = text + "    </div>";
    text = text + "    <div class=\"col-4\">";
    var item_name = "item"+ i.toString();
    text = text + "        <span><p class=\"card-title \" style=\"text-align: left;font-size: 1vw;\">" + sessionStorage.getItem(item_name) + "</p>  </span>";
    text = text + "    </div>";
    text = text + "   <div class=\"col-3\">";
    var iten_price = "item"+ i.toString()+"_price";
    total = total + parentInt(sessionStorage.getItem(iten_price));
    text = text + "        <p style=\"text-align: center;width: 50%; margin: 0;\">"+ sessionStorage.getItem(iten_price) +"Rs.</p>";
    text = text + "    </div>"
    text = text + "</div>"
  }
  text = text + "<hr>";
  text = text + "      <div class=\"row pt-2 pb-2\">";
  text = text + "<div class=\"col-4\">";
  text = text + "          </div>";
  text = text + "<div class=\"col-4\">";
  text = text + "            </div>";
  text = text + "<div class=\"col-3\">";
  text = text + "                <p style=\"text-align: center;width: 50%; margin: 0;\">Total :"+ total.toString() + "Rs.</p>";
  text = text + "</div>";
  text = text + "</div>";

  div.innerHTML = text;
}