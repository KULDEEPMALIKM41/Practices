<?php

class Parents
{
	public $name='kuldeep';
	public $roll=105;
	
	public function parentsFun()
	{
		echo"I am the function of parents class<br>";
	}
}
class Child extends Parents
{
	public function childFun()
	{
		echo"I am the function of child class<br>";
	}
}
$obj1=new Child;
$obj1->childFun();
$obj1->parentsFun();
echo $obj1->name."<br>";
echo $obj1->roll."<br>";



?>