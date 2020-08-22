<?php

class Dad
{
	public function Car()
	{
		echo "Dad Car<br>";
	}	
}
class Son extends Dad
{
	public function Car()
	{
		echo "My New Car<br>";
	}
	public function dadCar()
	{
		//Dad::Car();	//or
		
		parent::Car();
	}
}

$Obj=new Son;
$Obj->Car();
$Obj->dadCar();





?>