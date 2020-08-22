<?php
class student
{
	private $name,$roll;
	function getData($name,$roll)
	{
		$this->sname=$name;
		$this->roll=$roll;
	}
	
	function showData()
	{
		echo "Roll No is : ".$this->roll." And Name is : ".$this->sname;
	}
}
$student1=new student();
$student1->getData("kuldeep",101);
$student1->showData();





?>