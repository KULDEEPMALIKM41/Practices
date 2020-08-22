<?php

class A
{
	public $name='kuldeep';
	public $roll=105;
	
	public function aFun()
	{
		echo"I am the function of A class<br>";
	}
	
		public function Fun()
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
	
		public function Fun()
	{
		echo"I am the function of B class<br>";
	}
}

class C extends B
{
	public function cFun()
	{
		echo"I am the function of C class<br>";
	}
	
		public function Fun()
	{
		echo"I am the function of C class<br>";
	}
	
	public function call()
	{
		self::Fun();
		parent::Fun();
		A::Fun();
	}
}

$obj1=new C;
$obj1->cFun();
$obj1->bFun();
$obj1->aFun();
echo "<br><br><br>";


$obj1->call();


echo "<br><br><br>";
$obj1=new B;
$obj1->aFun();

$obj1->bFun();
$obj1->cFun();


?>
