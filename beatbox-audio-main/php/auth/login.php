<?php

require "../config/configure.php";
error_reporting(E_ALL);
ini_set('display_errors', 1);
if(isset($_POST["submit"])){
  $user = $_POST["name"];
  $password = $_POST["password"];
  $hashpass = password_hash($password, PASSWORD_DEFAULT);
  $match = mysqli_query($conn, "SELECT * FROM users WHERE username = '$user'");
  $hashed = mysqli_query($conn, "SELECT * FROM users WHERE password = '$password'");
  $row = mysqli_fetch_assoc($match);
  if (mysqli_num_rows($match)>0 ){
    if (password_verify($password, (string)$row['password'])) {
      $_SESSION["login"] = true;
      $_SESSION["id"] = $row["id"];
	sleep(2);
            header("Location: ../audio/mix.php");

      // code...
      }
    else{
      echo "
      <script>
              alert('Incorrect username or password');
              
              
      </script>

      ";      
        }
    }
  else{
    echo "<script>alert('This user does not exist..');</script>
    ";
  }
  }
?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" href="../../images/BEATBOXAUDIO-favicon-TRANSPARENT.JPG" type="image/x-icon">
    <link rel="icon" href="BEATBOXAUDIO-favicon-TRANSPARENT.jpg" type="image/x-icon">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <link href="../../css/style.css" rel="stylesheet">
    <link href="../../css/style.css?<?php echo time(); ?>" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@600&display=swap" rel="stylesheet">
    <title>Beatbox Audio</title>
  </head>
<body class="audioback darkvc">

  <nav class="navbar sticky shadow">
      <hr class="white">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
      <img src="../../images/BEATBOXAUDIO_WHITE-TRANSPARENT.png" alt="Logo" width="50" height="50"class="d-inline-block align-text-top"></a>
    <a href="" class="white midd smallPadding moveright mobile-hide">Beatbox Audio</a>
    <a type="button" class="btn btn-primary vcpurpleBG smallPadding pbutton" href="../../index.php">Home</a>
  </div>
  <br class="smallPadding lower">
</nav>

<div class="primary card smallPadding darkvc form-mid" id="">
  <form method="post" class="mobile-responsive white form-box darkvc smallPadding white form-box darkvc smallPadding">
    <h1 id="logintext">Log-in</h1>
      <label for="name" id="enter-user username">Username</label>
      <input type="name" placeholder="Username" id="enter-user" name="name" required value="">
    <br>
      <label for="password">Password</label>
      <input type="password" placeholder="********" name="password" required value="">
    <br>
      <button type="submit" name="submit" class="smallPadding btn" >Log in</button>
      <div>
    <p6 id="areyounew"> are you new?</p6> <a href="sign-in.php" id="signuphere" class="underline vcpurple">sign up here</a>
    </div>
  </form>
</div>
</body>
</html>

