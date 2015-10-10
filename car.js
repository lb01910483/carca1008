
	
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
	}
	function attack_stop() {
		webiopi().callMacro("attack_stop");
	}
	function attack_turn() {
		webiopi().callMacro("attack_turn");
	}		

    window.oncontextmenu = function(event) {
     event.preventDefault();
     event.stopPropagation();
     return false;
};