<?php

	function sum($x,$y)
	{

		$c=$x+$y;
		return $c;
	}
	$a=20;
	$b=30;
	$res=sum($a,$b);
	
?>

<html>
<head>
<title>Functions</title>
</head>
<body>
<h1><?php
echo "Addition is : ".$res;
?></h1>
</body>
</html>