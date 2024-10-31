
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" href="../../images/BEATBOXAUDIO-favicon-TRANSPARENT.jpg" type="image/x-icon">
    <link rel="icon" href="../../images/BEATBOXAUDIO-favicon-TRANSPARENT.jpg" type="image/x-icon">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <link href="../../css/style.css" rel="stylesheet">
    <link href="../../css/style.css?<?php echo time(); ?>" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@600&display=swap" rel="stylesheet">
    <title>Beatbox Audio</title>
  </head>
  <body class="back darkvc">
  	<nav class="navbar sticky shadow">
      <hr class="white">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
      <img src="../../images/BEATBOXAUDIO_WHITE-TRANSPARENT.png" alt="Logo" width="50" height="50"class="d-inline-block align-text-top"></a>
    <a href="" class="white midd smallPadding moveright mobile-hide">Beatbox Audio</a>
    <a type="button" class="btn btn-primary vcpurpleBG smallPadding pbutton" href="/php/auth/login.php">Login</a>
  </div>
  <br class="smallPadding lower">
</nav>
	<div class="smallPadding lefty midd text-left">
  <div class="row">
    <div class="col">
         <h1 style="" class="big orange">Mix <span class="white">and </span class="orange"><span>master</span><br><span class="white"> your beatbox track instantly!</span></h1>
         <br>
    </div>
    <div class="col righty mobile-mid">
            <div class="card box smallPadding rrrr righty">
    <div class="card-body">
        <img class="logo lowpacity" src="../../images/upload_icon.svg" width="250px" height="250px" alt="">
      <div class="logotext mid grey">
        What is your audio source? 
      </div>
      <a id="mustlogin" onclick="glow(event)" name="" method="" action="" class=" logobutton btn btn-primary vcpurpleBG blanked">Audio File
      </a>
      <a id="mustlogin" onclick="glow(event)" class=" btn btn-primary vcpurpleBG logobutton blanked">Microphone</a>
        <hr class="white rounded solid">
        <a id="loginbutton" href="/php/auth/login.php" type="button" class="open mid btn btn-primary vcpurpleBG smallPadding pbutton">Login to continue</a>
     </div>
   </div>
<br> 
	<nav class="">
	</div>
</nav>
  </body>
    <script type="text/javascript" src="loginmechanics.js"></script>

		<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</html>
