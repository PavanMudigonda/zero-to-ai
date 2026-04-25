Jenkins Shared Library Test
======

This repo demonstrate the minimal viable best practice for Jenkins Shared Library.

**How to use this Repo to learn?**

Every subfolder in ``./pipeline-scripts`` represents an example. Each folder comes with two file ``old.Jenkinsfile``, representing pipeline script without shared library, and ``new.Jenkinsfile`` representing equavilent code with shared library. In ``./vars`` each ``.groovy`` file is a Shared Library, the shared library name ``./vars/${LibraryName}`` is the same as ``./pipeline-scripts/${LibraryName}``.

You can copy and paste the content of ``old.Jenkinsfile`` to Jenkins Pipeline Configuration and run once. And then do the same thing with ``new.Jenkinsfile``.

**Setup your Jenkins before playing with this Repo**

Jenkins -> Manage Jenkins -> Configure System -> Search: Global Pipeline Libraries

Fill in git url, check "Load Implicitly" (if not check, you need to manually declare ``@Library("${LibraryName}")`` at begin of your Jenkinsfile). So your Jenkins system can load shared library implemented in this repo.

**What is Jenkins Shared Library?**

You may already very familiar with Jenkins pipeline scripts. Actually those ``node {}``, ``stages("...") {}``, ``steps { ... }``, ``script{ ... }``, ``withCredential() { ... }`` syntax are simply shared library implemented in community plugins. Those declaritive are predefined in a groovy script like ``node|stages|steps|script|withCredential.groovy``, and you will see available parameters in plugin source code. 
