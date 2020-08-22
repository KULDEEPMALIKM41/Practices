<?php
class Weakstudent
{
	protected $wkstudentnm='kuldeep';
	protected $wkstudentfnm='shiv';
}
class student extends Weakstudent
{
	protected $contact='8890834462';
		
	function showData()
	{
		echo $this->wkstudentnm;
		echo $this->wkstudentfnm;
		echo $this->contact;
	}
}
$obj1=new student;
$obj1->showData();
?>