# Fixes a faulty wordpress site

$file_to_edit = '/var/www/html/wp-settings.php'

exec { 'fix-wordpress':
  command => 'bash -c "sed -i s/class-wp-locale.phpp/class-wp-locale.php/ \
/var/www/html/wp-settings.php; service apache2 restart"',
  path    => '/usr/bin:/usr/sbin:/bin'
}
