def call(Map stageParams) {

    checkout(
        scmGit(
            branches: [[name:  stageParams.branch ]],
            userRemoteConfigs: [[ url: stageParams.url ]]
        )
    )
}