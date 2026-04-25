Let's say in one of your pipeline script, there are some common stages::

    stages {
        stage("build") { ... }
        stage("test") { ... }
        stage("deploy") { ... }
    }

You want to write a shared library and parameterize those stages. So you can easily reuse them in other pipeline script::

    stages {
        stage("build") { ... }
        myCommonTestStage()
        stage("deploy") { ... }
    }

**THE ANSWER IS NO, THERE's NO WAY YOU CAN DO THAT!!!**

At the end of official doc https://www.jenkins.io/doc/book/pipeline/shared-libraries/ you will see:

    Only entire pipelines can be defined in shared libraries as of this time. This can only be done in vars/*.groovy, and only in a call method. Only one Declarative Pipeline can be executed in a single build, and if you attempt to execute a second one, your build will fail as a result.

**Conclusion**

If you really want to write a shared library for resuable stages, you have two option:

1. Write a Highlevel Pipeline Script, and use Disclosure to injecting customize code block into it. See example 3.
2. Only include code block inside of ``steps { ... }`` (DO NOT INCLUDE ``steps``), put valid ``step`` derivative like ``script`` in your ``call()`` function. And reference the library name inside of ``steps { ... }``
