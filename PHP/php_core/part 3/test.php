<h1 align='center'><?php

session_start();
if(isset($_SESSION['name']))
{
	echo "Welcome : ".$_SESSION['name'];
}
else
{
	echo"<script>alert('You are not login')</script><script>window.location='session.php'</script>";
}

?>
</h1>
<h2>
<a href='Logout.php' style='float:right;' >Logout</a>
</h2>