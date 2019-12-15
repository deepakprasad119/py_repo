
# <h1> Puppet Topics



# <h2> What is Puppet?

The Puppet is a configuration management tool that is extensively used for automating the administration tasks. Puppet tool helps you deploy, manage and configure your servers.


# <h2> What is Manifests?

The Manifests are just files in Puppet wherein the client configuration is specified.
The manifest is the closest thing to what one might consider a Puppet program.

# <h2> What is the difference between a Module and a Manifest?
The manifests that we define in modules can be included in the manifests. This makes it easier to manage the manifests. It is possible to push the chosen manifest on to the specific agent or node.

A module is a structure used for creating portable code. While modules usually contain manifests, they also typically contain files, templates, metadata, and test cases
 
# <h2> What is Facter?
The Facter is a system profiling library which is used to gather system information during a Puppet run. The Facter offers your information regarding the IP address, version of kernel, CPU and others.


# <h2> What is MCollective?
The MCollective is a tool that is developed by the Puppet labs for server orchestration. MCollective helps to run thousands of jobs in parallel using your own or existing plugins.
