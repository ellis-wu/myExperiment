<?php
echo gethostname().'<br/>';

$index = rand(1, 10);
echo 'Random : '.$index.'<br/>';
$load = 'Medium';
$A = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef";
if ($index < 3) {
  if (rand(1, 2) == 1) {
    $load = 'Low';
    $A = "0123456789abcdef0123456789abcdef";
  } else {
    $load = 'High';
    $A = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef";
  }
} else {
  $load = 'Medium';
}

echo 'Load : '.$load.'<br/>';


$B = $A.$A.$A.$A.$A.$A;
$C = $B.$B.$B.$B.$B.$B;
$D = $C.$C.$C.$C.$C.$C;
$E = $D.$D.$D.$D.$D.$D;
$F = $E.$E.$E.$E.$E.$E;
$G = $F.$F.$F.$F.$F.$F;
$H = $G.$G.$G.$G.$G.$G;

echo 'Status : test OK!'.'<br/>';
echo 'Mem(MB) : '.memory_get_usage()/1024/1024;

?>
