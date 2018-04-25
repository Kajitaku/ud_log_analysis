# ud_log_analysis
Source code for Logs Analysis Project

**analyze.py includes three queries and outputs following results.**

1. What are the most popular three articles of all time?
1. Who are the most popular article authors of all time?
1. On which days did more than 1% of requests lead to errors?

# Install following tools.
**Virtual Machine**
1. [vagrant](https://www.vagrantup.com/)
2. [virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) (ver 5.1)

**Git**
If you don't already have Git installed, download Git from [git-scm.com](https://git-scm.com/downloads)

# Set up
**Virtual Machine**
1. Run `git clone https://github.com/udacity/fullstack-nanodegree-vm.git` to get virtual machine environment.
2. `cd fullstack-nanodegree-vm`
3. `vagrant up` to lunch a virtual machine.

**Database**
1. Get a mock PostgreSQL database zip file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
2. Unzip the zip and put extracted newsdata.sql into ./fullstack-nanodegree-vm/vagrant/
3. `vagrant ssh` to login a virtual machine.
4. Move to /vagrant inside it.
5. Run `psql -d news -f newsdata.sql` to load database data.

**Source code**
1. Run `cd ./fullstack-nanodegree-vm/vagrant/`
2. Run `git clone https://github.com/Kajitaku/ud_log_analysis.git` to get analysis code.

# How to use
1. `cd ./fullstack-nanodegree-vm/vagrant/`
2. `vagrant up`
3. `vagrant ssh`
4. `cd /vagrant/ud_log_analysis`
5. `python analyze.py`

# License