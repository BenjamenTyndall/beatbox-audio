<?php
$validity = 0;
$username = $_POST["name"];
$email = $_POST["email"];
$pass = $_POST["password"];
$password = password_hash($pass, PASSWORD_BCRYPT);
if (isset($_POST["submit"])) {
	$userdets = mysqli_query($conn, "SELECT * FROM users WHERE username = '$username' OR email = '$email'");
	$row = mysqli_fetch_assoc($userdets);
	if(mysqli_num_rows($userdets) > 0){
		$fetchpass = mysqli_query($conn, "SELECT * FROM users WHERE password = '$hashpass'");
		echo password_verify($pass, $fetchpass);
		if ($fetchpass) {
			echo password_verify($pass, $fetchpass);
		}
	else{
			echo "<script>alert('Password does not match, try again')</script>";
		}
	}
	else{
		echo "<script>alert('User is not registered')</script>";
	}
}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>

<div class="theForm middle smallPadding darkvc" id="login-popup">
	<form method="post" class="white form-box darkvc smallPadding">
		<button class="tr white clear" onclick="closeForm()">X</button>
		<h1 id="logintext">log-in</h1>
			<label for="usernameoremail" id="enter-user">Username</label>
			<input type="name" placeholder="Username" id="name" name="name" required value="">
		<br>
			<label for="password">Password*</label>
			<input type="password" placeholder="********" name="password" required value="">
		<br>
			<button type="submit" name="submit" class="smallPadding btn">log in</button>
		<div>
		<p6 id="areyounew"> are you new?</p6> <a href="sign-up.php" id="signuphere" class="underline vcpurple">sign up here</a>
		</div>
	</form>
</div>
</body>
</html>