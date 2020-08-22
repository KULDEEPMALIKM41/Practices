<?php
include('header.php');

$con= mysqli_connect('localhost','root','','php');

$query="select * from student";

$run=mysqli_query($con,$query);
?>
<table align='center' border='1'>
<tr>
<th>Roll No</th>
<th>Name</th>
<th>Standard</th>
<th>Address</th>
</tr>

<?php

if($run)
{
	while($data=mysqli_fetch_assoc($run))
	{
		?>
		<tr>
			<td align='center'><?php echo $data['Roll_No']?></td>
			<td align='center'><?php echo $data['S_Name']?></td>
			<td align='center'><?php echo $data['Standard']?></td>
			<td align='center'><?php echo $data['Address']?></td>
		</tr>
		
		<?php
	}
}

include('header.php');
?>