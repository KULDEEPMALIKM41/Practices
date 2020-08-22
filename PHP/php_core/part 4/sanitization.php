<?php
$a='kuldeepmalikm41@gmail.com';
$b='kul     dee    --p@_  com';
$c='(kuldeep@gmailcom)';
$d="123!@#$%^&*((_+.+-:<>?''";
$e="k1u2l3d4e5@123.52";
$f='this is sanitizing lession';
$x=filter_var($a,FILTER_SANITIZE_EMAIL);
echo "sanitize email is : $x<br><br>";
if (filter_var($x,FILTER_VALIDATE_EMAIL))
{
	echo "$a IS VALID EMAIL<br><br>";
}
else
{
	echo "$a IS NOT VALID EMAIL<br><br>";
}


$y=filter_var($b,FILTER_SANITIZE_EMAIL);
echo "sanitize email is : $y<br><br>";
if (filter_var($y,FILTER_VALIDATE_EMAIL))
{
	echo "$b IS VALID EMAIL<br><br>";
}
else
{
	echo "$b IS NOT VALID EMAIL<br><br>";
}


$z=filter_var($c,FILTER_SANITIZE_EMAIL);
echo "sanitize email is : $z<br><br>";
if (filter_var($z,FILTER_VALIDATE_EMAIL))
{
	echo "$c IS VALID EMAIL<br><br>";
}
else
{
	echo "$c IS NOT VALID EMAIL<br><br>";
}


$sd=filter_var($d,FILTER_SANITIZE_STRING);
echo " STRING sanitize $d is : $sd<br><br>";

$sd=filter_var($d,FILTER_SANITIZE_NUMBER_INT);
echo "NUMBER_INT sanitize $d is : $sd<br><br>";

$sd=filter_var($d,FILTER_SANITIZE_NUMBER_FLOAT);
echo "NUMBER_FLOAT sanitize $d is : $sd<br><br>";

$sd=filter_var($d,FILTER_SANITIZE_SPECIAL_CHARS);
echo " SPECIAL_CHARS sanitize $d is : $sd<br><br>";



$se=filter_var($e,FILTER_SANITIZE_STRING);
echo "STRING sanitize $e is : $se<br><br>";

$se=filter_var($e,FILTER_SANITIZE_NUMBER_INT);
echo "NUMBER_INT sanitize $e is : $se<br><br>";

$se=filter_var($e,FILTER_SANITIZE_NUMBER_FLOAT);
echo "NUMBER_FLOAT sanitize $e is : $se<br><br>";

$se=filter_var($e,FILTER_SANITIZE_SPECIAL_CHARS);
echo "SPECIAL_CHARS sanitize $e is : $se<br><br>";

$sf=filter_var($f,FILTER_SANITIZE_ENCODED);
echo "NUMBER_FLOAT sanitize $f is : $sf<br><br>";


?>