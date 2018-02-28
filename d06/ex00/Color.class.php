<?php

class Color() {
	
	public $verbose = false;
	public $red = 
	public $green =
	public $blue = 
	
	public function  __construct(array[either rgb or red, green, blue]) {
		if rgb {
			split into red green blue
		}
		$this->red = $red;
		$this->green = $green;
		$this->blue = $blue;


	convert any of these values into an integer before using
	}

	public function __toString(something) {
		return "Color( red: " . $this->red . ", green: " . $this->green . ", blue: " . $this->blue . " ) /*constructed or destrurcted?*/";
	}

	public static function doc() {
		returns documentation from ('Color.doc.txt', 'r');
	}

	add( Color $rhs ) - adds each color component, return new instance 

	sub( Color $rhs ) - subtracts color component, return new instance

	mult ( $f ); - multiplies color components, returns new instance
	if verbose is true, then constructor or destructor will produce output. 
}


?>
