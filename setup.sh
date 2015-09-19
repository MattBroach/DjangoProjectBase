# Simple setup.sh for configuring Ubuntu 14.04 vagrant virtual box

# Set Environmental Variable and paths.  
# NOTE the possible values for THIS_LOC are 'local', 'staging', and 'production'
# Set MYPATH to the location of the manage.py file for the project file
export THIS_LOC='local'
export MYPATH=/vagrant
echo "export DJANGO_LOCATION=$THIS_LOC" >> ~/.profile
echo "export DJANGO_PATH=$MYPATH" >> ~/.profile

# Ubuntu aliases
touch ~/.bash_aliases
echo "alias runs='python3 $MYPATH/manage.py runserver [::]:8001'" >> ~/.bash_aliases && source ~/.bash_aliases
echo "alias shell='python3 $MYPATH/manage.py shell'" >> ~/.bash_aliases && source ~/.bash_aliases
echo "alias resetdb='bash $MYPATH/reset.sh'" >> ~/.bash_aliases && source ~/.bash_aliases
echo "alias ft='python3 $MYPATH/manage.py test'" >> ~/.bash_aliases && source ~/.bash_aliases
echo "alias mm='python3 $MYPATH/manage.py makemigrations'" >> ~/.bash_aliases && source ~/.bash_aliases
echo "alias migrate='python3 $MYPATH/manage.py migrate'" >> ~/.bash_aliases && source ~/.bash_aliases
		
# General updates
sudo apt-get update
sudo locale-gen en_US.UTF-8

# Install PostgreSQL and setup database
sudo apt-get install -y postgresql 
sudo apt-get install -y postgresql-contrib
sudo -u postgres psql -U postgres -d postgres -c "alter user postgres with password 'password';"
sudo -u postgres createdb {{project_name | lower}}_db
sudo -u postgres psql -c "CREATE EXTENSION adminpack;"

# Install necessary libraries
sudo apt-get install -y python3-dev
sudo apt-get install -y libpq-dev

# Install pip and necessary packages
sudo apt-get install -y python3-pip
sudo pip3 install django
sudo pip3 install psycopg2

#Server software
#installed when not local
if [ "$THIS_LOC" != 'local' ]; then
    sudo pip3 install uwsgi
    sudo apt-get install -y nginx

fi

# Development packages
sudo pip3 install django-debug-toolbar