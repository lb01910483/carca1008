
	
	function go_forward() {
		webiopi().callMacro("go_forward");

	}
		
	function go_backward() {
		webiopi().callMacro("go_backward");
	}
		
	function turn_right() {
		webiopi().callMacro("turn_right");
	}
		
	function turn_left() {
		webiopi().callMacro("turn_left");
	}
	function stop() {
		webiopi().callMacro("stop");
	}
	function attack_back() {
		webiopi().callMacro("attack_back");
		spim();
	}
	function attack_stop() {
		webiopi().callMacro("attack_stop");

		spim();
	}
	function attack_turn() {
		webiopi().callMacro("attack_turn");

		spim();
	}		
	function change(){
		  var c=Math.floor(Math.random() * 3)+ 1;
		  if(c === 1)
		  {
		  	document.getElementById("container").innerHTML='<input type="image" src="play/rsz_weapon1.png" ontouchstart="attack_back()"  id="weapon1" >';
			}
		  else if (c === 2)
		  {

		  	document.getElementById("container").innerHTML='<input type="image" src="play/rsz_weapon2.png" ontouchstart="attack_stop()"  id="weapon1" >';
		  }
		  else
		  {
		  	document.getElementById("container").innerHTML='<input type="image" src="play/rsz_weapon3.png" ontouchstart="attack_turn()"  id="weapon1"  >';
		  }
	}
    window.oncontextmenu = function(event) {
     event.preventDefault();
     event.stopPropagation();
     return false;
};

window.onload=change


slotitem = new Array('1','2','3');


weapon= new Array('attack_stop()','attack_turn()','attack_back()');

function spim(){

	b=0;
	spinem();

};

function spinem() {

turns1=10+Math.floor((Math.random() * 10))

for (a=0;a<turns1;a++)

	{ document.getElementById("container").innerHTML='<input type="image"  src="play/rsz_weapon' + slotitem[a % 3]+'.png"  ontouchstart="'+weapon[a % 3]+'"  id="weapon1"  >';} 


b++;

if (b<25) {setTimeout("spinem(b);",50);} 

}

