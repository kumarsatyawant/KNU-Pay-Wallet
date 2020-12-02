#!/usr/bin/perl  -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

#$lgn = "transfer_money.htm";

$outf =  "register_1.out"; #account and user_name
$outf_1 =  "register_4.out"; #user_name and name
$itf = "customer_balance.out"; #user_name and balance

$rec_account_no = param("rec_account_no"); #receiver account no
$send_account_no = param("account_no"); # sender account no
$amount = param("amount");
$userid = param("userid"); #sender user_name

# Output the HTTP header
print header ();

print<<EOP; 
<html>
<head><title>Confirm Transfer</title>
<meta name="author" content="Satyawant_Kumar Josy_Sebastian Reuben_Johns">
<link rel="stylesheet" href="design.css">
<style>
input[type=submit] {
  width: 30%;
  background-color: #0080ff;
  border-radius: 5px;
  font-size: 12px;
  margin-left: 150;
  padding: 10px;
  text-align: center;
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

if($rec_account_no eq $send_account_no){
		print<<EOP; 
			<head><title>Account Validation</title></head>
			<body><div class="content heading_new"><br>
			<h2>Same Sender's and Receiver's account Account No</h2>
			<p>Sender's Account No: <font color="red">$send_account_no</font>.</p>
			<p>Receiver's Account No: <font color="red">$rec_account_no</font>.</p>
			<p>You can't transfer to your own Account. Please enter another account No!!</p>
EOP
		exit;
	}

open(OUT,"$outf") || die "can't read to $outf";
%hash_account_no = split(",", <OUT>);
close(OUT);

$count = 0;

foreach $key (keys %hash_account_no) {
	if($key eq $rec_account_no){
		$count++;
	}
}

if($count > 0){
	$rec_userid = $hash_account_no{$rec_account_no};
	
	open(OUT,"$itf") || die "can't read to $itf";
	%hash_balance = split(",", <OUT>);
	close(OUT);
		
	$send_balance = $hash_balance{$userid};
	
	if(!exists($hash_balance{$userid})){
		$send_balance = 0;
	}
	
	$rec_balance = $hash_balance{$rec_userid};
	
	if(!exists($hash_balance{$rec_userid})){
		$rec_balance = 0;
	}
	
	if($send_balance >= $amount){
			open(OUT,"$outf_1") || die "can't read to $outf_1";
			%hash_rec_name = split(",", <OUT>);
			close(OUT);
	
			$rec_name = $hash_rec_name{$rec_userid};
			
			$post_send_bal = $send_balance - $amount;
			$post_rec_bal = $rec_balance + $amount;
	
			print<<EOP; 
			<div class="content">
				<h2 class="heading">Welcome to KNU Pay</h2><br>
				<div class="transfer_body"><br>
					<h2 style="text-align:center;">Please Note that:</h2><hr>
					<p>Transfer Amount: <b>$amount dollar</b></p>
					<p>Receiver's Account NO: <b>$rec_account_no</b></p>
					<p>Receiver's Name: <b>$rec_name</b></p>
					<p style="text-align:center;">Please press <b>Confirm</b> below to proceed.</p>
					
					<form action="transaction_update.cgi" method="post">
						<input type="hidden" name="post_send_bal" id="post_send_bal" value=$post_send_bal>
						<input type="hidden" name="post_rec_bal" id="post_rec_bal" value=$post_rec_bal>
						<input type="hidden" name="userid" id="userid" value=$userid>
						<input type="hidden" name="rec_userid" id="rec_userid" value=$rec_userid>
						<input type="hidden" name="amount" id="amount" value=$amount>
						<input type="hidden" name="rec_account_no" id="rec_account_no" value=$rec_account_no>
						<b><input type="submit" value="Confirm"></b>
					</form>
				</div>
			</div>
EOP
	}
	else{
		print<<EOP; 
		<head><title>Balance Validation</title></head>
		<body><div class="content heading_new"><br>
		<h2>Insufficient Balance</h2>
		<p>Available balance: <font color="red">$send_balance dollar!</font></p>
		<p>Please recharge your wallet!!</p>
EOP
	}
}
else{
	print<<EOP; 
		<head><title>Account Validation</title></head>
		<body><div class="content heading_new"><br> 
		<h2>Invalid Account No</h2>
		<p>Account No: <font color="red">$rec_account_no</font> does not exists.</p>
EOP
}