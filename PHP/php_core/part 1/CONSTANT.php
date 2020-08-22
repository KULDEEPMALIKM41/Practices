
<?php
define("CONSTANT", "Hello world.",TRUE);
echo CONSTANT.'<BR>'; // outputs "Hello world."
echo Constant.'<BR>'; // outputs "Constant" and issues a notice.


const A = 'Hello World';
echo A.'<BR>';


//Magic constants

echo __LINE__ .'<BR>';

echo __FILE__ .'<BR>';

echo __DIR__ .'<BR>';

echo __FUNCTION__ .'<BR>';

echo __CLASS__ .'<BR>';

echo __METHOD__ .'<BR>';

echo __TRAIT__ .'<BR>';

echo __NAMESPACE__ .'<BR>';

?>


