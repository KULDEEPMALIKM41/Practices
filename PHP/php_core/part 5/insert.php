<?php
$name=$_POST['name'];
$standard=$_POST['standard'];
$address=$_POST['address'];

$con=mysqli_connect('localhost','root','','php');

$query="insert into student VALUES(NULL,'$name','$standard','$address')";

$run=mysqli_query($con,$query);

if ($run)
{
	echo "<script>alert('Data save successfully')</script>";
	echo "<script>location='index.php'</script>";
}
else
{
	echo"Error!!";
}
?>