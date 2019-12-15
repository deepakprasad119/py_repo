
# <h1> Jenkins Topics






# <h2> What is Jenkins? 
Jenkins is an open source automation tool used for continous inetration and delivery and monitor them.

With Jenkins we can build pipelines to build project, run tests and then deploy


# <h2> How to turn off Jenkins Security if the administrative users have locked out of the admin console? 

We can disable the security in config.xml file and security will be disabled when jenkins is started the next time.



# <h2> Difference between webhook and polling? 
    
There are two ways your apps can communicate with each other to share information: polling and webhooks. As one of our customer champion's friends has explained it: Polling is like knocking on your friend’s door and asking if they have any sugar. Webhooks are like someone tossing a bag of sugar at your house whenever they buy some.

Webhooks are automated messages sent from apps when something happens. They have a message—or payload—and are sent to a unique URL—essentially the app's phone number or address.

Poll SCM periodically polls the SCM to check whether changes were made (i.e. new commits) and builds the project if new commits where pushed since the last build.

# <h2> What are some of the useful plugins in Jenkins?
Git repository
Amazon EC2
HTML Publisher


# <h2> How to setup a Jenkins job?
go to the Jenkins top page and then select a ‘New Job’ and build a freestyle software project.


# <h2> What is the process for creating a backup and copy files in Jenkins?
regularly backup our Jenkins_Home directory



# <h2> What are Declarative Pipelines in Jenkins?

pipeline {
    agent any
    stages { 
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}

The above code has 3 major elements

Pipeline: The block of script contents.
Agent: Defines where the pipeline will start running from.
Stage: The pipelines contain several steps enclosed in the block called Stage.



# <h2> What is Agent Directive in Jenkins?

Answer: The Agent is the section that specifies the execution point for the entire pipeline or any
specific stage in the pipeline. This section is being specified at the top-level inside the
pipeline block.


# <h2> How can you define a Continuous Delivery Workflow?

Git Clone
Compile
Unit test
Packaging
Deploy

# <h2> What are the various ways in which the build can be scheduled in Jenkins?

After the completion of other builds.
By source code management (modifications) commit. (webhook)
At a specific time. (scheduled)
By requesting manual builds. (polling)




