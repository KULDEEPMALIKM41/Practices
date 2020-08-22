
<?php

$s=$_REQUEST['submit']; //we are use $_REQUEST in place of $_POST and $_GET. 
						//$_REQUEST any type of method data fetch.

if ($s<>null)
{
echo 'your Login Id is : '.$_REQUEST['id']."<br>";
echo 'your Password is : '.$_POST['password']."<br>";
echo "your Image is : <img src='".$_POST['img']."'height='100'><br>";
}




?>









<html>
<head>
<title>Example of post</title>
</head>
<body>

<form action="" method="post">

<table align="center" border="1">
<tr>
<td>Login Id</td>
<td><input type="text" name="id"></td>
<tr>

<tr>
<td>Password</td>
<td><input type="password" name="password"></td>
<tr>

<tr>
<td>Upload Image</td>
<td><input type="file" name="img"></td>
<tr>

<tr>
<td colspan="2" align="center"><input type="submit" name="submit" value="submit"></td>
<tr>

</table>



</form>



</body>
</html>