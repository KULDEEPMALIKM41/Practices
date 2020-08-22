

<html>
<head>
<title>Example of $file</title>
<head>

<body>

<form action="" method="post" enctype="multipart/form-data">

<table align="center" border="1">

<tr>
<th colspan="2"> Upload your file</th>
</tr>

<tr>
<td> Upload file</td>
<td><input type="file" name="img"<td>
</tr>

<tr>
<td colspan="2" align="center"> <input type="submit" name="submit" value="submit"></td>
</tr>


</table>



</form>

<pre>
<?php

$s=$_REQUEST['submit'];
if($s<>null)
{
	print_r($_FILES['img']['name']);
}

?>
</pre>
</body>


</html>