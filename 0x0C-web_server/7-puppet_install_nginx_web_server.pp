# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Set up Nginx config file
file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => "
    server {
      listen 80;
      server_name _;
      
      location / {
        root /var/www/html;
        index index.html;
        try_files \$uri \$uri/ =404;
      }
      
      location /redirect_me {
        return 301 /redirected;
      }
      
      location /redirected {
        return 301 /;
      }
    }
  ",
  notify => Service['nginx'],
}

# Create root HTML file
file { '/var/www/html/index.html':
  ensure => present,
  content => 'Hello World!',
}

# Start and enable Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}
