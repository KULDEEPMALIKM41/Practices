<?php 
class Student
{
	
	
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
$object1->getData('kuldeep');
$object1->showData();

?>