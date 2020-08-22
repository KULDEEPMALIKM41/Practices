<?php

if(isset($_COOKIE['uname']))
{

echo $_COOKIE["uname"];

}
else
{
	echo"<script>alert('you are not login')</script>";
	echo"<script>window.location='cookeis.php'</script>";
}
?>

</h1>
<h2>
<a href='Logout2.php' style='float:right;' >Logout2</a>
</h2>