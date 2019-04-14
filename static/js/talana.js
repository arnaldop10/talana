/*
	Talana JavaScript File
*/
if (window.location.pathname === '/upload/') {
	const prev_photo = document.getElementById('prev_photo')
	const photo_pet = document.getElementById('id_photo_pet')
	const controls = document.getElementById('controls')
	const rotatePlus = document.getElementById('rotate90+')
	const rotateMinus = document.getElementById('rotate90-')
	const rotateV = document.getElementById('rotateV')
	const rotateH = document.getElementById('rotateH')

	prev_photo.style.display = 'none'

	rotatePlus.onclick = (event) => {
		event.preventDefault()
		prev_photo.style.transform = "rotate(90deg)"
	}

	rotateMinus.onclick = (event) => {
		event.preventDefault()
		prev_photo.style.transform = "rotate(-90deg)"
	}

	rotateV.onclick = (event) => {
		event.preventDefault()
		prev_photo.style.transform = "scaleX(-1)"
	}

	rotateH.onclick = (event) => {
		event.preventDefault()
		prev_photo.style.transform = "scaleY(-1)"
	}

	photo_pet.onchange = (event) => {
		event.preventDefault()
		upload_img(photo_pet, prev_photo, controls)
	}

	function upload_img(input, prev_photo, controls) {
	    if (input.files && input.files[0]) {
	        var reader = new FileReader();

	        reader.onload = function (e) {
	        		prev_photo.style.display = 'block';
	            prev_photo.setAttribute('src', e.target.result);
	            controls.style.display = 'block';
	        }

	        reader.readAsDataURL(input.files[0]);
	    }
	}
} else {
	/* 
	 Sección para votar
	*/

	getUserIP(function(ip){
		let inputs = document.getElementsByName('ip')
		inputs.forEach( function(el) {
			el.value = ip
		});
	});

	function getCookie(cname) {
	  var name = cname + "=";
	  var decodedCookie = decodeURIComponent(document.cookie);
	  var ca = decodedCookie.split(';');
	  for(var i = 0; i <ca.length; i++) {
	    var c = ca[i];
	    while (c.charAt(0) == ' ') {
	      c = c.substring(1);
	    }
	    if (c.indexOf(name) == 0) {
	      return c.substring(name.length, c.length);
	    }
	  }
	  return "";
	}

	if (getCookie('ip')) {
		let buttons = document.getElementsByClassName('btn')
		for (var i = 0; i < buttons.length; i++) {
			buttons[i].setAttribute('disabled', 'true')
		}
	}

}