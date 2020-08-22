<?php
class Weakstudent
{
	private $wkstudentname;
	
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
	private $Student;
	
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
		$this->getWkName($this->Student); //if we want that this class variable value give parents class  protected variable.
		
	}
	
}
$obj1=new Student;
$obj1-> getWkName('Ashish');
$obj1-> showWKName();

$obj1-> getStname('kuldeep');
$obj1->showName();

$obj1->call();
$obj1-> showWKName();
$obj1->showName();

echo "<pre>";
print_r ($obj1);
echo "</pre>";
?>