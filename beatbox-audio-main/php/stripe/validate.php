<?php
 error_reporting(E_ALL);
ini_set("display_error",1);
require 'configure.php';
if (!empty($_SESSION["id"])) {
  $id = $_SESSION["id"];
	echo $id;
  $res = mysqli_query($conn, "SELECT * FROM users WHERE id = '$id'");
  $row = mysqli_fetch_assoc($res);
  $sesh = $_GET['session_id'];

//	$sesh = "TESTTESTaldkgj334k5kodoksodkoo";
echo $sesh;
  $query = "UPDATE users SET subscriberID = '$sesh' WHERE id = '$id'";
	mysqli_query($conn, $query);
	echo $query;
	header("Location: mix.php");
	if(mysqli_query($conn, $query)){

		echo "Updated!";
}else{
	echo "error: ".mysqli_error($conn);
}
  }
if(!isset($_SESSION['login'])){
  header("Location: index.php");
}
echo $row['username'];
echo $row['email'];
echo $row['id'];
echo $row['subscriberID'];




?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>user integration</title>
</head>
<body>
</body>
</html>
