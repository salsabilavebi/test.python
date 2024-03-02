<?php

function sequenceExists($main, $seq) {
    $mainLength = count($main);
    $seqLength = count($seq);

    if ($seqLength > $mainLength) {
        return false;
    }

    for ($i = 0; $i <= $mainLength - $seqLength; $i++) {
        $found = true;
       
        for ($j = 0; $j < $seqLength; $j++) {
            if ($main[$i + $j] != $seq[$j]) {
                $found = false;
                break;
            }
        }
        
        if ($found) {
            return true;
        }
    }
    
    return false;
}

$main = array(20, 7, 8, 10, 2, 5, 6);
$seq1 = array(7, 8);
$seq2 = array(8, 7);
$seq3 = array(7, 10);

echo sequenceExists($main, $seq1) ? 'true' : 'false'; 
echo "\n";
echo sequenceExists($main, $seq2) ? 'true' : 'false'; 
echo "\n";
echo sequenceExists($main, $seq3) ? 'true' : 'false'; 
?>
