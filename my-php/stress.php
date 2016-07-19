<?php
echo gethostname().'<br/>';
echo 'test OK!'.'<br/>';
$A = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef";
$B = $A.$A.$A.$A.$A.$A;
$C = $B.$B.$B.$B.$B.$B;
$D = $C.$C.$C.$C.$C.$C;
$E = $D.$D.$D.$D.$D.$D;
$F = $E.$E.$E.$E.$E.$E;
$G = $F.$F.$F.$F.$F.$F;
$H = $G.$G.$G.$G.$G.$G;
echo memory_get_usage()/1024/1024;
?>
