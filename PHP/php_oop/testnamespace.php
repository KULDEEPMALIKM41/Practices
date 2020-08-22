<?php
namespace govt_teacher\profile
{
	class addstudent
	{
		public function __construct()
		{
			echo"class addstudent from govt_teacher\profile namespace<br>";
		}
	}
	class viewstudent
	{
		public function __construct()
		{
			echo"class viewstudent from govt_teacher\profile namespace<br>";
		}
	}
}
namespace prive_teacher\profile
{
	class addstudent
	{
		public function __construct()
		{
			echo"class addstudent from prive_teacher\profile namespace<br>";
		}
	}
	class viewstudent
	{
		public function __construct()
		{
			echo"class viewstudent from prive_teacher\profile namespace<br>";
		}
	}
}

namespace{
	echo'internal obj<br>';
	$obj1=new govt_teacher\profile\addstudent();
	$obj2=new govt_teacher\profile\viewstudent();
	$obj3=new prive_teacher\profile\addstudent();
	$obj4=new prive_teacher\profile\viewstudent();
}



?>