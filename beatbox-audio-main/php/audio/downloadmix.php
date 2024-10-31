<?php

$file = '/var/www/html/audiofiles/' . $_GET['filename'];
$extension = $_GET['type'];
$wavfile ='/var/www/html/audiofiles/' . pathinfo(basename($file), PATHINFO_FILENAME). '.wav';
$base = '/var/www/html/audiofiles/' . pathinfo(basename($file), PATHINFO_FILENAME). '--processed.wav';
$etc = '/var/www/html/audiofiles/' . pathinfo(basename($file), PATHINFO_FILENAME). '--Normalised.wav';
$downloadas = pathinfo(str_replace("__"," ",$_GET['filename']), PATHINFO_FILENAME). '--processed.wav';

if ($extension === 'mov' || $extension === 'mp4') {
    $mp4file = '/var/www/html/audiofiles/' . pathinfo(basename($file), PATHINFO_FILENAME). '.mp4';
    $base = '/var/www/html/audiofiles/' . pathinfo(basename($file), PATHINFO_FILENAME). '--processed.mp4';
    $etc = '/var/www/html/audiofiles/' . pathinfo(basename($file), PATHINFO_FILENAME). '--Normalised.mp4';
$downloadas = pathinfo(str_replace("__"," ",$_GET['filename']), PATHINFO_FILENAME). '--processed.mp4';
    

if (file_exists($base)) {

    // Set headers for file download
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
    //$mixname = $_GET['filename'] . "--Processed.wav";

    //header('Content-Disposition: attachment; filename="'. $mixname .'"');
    header('Content-Disposition: attachment; filename="' . $downloadas  .'"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($base));

    // Output file content
    readfile($base);
    sleep(2);
    if (unlink($base) && unlink($etc) && unlink($file) && unlink($wavfile)) {
        echo "Deleted";
        header("Location: mix.php");
        // code...
    }
    // Output success message
    echo "File downloaded successfully.";

} else {
    // If file does not exist, output error message
    $red = "Error: File not found. Please ensure file names do not include special characters such as '.', '@', '$', '^', '()' ";
    $timer = 5;
    while ($timer > 0) {
        sleep(1);
        $timer--;
        // code...
    }
    if ($timer === 0){
    //header("Location: mix.php");
}
}


}else{

if (file_exists($base)) {

    // Set headers for file download
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
	//$mixname = $_GET['filename'] . "--Processed.wav";

	//header('Content-Disposition: attachment; filename="'. $mixname .'"');
    header('Content-Disposition: attachment; filename="' . $downloadas  .'"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($base));

    // Output file content
    readfile($base);
    sleep(2);
    if (unlink($base) && unlink($etc) && unlink($file) && unlink($wavfile)) {
        echo "Deleted";
        header("Location: mix.php");
        // code...
    }
    // Output success message
    echo "File downloaded successfully.";

} else {
    // If file does not exist, output error message
    $red = "Error: File not found. Please ensure file names do not include special characters such as '.', '@', '$', '^', '()' ";
    $timer = 5;
    while ($timer > 0) {
        sleep(1);
        $timer--;
        // code...
    }
    if ($timer === 0){
    //header("Location: mix.php");
}
}
}
?>

<html>
<head>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body class="back darkvc ">
    <div class="">
<h1 class="white mid">Information: <?php echo $red;?></h1>
<br>
    <button class="white mid btn girthbtn logobutton btn btn-primary vcpurpleBG smallPadding marginside purp " onclick="<?php header('Location: mix.php');?>">Back to Mix.php</button>
</div>
</body>

</html>
