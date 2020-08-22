<?php
class Weakstudent
{
	public $wkstudentnm;
	
	function showDatawk()
	{
		echo $this->wkstudentnm;
	}
}
$obj1=new Weakstudent;
$obj1->wkstudentnm='kuldeep';
echo $obj1->wkstudentnm."<br>";
$obj1->showDatawk();





?>