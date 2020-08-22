<?php

class A
{
	public $name='kuldeep';
	public $roll=105;
	
	public function aFun()
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

class C extends A
{
	public function cFun()
	{
		echo"I am the function of C class<br>";
	}
}
$obj1=new B;
$obj1->bFun();
$obj1->aFun();
echo $obj1->name."<br>";
echo $obj1->roll."<br>";

$obj2=new C;
$obj2->cFun();
$obj2->afun();
echo $obj2->name."<br>";
echo $obj2->roll."<br>";




?>