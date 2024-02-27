#!/usr/bin/env ruby
# This script accepts an argument then passes it to a regular expression,
#  that matches method
# This regular expression must match School

puts ARGV[0].scan(/School/).join
