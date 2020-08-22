<?php

$arrx=array(10,20,30,40,array(42,44,46,48),50);
foreach($arrx as $ky => $vl)
{
	if( is_array($vl))
	{
		foreach($vl as $k=>$v)
		{
			echo "$ky . $k => $v<br>";
		}
	}

	else
	{		
		echo $ky."=>".$vl."<br>";
	}
}


?>