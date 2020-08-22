<?php

class parents
{
	private $name;
	public function __construct($value)
	{
		$this->name=$value;
	}
	
	public function showData()
	{
		echo "this class is parents"." ".$this->name."<br>";
	}
}

class child extends parents
{
	private $name1;
	public function __construct($value1)
	{
		$this->name1=$value1;	
		parent::__construct("$this->name1");
	}
	
	public function showData1()
	{
		echo "this class is child ".$this->name1."<br>";
	}
}
$obj=new child('kuldeep');

$obj->showData1();

$obj->showData();







?>