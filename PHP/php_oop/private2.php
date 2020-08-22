<?php
class Student
{
	private $stu_name;
	
	function getname($name)
	{
		$this->stu_name=$name;
	}
	
	function showname()
	{
		echo $this->stu_name;
	}
}
$obj1=new Student;
//$obj1->stu_name='kuldeep';  //not access private property.
$obj1->getname('kuldeep');
$obj1->showname();

?>