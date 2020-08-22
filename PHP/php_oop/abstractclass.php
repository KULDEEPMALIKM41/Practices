<?php
abstract class genaral
{
	abstract public function getData();
	
	public function attendans()
	{
		echo"Function for teacher and student both attendans<br>";
	}
}

class teacher extends genaral
{
	public function getData()
	{
		echo "this function for teachers get data<br>";
	}
}

class student extends genaral
{
	public function getData()
	{
		echo "this function for students get data<br>";
	}
}
$obj1=new teacher();
$obj1->attendans();
$obj1->getData();

$obj2=new student();
$obj2->attendans();
$obj2->getData();






?>