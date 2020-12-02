#!/usr/bin/perl  -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$outf =  "register_1.out"; #account and user_name

$itf =  "customer_balance.out";
$itf_1 =  "register_4.out"; #user_name and name

$wall = "wallet_history.out"; 

$lm = "adm_real_login.htm";

$cust_account_no = param("cust_account_no");
$amount = param("amount");
$trans_type = param("trans_type");

print header ();

print<<EOP; 
	<html>
	<head><title>Transaction Update</title>
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

open(OUT,"$outf") || die "can't read to $outf";
%hash = split(",", <OUT>);
close(OUT);

$count = 0;

foreach $key (keys %hash) {
	if($key eq $cust_account_no){
		$count++;
	}
}

if($count > 0){
	$cust_user_name = $hash{$cust_account_no};
	
	open(OUT,"$itf") || die "can't read to $itf";
	%hash_balance = split(",", <OUT>);
	close(OUT);
	
	open(OUT,"$itf_1") || die "can't read to $itf";
	%hash_name = split(",", <OUT>);
	close(OUT);
	
	if($amount > 0){
		if($trans_type eq "deposit"){
		$hash_balance{$cust_user_name} += $amount;
	
		open(OUT,">$itf") || die "can't read to $itf";
		$, = ",";
		print OUT %hash_balance;
		close(OUT);
	
		print <<EOP;	
			<html><head><title>Customer Account Update</title></head>
			<body>
			<div class="content heading_new"><br>
			<h2>Confirmation page</h2>
			<p><b>$amount dollar!</b> has been credited to Account No: <b>$cust_account_no</b>.</p>
			<p>Updated Account balance: <b>$hash_balance{$cust_user_name} dollar!</b>.</p>
			<p>Account Holder's Name: <b>$hash_name{$cust_user_name}!</b>.</p>
			
			<p>Update more <a href=$lm>details</a></p>
			</body></html>
EOP
	
		open(OUT,"$wall") || die "can't read to $wall";
		@hist = <OUT>;
		chomp @hist;
		close(OUT);
		
		$date = localtime();
		$update = "Self Recharge";
		
		$wallet[0] = $cust_account_no;
		$wallet[1] = $update;
		$wallet[2] = $amount;
		$wallet[3] = $date;
		
		open(OUT,">$wall") || die "can't write to $wall";

		for($i=0; $i<@hist; $i++){
			print OUT $hist[$i]."\n";
		}
		print OUT @wallet;
		close(OUT);
		}
		elsif($trans_type eq "withdraw"){
			if($hash_balance{$cust_user_name} >= $amount){
				$hash_balance{$cust_user_name} -= $amount;
	
				open(OUT,">$itf") || die "can't write to $itf";
				$, = ",";
				print OUT %hash_balance;
				close(OUT);

				print <<EOP;	
					<html><head><title>Customer Account Update</title></head>
					<body>
					<div class="content heading_new"><br>
					<h2>Confirmation page</h2>
					<p><b>$amount dollar!</b> has been debited from Account No: <b>$cust_account_no</b>.</p>
					<p>Updated Account balance: <b>$hash_balance{$cust_user_name} dollar!</b>.</p>
					<p>Account Holder's Name: <b>$hash_name{$cust_user_name}!</b>.</p>
					<p>Update more <a href=$lm>details</a></p>
					</body></html>
EOP

				open(OUT,"$wall") || die "can't read to $wall";
				@hist = <OUT>;
				chomp @hist;
				close(OUT);
		
				$date = localtime();
				$update = "Self Withdraw";
				#@wallet = [];
				$wallet[0] = $cust_account_no;
				$wallet[1] = $update;
				$wallet[2] = $amount;
				$wallet[3] = $date;
		
				open(OUT,">$wall") || die "can't write to $wall";

				for($i=0; $i<@hist; $i++){
					print OUT $hist[$i]."\n";
				}
				
				print OUT @wallet;
				close(OUT);
			}
			else{
				if(!exists($hash_balance{$cust_user_name})){
					$hash_balance{$cust_user_name} = 0;
				}
				print <<EOP;	
					<html><head><title>Customer Account Update</title></head>
					<body>
					<div class="content heading_new"><br>
					<h2>Insufficient Balance</h2>
					<p>Current Account Balance: <b>$hash_balance{$cust_user_name} dollar! only</b>.</p>
					<p>Please <a href=$lm>go back</a> and try again.</p>
					</body></html>
EOP
			}
		}
	}
	else{
		print <<EOP;	
		<html><head><title>Customer Account Update</title></head>
		<body>
		<div class="content heading_new"><br>
		<h2>Input Error</h2>
		<p>Invalid Amount: <b>$amount!</b>. Please enter amount greater than <b>0 dollar!.</b></p>
		<p>Please <a href=$lm>go back</a> and try again.</p>
		</body></html>
EOP
	}
}
else{
	print <<EOP;	
		<html><head><title>Customer Account Update</title></head>
		<body>
		<div class="content heading_new"><br>
		<h2>Input Error</h2>
		<p>Invalid Customer Account Number: <b>$cust_account_no!</b>.</p>
		<p>Please <a href=$lm>go back</a> and try again.</p>
		</body></html>
EOP
}


