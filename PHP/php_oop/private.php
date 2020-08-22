<?php
class Student
{
	private $roll=101;
	private $stu_name='kuldeep';
	private $f_name='shiv';
	
	function showData()
	{
		echo $this->roll."<br>";
		echo $this->stu_name."<br>";
		echo $this->f_name."<br>";
	}
}

$obj1=new Student;
$obj1->showData();
//echo $obj1->roll;
//echo $obj1->stu_name;			//not Access private Member.
//echo $obj1->f_name;




?>