# puppet declarative script to install flask from pip3.
$package_name = 'flask'
$package_version = '2.1.0'
$package_provider = 'pip3'

package { $package_name:
  ensure   => $package_version,
  provider => $package_provider,
}
