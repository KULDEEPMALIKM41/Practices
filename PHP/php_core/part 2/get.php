<?php
$s=$_GET['submit']; //we are use $_REQUEST in place of $_POST and $_GET. 
						//$_REQUEST any type of method data fetch.

if($s<>Null)
{
	echo "<h1>your name is ".$_GET['name']."<br>";
	echo "your address is ".$_REQUEST['address']."<br>";
	echo "your gender is ".$_REQUEST['gender']."<br></h1>";
}


else
{
echo "<h1><center>Enter Information<center></h1>";

}


?>



<html>
<head>
<title>Example of get method</title>
</head>
<body>
<form action="" method="get">

<table align="center" border="1" width="500">

<tr>
<td>Name : </td>
<td><input type="text" name="name" size="70"></td>
</tr>

<tr>
<td>Address : </td>
<td><textarea rows="3" cols="53" name="address"></textarea></td>
</tr>

<tr>
<td>Gender : </td>
<td>Male<input type="radio" value="Male" name="gender"> Female<input type="radio" value="Female" name="gender"></td>
</tr>

<tr>
<td align="center" colspan="2"><input type="submit" name="submit" value="submit"></td>
</tr>

</table>

</form>
</body>
</html>
