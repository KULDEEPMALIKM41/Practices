<?php

class Addition
{
	public function __construct()
	{
		echo "Function Overloading<br>";
	}
	
	public function __call($fname,$argument)
	{
		if ("Add"==$fname)
		{
			$this->x=0;
			foreach ($argument as $v)
			{
				$this->x=$this->x+$v;
			}
			echo $this->x."<br>";
		}
		else
		{
			echo "This function is on define<br>";
		}
	}
	
	
}

$obj=new Addition();
$obj->Add(10,20);
$obj->Add(10,20,30);
$obj->Add(10,20,30,40);
$obj->Add(10,20,30,40,50);
echo"<pre>";
print_r($obj);
echo"</pre>";
?>