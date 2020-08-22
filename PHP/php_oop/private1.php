<?php
class Student
{
	private $roll=101;
	private $stu_name='kuldeep';
	private $f_name='shiv';
		
}
class Weakstudent extends Student
{
	private $contact='8890834430';
	
	function showData()
	{
		//echo $this->roll;
		//echo $this->stu_name;   //private member is not access in another class.
		//echo $this->f_name;
		echo $this->contact;
	}
}

$obj1=new Weakstudent;
$obj1->showData();


?>