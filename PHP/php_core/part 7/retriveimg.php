<html>
<head>
<title>Retrive Img</title>
<head>
<body>
<table align='center' border='1' width='500'>
<tr>
<th>ID</th>
<th>Image Name</th>
<th>Image</th>
</tr>
<?php
$con=mysqli_connect('localhost','root','','php');

$query="select * from images";

$run=mysqli_query($con,$query);

if($run)
{
	while($data=mysqli_fetch_assoc($run))
	{
?>
<tr>
<td align='center'><?php echo $data['id'];?></td>
<td align='center'><?php echo $data['imgname'];?></td>
<td align='center'><img src="images/<?php echo $data['imgname'];?>" height="150" ></td>
</tr>
<?php		
	}
	
}




?>



</table>
</body>
</html>