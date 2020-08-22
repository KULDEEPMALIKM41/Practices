<?php
class Weakstudent
{
	protected $wkstudentname;
	
	function getWkName($name)
	{
		$this->wkstudentname=$name;
	}
	
	function showWKName()
	{
		echo $this->wkstudentname."<br>";
	}
}
class Student extends Weakstudent
{
	protected $Student;
	
	function getStname($name)
	{
		$this->Student=$name;
	}
	
	function showName()
	{
		echo $this->Student."<br>";
	}
	
	function call()
	{
		$this->wkstudentname=$this->Student; //if we want that this class variable value give parents class  protected variable.
	}
	
}

class extra extends Student
{
	function test()
	{
	echo $this->wkstudentname;
	echo $this->Student;
	}
}
$obj1=new extra;
$obj1-> getWkName('Ashish');
$obj1-> showWKName();

$obj1-> getStname('jamura');
$obj1->showName();

$obj1->call();
$obj1-> showWKName();
$obj1->showName();

echo "<pre>";
print_r ($obj1);
echo "</pre>";
$obj1->test();

?>