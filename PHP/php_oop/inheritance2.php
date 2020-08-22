<?php

class A
{
	public $name='kuldeep';
	public $roll=105;
	
	public function aFun()
	{
		echo"I am the function of A class<br>";
	}
	
	final public function bFun()
	{
		echo"I am the function of A class<br>";
	}
}

class B extends A
{
	public function bFun()
	{
		echo"I am the function of B class<br>";
	}
}
?>