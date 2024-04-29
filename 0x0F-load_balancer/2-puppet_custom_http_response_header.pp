# names of the custom HTTP header must be X-Served-By.
# The value of the custom HTTP header

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
  match => 'http {',
}
-> exec {'start':
  command => '/usr/sbin/service nginx start',
}
exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}
