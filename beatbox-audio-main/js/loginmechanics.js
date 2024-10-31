var loginbutton = document.getElementById("loginbutton");


function openPop(){
	var popup = document.getElementById("popup").style.display = "block";
}


function glow(event){
	loginbutton.setAttribute('style','background-color: blue');
	setTimeout(5);
	loginbutton.setAttribute('style','background-color: purple');
}

function openForm() {
  document.getElementById("login-popup").style.display = "block";
}

function closeForm() {
  document.getElementById("login-popup").style.display = "none";
  	document.getElementById("signon").style.display = "none";
	document.getElementById("areyounew").style.display = "block";
	document.getElementById("areyouold").style.display = "none";
	document.getElementById('signuphere').style.display = "block";
	document.getElementById('logintext').textContent = "Log-in";
	document.getElementById("alreadyhaveaccount").style.display = "none";
}
