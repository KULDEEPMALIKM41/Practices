<?php
$http_client_ip=$_SERVER['HTTP_CLIENT_IP'];
$http_forwarded_for=$_SERVER['HTTP_FORWARDED_FOR'];
$http_addr=$_SERVER['REMOTE_ADDR'];

if(!empty($http_client_ip))
{
	echo "IP is ".$http_client_ip;
}
else if(!empty($http_forwarded_for))
{
	echo "IP is ".$http_forwarded_for;
}
else if(!empty($http_addr))
{
	echo "IP is ".$http_addr;
}




?>