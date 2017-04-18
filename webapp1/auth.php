<html>
<head>
  <title> MircoBlog </title>
  <!-- Compiled and minified CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.0/css/materialize.min.css">
<link rel="stylesheet" type="text/css" href="main.css"/>
<!-- Compiled and minified JavaScript -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.98.0/js/materialize.min.js"></script>
</head>
<body>
  <nav>
  <div class ="nav-wrapper">
    <a href="#" class="brand-logo right">MicroBlog</a>
    <ul id = "nav-mobile" class = "left hide-on-med-and-down">
      <li>
        <a href="home.php">Home</a>
      </li>
      <li>
        <a href="about.php">About us</a>
      </li>
      <li>
        <a href="logout.php">Logout</a>
      </li>
    </ul>
  </div>
</nav>
<h1 class = "s12 m4 l8">
  <?php
  $_POST = parse_url($_SERVER["_POST"]);
  $a=explode("&",$_POST["path"]);

  $email = explode('=',$a[0])[1];
  $pass = explode('=',$a[1])[1];

  $email = str_replace("%40","@",$email);

  $servername = "localhost";
  $username = "root";
  $password = "passw0rd";
  $db="MICROBLOG";
  $conn=mysqli_connect($servername, $username, $password, $db);

  if(!$conn){
    die("Connection failed: ".mysqli_connect_error());
  }
  #echo "Connected successfully";
  $query = "SELECT * FROM microblog_users where email = '$email';";
  #echo $query;
  $result = mysqli_query($conn,$query);
  $row = mysqli_fetch_assoc($result);
  if(strcmp($row["pass"],$pass)!=0)
  {
    $link="login.php";
    echo "password mismatch<br />";
    echo "<a href ='".$link."'>Click here to get redirected</a>";
  }
  else {
    echo "password matched<br/>";
    $session_hash = $_SERVER["SESSION_ID"];
    $id = $row["id"];
    $query = "select * from session where ID = ".$id;
    $result = mysqli_query($conn,$query);
    $row_count = mysqli_num_rows($result);
    if($row_count==0)
    {
      $query = "INSERT INTO session(ID,session_hash) VALUES ('$id','$session_hash');";
    }
    else
    {
      $query = "UPDATE session SET session_hash='$session_hash' where id='$id';";
    }
    #echo $query;
    mysqli_query($conn,$query);
    echo "Login Sucessful<br />";
    $link="home.php";
    echo "<h6><form method='post' action='home.php'>
    <input class = 'waves-effect waves-light btn' type='submit' value='Redirect' />
    </form></h6>";
  }
  ?>

 </form>
 </h1>
 </body>
 </html>
