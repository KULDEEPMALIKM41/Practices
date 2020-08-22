<html>
<head>
<title>Image Upload</title>
</head>
<body>
<form action='' method='post' enctype='multipart/form-data'>
<table align='center' border='1'>
<tr>
<td><input type='file' name='img'></td>
<td><input type='submit' name='submit' value='submit'></td>
</tr>
</body>
</html>





<?php
if(isset($_POST['submit']))
{
	
	$img = $_FILES['img']['name'];

	$temp_name=$_FILES['img']['tmp_name'];
	
	$con=mysqli_connect('localhost','root','','php');
	
	$query="insert into images values(NULL,'$img')";
	
	$run=mysqli_query($con,$query);
	
	if($run)
	{
		move_uploaded_file($temp_name,"images/$img");
		echo "<script>alert('Upload Success')</script>";	
	}
	else
	{
		echo "Error!!";
	}
}	
	
?>