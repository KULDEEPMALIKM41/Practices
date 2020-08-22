<?php 
class Student
{
	public $stu_name;
	
	function getData($name)
	{
		$this->stu_name=$name;
	}
	function showData()
	{
		echo $this->stu_name;
	}
}

$object1= new Student;
$object2= new Student;
$object1->stu_name='kuldeep';
$object1->showData();

?>