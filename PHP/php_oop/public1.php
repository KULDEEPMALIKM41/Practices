<?php
class Weakstudent
{
	public $wkstudentnm;
	public $wkstudentfnm;
}
class student extends Weakstudent
{
	public $contact;
		
	function showData()
	{
		echo $this->wkstudentnm."<br>";
		echo $this->wkstudentfnm."<br>";
		echo $this->contact."<br>";
	}
}
$obj1=new student;
$obj1->wkstudentnm='kuldeep';
$obj1->wkstudentfnm='shiv';
$obj1->contact='8890834462';


echo $obj1->wkstudentnm."<br>";
echo $obj1->wkstudentfnm."<br>";
echo $obj1->contact."<br>";


$obj1->showData();


echo "<pre>";
print_r ($obj1);
echo "</pre>";
?>