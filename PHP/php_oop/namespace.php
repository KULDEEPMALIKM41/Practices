<?php
namespace test
{
	class teacher
	{
		public function __construct()
		{
			echo'teacher class from test namespace<br> ';
		}
	}	
	class student
	{
		public function __construct()
		{
			echo'student class from test namespace<br> ';
		}
	}
	$obj1=new teacher(); //create object in local namespace.
	$obj2=new student();
	
}
namespace
{
	$obj1=new test\teacher();
	$obj2=new test\student(); //create object in global namespace.
}



?>