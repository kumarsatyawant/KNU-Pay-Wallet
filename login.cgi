#!/usr/bin/perl  -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$outf_n=  "register_1.out";
$outf=  "register_2.out";
$outf_1=  "register_3.out";
$itf_1=  "register_4.out";

$acnt = "customer_balance.out";

$lgn = "login.htm";
$rgr = "register.htm";

$userid = param("user_name");
$passwd = param("pass");

$userid_new = $userid;

# Output the HTTP header
print header ();

print<<EOP; 
	<html>
	<head><title>User Login Update</title>
	<meta name="author" content="Satyawant_Kumar Josy_Sebastian Reuben_Johns">
	<link rel="stylesheet" href="design.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<style>
		input[type=submit] {
			width: 10%;
			background-color: #B22222;
			border-radius: 5px;
			font-size: 12px;
			margin-left: 50;
			padding: 10px;
		}

		input[type=submit]:hover {
			background-color: red;
		}

		input[type=reset]:hover {
			background-color: red;
		}
		
	</style>
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

$error_message = "";
  
#Checking whether the input field is empty or filled
#if ($userid eq ""){$error_message .= "User Name";}
#if ($passwd eq ""){$error_message .= "Password";}

if ( $error_message )
  {
	#print error message if the input field is empty
	print<<EOP; 

	<head><title>Input field Validation</title></head>
	<body><div class="content"><br> 
	<h2>Incomplete Input</h2>
	<p>You did not enter <b>$error_message</b>.
    <p>Please <a href=$lgn>go back</a> and try again.</p></div>
EOP
    exit;
  }

$count = 0;

account_validation();

sub account_validation
{
	open(OUT,"$outf") || die "can't read to $outf";
	%hash = split(",", <OUT>);
	close(OUT);
	
	open(OUT,"$outf_1") || die "can't read to $outf_1";
	%hash_email = split(",", <OUT>);
	close(OUT);
	
	open(OUT,"$itf_1") || die "can't read to $itf_1";
	%hash_name = split(",", <OUT>);
	close(OUT);
	
	#Checking if the userid is correct
	foreach $key (keys %hash) 
	{
		if($key eq $userid)
		{
			$count++;
		}
	}
	
	open(OUT,"$outf_n") || die "can't read to $outf_n";
	%hash_account_no = split(",", <OUT>);
	close(OUT);
	
	foreach $key (keys %hash_account_no) 
	{
		if($hash_account_no{$key} eq $userid)
		{
			$account_no = $key;
		}
	}
	
	open(OUT,"$acnt") || die "can't read to $acnt";
	%hash_account_balance = split(",", <OUT>);
	close(OUT);
	
	if(exists($hash_account_balance{$userid})){
		$aval_balance = $hash_account_balance{$userid};
	}
	else{
		$aval_balance = 0;
	}
	
	#$aval_balance .= " dollar";
}

if($count > 0){
	
	#Checking if the password is correct. If yes then print the login confirmation else print error message
	if($hash{$userid} eq $passwd){
		print<<EOP; 
			<head><title>ID Validation</title></head>
			<body><div class="content heading_new"><br> 
			<h2>You are successfully Login!</h2>
			<p class="right">Welcome <b>$hash_name{$userid}!</b>.</p>
			<p class="right">Account No: <b>$account_no</b></p></div><br>
			
			<div class="content">
			<ul>
			<form action="profile.cgi" method="post">
				<input type="hidden" name="userid" id="userid" value=$userid>
				<input type="hidden" name="account_no" id="account_no" value=$account_no>
				<b><input type="submit" value="Profile"></b>
			</form>
			
			<form action="wallet_history.cgi" method="post">
				<input type="hidden" name="userid" id="userid" value=$userid>
				<input type="hidden" name="account_no" id="account_no" value=$account_no>
				<b><input type="submit" value="Wallet History"></b>
			</form>
			
			<form action="transfer_money_new.cgi" method="post">
				<input type="hidden" name="userid" id="userid" value=$userid>
				<input type="hidden" name="account_no" id="account_no" value=$account_no>
				<b><input type="submit" value="Transfer Money"></b>
			</form>
			
			</ul></div>
			
			<div class="content balance">
			<ul>
				<button class="button button2" onclick="show_balance_1()"><b>View Balance</b></button>
				<button class="button button2" onclick="show_balance_2()"><b>Hide Balance</b></button><br>
				<b>Dollars:</b> <input type="text" name="account_balance" id="account_balance" disabled="disabled">
			</ul>
			</div>
			
			<script>
				function show_balance_1() {
					document.getElementById("account_balance").value = $aval_balance;
				}
				
				function show_balance_2() {
					document.getElementById("account_balance").value = "";
				}
			</script>
			
EOP

	}
	else{
		print<<EOP; 
			<head><title>Password Validation</title></head>
			<body><div class="content heading_new"><br> 
			<h2>Invalid Password</h2>
			<p>You have entered an invalid password: <font color="red">$passwd</font>
			<p><a href=$lgn>Login again</a></p></div>
EOP
	}
}
else{
	print<<EOP; 
			<head><title>ID Validation</title></head>
			<body><div class="content heading_new"><br> 
			<h2>Invalid UserId</h2>
			<p>UserId <font color="red">$userid</font> does not exists.
			<p><a href=$lgn>Login again</a></p></div>
EOP
}