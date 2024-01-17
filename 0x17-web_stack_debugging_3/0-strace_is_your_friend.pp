# site is running on Apache2, fix errors found in server
$config_file = '/var/www/html/wp-settings.php'

exec { 'edit_file':
  command => "sed -i 's/phpp/php/g' ${config_file}",
  path    => ['/bin','/usr/bin']
}
