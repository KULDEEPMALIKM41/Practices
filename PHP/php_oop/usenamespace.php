<?php
use govt_teacher\profile\addstudent as gtp;
use govt_teacher\profile\viewstudent;
include'testnamespace.php';

echo'<br><br>extarnal obj<br>';
$obj1=new gtp;
$obj2=new viewstudent();
$obj3=new prive_teacher\profile\addstudent();
$obj4=new prive_teacher\profile\viewstudent();


?>