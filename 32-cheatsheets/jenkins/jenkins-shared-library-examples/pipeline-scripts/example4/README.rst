Let's say in one of your pipeline script, there are some common steps::

    stage("...") {
        steps {
            // step1 ...
            // step2 ...
            // step3 ...
        }
    }

You want to write a shared library and parameterize those steps. So you can easily reuse them in other pipeline script:

    stage("...") {
        steps {
            // do something first
            myCommonSteps "param1" "param2"
            // do something else
        }
    }
