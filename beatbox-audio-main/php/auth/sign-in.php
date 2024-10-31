<?php
$noti = "";
require "../config/configure.php";
if(isset($_POST["submit"])){
        $validity = 0;
        $username = $_POST["name"];
        $email = $_POST["email"];
        $password = $_POST["password"];
        $hashpass = password_hash($password, PASSWORD_DEFAULT);
	if(filter_var($email, FILTER_VALIDATE_EMAIL)){

        $duplicate = mysqli_query($conn, "SELECT * FROM users WHERE username = '$username' OR email = '$email' ");
        if (mysqli_num_rows($duplicate) > 0) {
                $noti = "This email or username is already taken.";


	}else {
              	$query = "INSERT INTO users (username, email, password, validity) VALUES('$username', '$email', '$hashpass', '$validity')";
                mysqli_query($conn, $query);
		sleep(1);
		ob_end_flush();
                $noti = "You are now registered with Beatbox Audio!";
	//	header("Location : index.php");
        	}
	}else{
		$noti = "Not a valid email, please try again!";
	}
}
?>

<!DOCTYPE HTML>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Sign up!</title>
	<link rel="shortcut icon" href="images/BEATBOXAUDIO-favicon-TRANSPARENT.JPG" type="image/x-icon">
  <link rel="icon" href="BEATBOXAUDIO-favicon-TRANSPARENT.jpg" type="image/x-icon">
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
	<link rel="stylesheet" type="text/css" href="../../css/style.css">
</head>
<body class="audioback darkvc">
  	<nav class="navbar sticky shadow">
      <hr class="white">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
      <img src="../../images/BEATBOXAUDIO_WHITE-TRANSPARENT.png" alt="Logo" width="50" height="50"class="d-inline-block align-text-top"></a>
    <a href="" class="white midd smallPadding moveright">Beatbox Audio</a>
    	<p6 class=" darkvc bottom"><?php echo $noti ?></p6>
  </div>
</nav>
<br>
<form method="post"class="mobile-responsive white form-box darkvc smallPadding">
	<div class="">
		<h1 id="logintext">Sign-up</h1>
			<label for="name" id="enter-user">Username</label>
			<input type="name" placeholder="Username" id="enter-user" name="name" required>
		</div>
		<br>
		<div id="signon" class="">
			<label for="email" id="Email">Email address*</label>
			<input type="email" placeholder="email address" id="enter-email" name="email" required>	
		</div>
		<br>
			<label for="password">Password*</label>
			<input type="password" placeholder="********" name="password" required>
		<br>
			<button type="submit" name="submit" href="logincode.php" class="smallPadding btn">register</button>
		<div>
		<p6> already registered?</p6>  <a href="login.php" class="underline vcpurple">log-in here</a>
		</div>
	</form>
</div>
<footer>
</footer>
</body>
</html>
