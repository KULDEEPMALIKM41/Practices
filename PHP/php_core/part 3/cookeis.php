<?php
if (isset($_COOKIE['uname']))
{
	echo"<script>alert('you are already login!')</script>";

	echo"<script>window.location='test2.php'</script>";
	exit();
}
?>
<html>
<head>
<title>Example of session</title>
</head>
<body>
<form action="" method="post">
<table align=center>
<tr>
<td>Username : </td>
<td><input type="text" name="uname"></td>
</tr>

<tr>
<td>Password : </td>
<td><input type="password" name="pas"></td>
</tr>

<tr>
<td colspan="2" align="center"><input type="submit" name="submit" value="submit"></td>
</tr>

</table>
</form>
</body>
</html>

<?php
if(isset($_POST['submit']))
{
setcookie("uname",$_POST['uname'],time()+86400);

header("location:test2.php");
}
?>