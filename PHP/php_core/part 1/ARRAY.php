<?php
 
	echo "<h1>example of ARRY in php</h1>";
	
	$student_name=array("kuldeep","sanjay","name"=>"prakash","bharat");
	
	echo $student_name["name"];
	
	echo "<br><br>";
	
	echo $student_name[0];
	
	echo "<br><br>";
	
	echo $student_name[1];
	
	echo "<br><br>";
	
	echo $student_name[2];
	
	echo "<br><br>";
	
	
	$student_fname=array();
	
	$student_fname[0]="kuldeep";
	
	$student_fname[1]="sanjay";
	
	$student_fname["name"]="prakash";
	
	$student_fname[2]="bharat";
	
	var_dump($student_fname);
	
	echo "<br><br>";
	
	echo $student_name["name"];
	
	echo "<br><br>";
	
	echo $student_name[0];
	
	echo "<br><br>";
	
	echo $student_name[1];
	
	echo "<br><br>";
	
	echo $student_name[2];
	
?>