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
main(input);



sub main {
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
}

sub speak_number_ones {
    #variable "one doesn't exist yet, you have to declare it
    #all varriables are prefixed. they need either $, @, or %

    #(one = 1) assigned one the value of 1. use eq or ==
    # you can do this with one-liner ifs or a switch
    if (one eq 1) {
	print "one ";
    }    elsif (one = 2) {
	print "two ";
    }    elsif (one = 3) {
	print "three ";
    }    elsif (one = 4) {
	print "four ";
    }    elsif (one = 5) {
	print "five ";
    }    elsif (one = 6) {
	print "six ";
    }    elsif (one = 7) {
	print "seven ";
    }    elsif (one = 8) {
	print "eight";
    }    elsif (one = 9) {
	print "nine ";
    }
}

sub speak_number_tens {

}

sub speak_number_teens {

}

sub speak_number_hundreds {

}

