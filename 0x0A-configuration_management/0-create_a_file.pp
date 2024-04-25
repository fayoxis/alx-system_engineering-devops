# This is a  manifest creates  at /tmp
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
