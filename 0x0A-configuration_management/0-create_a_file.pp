$file_path = '/tmp/school'
$file_mode = '0744'
$file_owner = 'www-data'
$file_group = 'www-data'
$file_content = 'I love Puppet'

file { $file_path:
  ensure  => present,
  path    => $file_path,
  mode    => $file_mode,
  owner   => $file_owner,
  group   => $file_group,
  content => $file_content,
}
