# puppet declarative script to install flask from pip3.
$flask_package_ensure = '2.1.0'
$flask_package_provider = 'pip3'

package { 'flask':
  ensure   => $flask_package_ensure,
  provider => $flask_package_provider,
}
