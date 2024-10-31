<?php
//login code
require "../config/configure.php";
  $id = $_SESSION["id"];
  $res = mysqli_query($conn, "SELECT * FROM users WHERE id = '$id'");
  $row = mysqli_fetch_assoc($res);
$session_id = $row['subscriberID'];
echo $session_id;

//if(is_null($session_id)){
  //      header("Location: cancel.php");
//
//}
//if(isset($_POST["submit"])){
//	echo "<script>alert('cancel')</script>";
//}
//

//https://buy.stripe.com/9AQaFQcBC3xS40w6oo
if(isset($_POST["submit"])){
	$session_id = $row['subscriberID'];

if (is_null($session_id)) {
//      header("Location: https://buy.stripe.com/test_aEUcN81VKefAc8g6oo");
  header("Location: https://buy.stripe.com/9AQaFQcBC3xS40w6oo");
//}
//if(!is_null($session_id)){
//	header("Location: cancel.php");
}
//}




	}

?>

<!DOCTYPE html>
<html>
<head>
  <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" href="../../images/BEATBOXAUDIO-favicon-TRANSPARENT.jpg" type="image/x-icon">
    <link rel="icon" href="images/BEATBOXAUDIO-favicon-TRANSPARENT.jpg" type="image/x-icon">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <link href="../../css/style.css" rel="stylesheet">
    <link href="../../css/style.css?<?php echo time(); ?>" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@600&display=swap" rel="stylesheet">
    <title>Audio - Account</title>
</head>
<body>
<body class="darkvc">
    <nav class=" back navbar sticky shadow">
      <hr class="white">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
      <img src="../../images/BEATBOXAUDIO_WHITE-TRANSPARENT.png" alt="Logo" width="50" height="50"class="d-inline-block align-text-top"></a>
    <a href="" class="white midd smallPadding moveright">Beatbox Audio</a>
    <a type="button" class="btn btn-primary vcpurpleBG bp smallPadding pbutton" href="../audio/mix.php">Mix</a>
  </div>
</nav>
  <div class="mid sticky svtop">
<h4 class="marginside white">Account: <span class="orange"><?php echo $row['username'];?></span></h4>
<hr class="white">
</div>
<div>
<form method="POST" class="mobile-responsive white form-box darkvc smallPadding">
  <div class="centre">
    <h4 id="logintext">Account info</h4>
      <label for="name" id="enter-user">Username</label>
      <h6 class="disp" type="name" placeholder=""><?php echo $row['username'];?></h6>
    <br>
    <div id="signon">
      <label for="email" id="Email">Email address</label>
      <h6 class="disp" type="email" placeholder=""id="enter-email" name="email"><?php echo $row['email'];?></h6>
    </div>
    <br>
      <label for="password">Password*</label>
      <h6 class="disp" type="password" name="password">********</h6>
    <br>
      <a href="https://billing.stripe.com/p/login/aEU7w6h1f1Fe6S48ww" class="smallPadding top white pbutton btn">Subscribe or cancel service</a>
    <div>

    </div>
  </form>


<div>
  <a class="smallPadding top white pbutton btn" href="logout.php">Log out</a>
  <hr class="white">
  <br>
  <a href="https://discord.gg/GdbJeuxD7m" class=" smallPadding top white pbutton btn" >Discord</a>
</div>
</div>

</div>
</nav>


</body>
</html>
