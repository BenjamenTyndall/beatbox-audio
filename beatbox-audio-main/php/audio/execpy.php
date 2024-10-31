<?php
ob_start();
ini_set('display_errors', 1);
error_reporting(E_ALL);

//$file = '/var/www/html/audiofiles/' . 'deadly-kick-gloomy-kick.wav';
$file = '/var/www/html/audiofiles/' . $_GET['filename'];
$extension = $_GET['type'];
$filen = $_GET['filename'];
$mic = $_GET['mic'];
$style = $_GET['style'];
        putenv("/usr/bin/ffmpeg");
        $scriptPath = '/var/www/html/mainscript.py';
        $arg1 = escapeshellarg($file);
        $arg2 = escapeshellarg($mic);
        $arg3 = escapeshellarg($style);
        $command = 'python ' . escapeshellarg($scriptPath) . ' ' . $arg1 . ' ' . $arg2 . ' ' . $arg3 . ' ' . "2>&1";
        $handle = popen($command, 'r');
        if($handle){
        while(($output = fgets($handle)) !== false){
	echo $output;
}
	pclose($handle);
	sleep(15);
//	if(file_exists($file. '--processed.wav')){
	header("Location: downloadmix.php?filename=$filen&type=$extension");
	ob_end_flush();
// }
}else{
	echo "error executing";
}

?>
