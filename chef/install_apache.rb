# install_apache.rb
# This Chef recipe installs Apache and ensures the service is running

package 'apache2' do
  action :install
end

service 'apache2' do
  action [:enable, :start]
end
