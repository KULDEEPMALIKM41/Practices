<h1><?php

	echo "website host server name is : ".$_SERVER['HTTP_HOST']."<br><br>";
	
	echo "you are using browser & system is : ".$_SERVER['HTTP_USER_AGENT']."<br><br>";

	echo "website host server name is : ".$_SERVER['SERVER_NAME']."<br><br>";
	
	echo "your IP address is : ".$_SERVER['REMOTE_ADDR']."<br><br>";
	
	echo "server port  is : ".$_SERVER['SERVER_PORT']."<br><br>";
	
	function filepath()
	{
		return $_SERVER['PHP_SELF'];
	}


?></h1>


<HTML>
<HEAD></HEAD>
<BODY>
<h1>
<?php  
 echo "PHP file path is : ".filepath()."<br><br>";
 echo "nice";	
 ?>
</h1>
</BODY>
</HTML>