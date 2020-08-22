<?php
	
	$fname="kuldeep";
	$lname="mali";
	
	function exa1()
	{
		global $fname;
		echo $fname;
	}
	
	function exa2()
	{
		echo $GLOBALS["fname"]." ".$GLOBALS["lname"];
	}

?>

<html>
<head>
<title>global variable</title>
</head>
<body>
<h1><?php  
 
		exa1();
		
		echo"<br>";
		
		exa2();

?></h1>
</body>
</html>