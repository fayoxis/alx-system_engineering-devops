# puppet declarative script to install flask from pip3.

package = {
  name     => 'flask',
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { $package['name']:
  ensure   => $package['ensure'],
  provider => $package['provider'],
}
