<?php

$a='kuldeepmalikm41@gmail.com';
$b='gopalmaligmailcom';
$c='127.0.0.1';
$d='48.58';
$e=5;
$f=10.50;
$g="12";
$h=15;

$range=array();
$range['options']=array('min_range'=> 0,'max_range'=>14);

if (filter_var($a,FILTER_VALIDATE_EMAIL))
{
	echo"($a) is valid email id<br><br>";
}
else
{
	echo"($a) is not valid email id<br><br>";
}




if (filter_var($b,FILTER_VALIDATE_EMAIL))
{
	echo"($b) is valid email id<br><br>";
}
else
{
	echo"($b) is not valid email id<br><br>";
}






if (filter_var($c,FILTER_VALIDATE_IP))
{
	echo"$c is valid IP address<br><br>";
}
else
{
	echo"$c is not valid IP address<br><br>";
}






if (filter_var($d,FILTER_VALIDATE_IP))
{
	echo"$d is valid IP address<br><br>";
}
else
{
	echo"$d is not valid IP address<br><br>";
}





if(filter_var($b,FILTER_VALIDATE_INT))
{
	echo"$b is INTGER<br><br>";
}
else
{
	echo"$b is not INTGER<br><br>";
}









if(filter_var($d,FILTER_VALIDATE_INT))
{
	echo"$d is INTGER<br><br>";
}
else
{
	echo"$d is not INTGER<br><br>";
}




if(filter_var($e,FILTER_VALIDATE_INT,$range))
{
	echo"$e is INTGER<br><br>";
}
else
{
	echo"$e is not INTGER<br><br>";
}





if(filter_var($f,FILTER_VALIDATE_INT))
{
	echo"$f is INTGER<br><br>";
}
else
{
	echo"$f is not INTGER<br><br>";
}






if(filter_var($g,FILTER_VALIDATE_INT,$range))
{
	echo"$g is INTGER<br><br>";
}
else
{
	echo"$g is not INTGER<br><br>";
}


if(filter_var($h,FILTER_VALIDATE_INT,$range))
{
	echo"$h is INTGER<br><br>";
}
else
{
	echo"$h is not INTGER<br><br>";
}








if(filter_var($c,FILTER_VALIDATE_FLOAT))
{
	echo"$c is FLOAT<br><br>";
}
else
{
	echo"$c is not FLOAT<br><br>";
}


if(filter_var($d,FILTER_VALIDATE_FLOAT))
{
	echo"$d is FLOAT<br><br>";
}
else
{
	echo"$d is not FLOAT<br><br>";
}




if(filter_var($e,FILTER_VALIDATE_FLOAT))
{
	echo"$e is FLOAT<br><br>";
}
else
{
	echo"$e is not FLOAT<br><br>";
}





if(filter_var($f,FILTER_VALIDATE_FLOAT))
{
	echo"$f is FLOAT<br><br>";
}
else
{
	echo"$f is not FLOAT<br><br>";
}






if(filter_var($g,FILTER_VALIDATE_FLOAT))
{
	echo"$g is FLOAT<br><br>";
}
else
{
	echo"$g is not FLOAT<br><br>";
}








if(filter_var(true,FILTER_VALIDATE_BOOLEAN))
{
	echo"true is BOOLEAN<br><br>";
}
else
{
	echo"true is not BOOLEAN<br><br>";
}




if(filter_var($d,FILTER_VALIDATE_BOOLEAN))
{
	echo"$d is BOOLEAN<br><br>";
}
else
{
	echo"$d is not BOOLEAN<br><br>";
}



?>