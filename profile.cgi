#!/usr/bin/perl  -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

print header ();

$userid = param("userid");
$account_no = param("account_no");

$outf =  "customer_balance.out";
$intf =  "register_2.out"; #user_name and password
$outf_1 =  "register_3.out"; #user_name and email
$intf_1 =  "register_4.out"; #user_name and name

print<<EOP; 
<html>
<head><title>Profile Info</title>
<meta name="author" content="Satyawant_Kumar Josy_Sebastian Reuben_Johns">
<link rel="stylesheet" href="design.css">
</head>
<body class="body_background">
<div class="sidenav">
	<a href="home.htm">Home</a>
	<a href="contact.htm">Contact</a>
	<a href="services.htm">Services</a>
	<a href="about.htm">About</a> 
</div>
</body>
</html>
EOP

open(OUT,"$intf_1") || die "can't read to $intf_1";
%hash_name = split(",", <OUT>);
close(OUT);

$name = $hash_name{$userid};
@names = split(" ", $name);

open(OUT,"$outf_1") || die "can't read to $outf_1";
%hash_email = split(",", <OUT>);
close(OUT);

$email = $hash_email{$userid};

open(OUT,"$intf") || die "can't read to $intf";
%hash_pass = split(",", <OUT>);
close(OUT);

$password = $hash_pass{$userid};

open(OUT,"$outf") || die "can't read to $outf";
%hash_balance = split(",", <OUT>);
close(OUT);

$balance = $hash_balance{$userid};

if(!exists($hash_balance{$userid})){
	$balance = 0;
}


print<<EOP;

<div class="content">
	<h2 class="heading">Welcome to KNU Pay</h2><br>
	<div class="profile_body"><br>
		<h2 style="text-align:center;">Account Profile Info:</h2><hr>
		<p>Account No: <b>$account_no</b></p>
		<p>First Name: <b>$names[0]</b></p>
		<p>Last Name: <b>$names[1]</b></p>
		<p>Email Address: <b>$email</b></p>
		<p>Your User Name: <b>$userid</b></p>
		<p>Account Password: <b>$password</b></p>
		<p>Current Account Balance: <b>$balance</b> dollar!</p>
	</div>
</div>
EOP