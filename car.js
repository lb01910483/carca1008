
	
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
		document.getElementById("container").innerHTML='';
		setTimeout("spim();",10000);
	}
	function attack_stop() {
		webiopi().callMacro("attack_stop");
		document.getElementById("container").innerHTML='';
		setTimeout("spim();",10000);
	}
	function attack_turn() {
		webiopi().callMacro("attack_turn");
		document.getElementById("container").innerHTML='';
		setTimeout("spim();",10000);
	}		
	function change(){
		  var c=Math.floor(Math.random() * 3)+ 1;
		  if(c === 1)
		  {
		  	document.getElementById("container").innerHTML='<input type="image" src="play/test_1.svg"  ontouchstart="attack_stop()"  id="weapon1" >';
			}
		  else if (c === 2)
		  {

		  	document.getElementById("container").innerHTML='<input type="image" src="play/test_2.svg"   ontouchstart="attack_turn()"  id="weapon1" >';
		  }
		  else
		  {
		  	document.getElementById("container").innerHTML='<input type="image" src="play/test_3.svg"  ontouchstart="attack_back()"  id="weapon1"  >';
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

	{ document.getElementById("container").innerHTML='<input type="image"  src="play/test_' + slotitem[a % 3]+'.svg"   ontouchstart="'+weapon[a % 3]+'"  id="weapon1"  >';} 


b++;

if (b<5) {setTimeout("spinem(b);",100);} 

}
