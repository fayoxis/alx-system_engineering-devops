#!/usr/bin/env ruby
#  script accepts an argument then passes it to a regular expression
puts ARGV[0].scan(/hbt+n/).join
