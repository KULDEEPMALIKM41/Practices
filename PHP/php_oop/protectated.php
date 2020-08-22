<?php
class Weakstudent
{
	protected $wkstudentnm='kuldeep';
	
	function showDatawk()
	{
		echo $this->wkstudentnm;
	}
}
$obj1=new Weakstudent;
//echo $obj1->wkstudentnm;// Cannot access protected property.
$obj1->showDatawk();





?>