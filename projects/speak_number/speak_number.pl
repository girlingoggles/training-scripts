#!/usr/bin/env perl
#girlingoggles made this
use strict;
use warnings;

# "varriable" "input" doesn't exist (if it did it would be $input)
# command line args is in @ARGV (caps needed) so you can do either
# my $input = @ARGV[0];
#or pass it directly with:
#x main(@ARGV[0]); # passes one first comand line argument to main
# or
# main(@ARGV); # passes every comand line argument to main   
main($input);


# main should call something
# also should grab input via:
# my $input = @_;
# that will grab the first scalar passed to main (should be the string that holds the number)
    # then you should do a
    # if (not defined $input) {
    # print "enter number";
    # $input = <>;
    # }
        # and then call your function passing it $input            
sub main {
    my $input = @ARGV[0];
    if (not defined $input) {
	print "enter number";
	$input = <>;
    }
    speak_number_hundreds($input)
}

sub speak_number_ones {
    #variable "one doesn't exist yet, you have to declare it
    #all varriables are prefixed. they need either $, @, or %

    #(one = 1) assigned one the value of 1. use eq or ==
        # you can do this with one-liner ifs or a switch   
    my $one = $input

    if (one == 1) {
	    print "one ";
    }
    elsif (one == 2) {
	print "two ";
    }
    elsif (one == 3) {
	print "three ";
    }
    elsif (one == 4) {
	print "four ";
    }
    elsif (one == 5) {
	print "five ";
    }
    elsif (one == 6) {
	print "six ";
    }
    elsif (one == 7) {
	print "seven ";
    }
    elsif (one == 8) {
	print "eight ";
    }
    elsif (one == 9) {
	print "nine ";
    }
}

sub speak_number_tens {
    my $ten == int($input / 10)

    if (ten == 1) {
	speak_number_teens($input);
    }    elsif (ten == 2) {
	print "twenty ";
    }    elsif (ten == 3) {
	print "thirty ";
    }    elsif (ten == 4) {
	print "fourty ";
    }    elsif (ten == 5) {
	print "fifty ";
    }    elsif (ten == 6) {
	print "sixty ";
    }    elsif (ten == 7) {
	print "seventy ";
    }    elsif (ten == 8) {
	print "eighty ";
    }    elsif (ten == 9) {
	print "ninety ";
    }
}

sub speak_number_teens {
    if (teen == 10) {
	print "ten ";
	elsif (teen == 11) {
	    print "eleven ";
    }    elsif (teen == 12) {
	print "twelve ";
    }    elsif (teen == 13) {
	print "thirteen ";
    }    elsif (teen == 14) {
	print "fourteen ";
    }    elsif (teen == 15) {
	print "fifteen ";
    }    elsif (teen == 16) {
	print "sixteen ";
    }    elsif (teen == 17) {
	print "seventeen ";
    }    elsif (teen == 18) {
	print "eighteen ";
    }    elsif (teen == 9) {
	print "nineteen ";
    }
}


sub speak_number_hundreds {
    my $hundred = ($input / 100)
	if ($input > 99) {
	    speak_number_ones($input)
		print "hundred "
    }
    speak_number_tens($input % 100)
}

