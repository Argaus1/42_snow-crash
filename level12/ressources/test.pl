#!/usr/bin/env perl
# Test version for terminal use — no CGI

use strict;
use warnings;

# Hardcoded test inputs
my $x = "\"<test;\$CMD>\$BLA;\"";
my $y = "somevalue";

sub t {
  my ($xx, $nn) = @_;
  $xx =~ tr/a-z/A-Z/; 
  $xx =~ s/\s.*?//;
  print($xx);
  print("\n");
  my @output = `egrep "^$xx" /tmp/xd 2>&1`;
  foreach my $line (@output) {
      my ($f, $s) = split(/:/, $line);
      if ($s =~ $nn) {
          return 1;
      }
  }
  return 0;
}

sub n {
  if ($_[0] == 1) {
      print("..");
  } else {
      print(".");
  }    
}

n(t($x, $y));
print "\n";
