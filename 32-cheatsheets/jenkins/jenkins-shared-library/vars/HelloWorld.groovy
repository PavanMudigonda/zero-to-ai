import org.dcube.build.HelloWorld
import org.dcube.ioc.ContextRegistry

def call(String solutionPath) {
    ContextRegistry.registerDefaultContext(this)

    def helloworld = new HelloWorld(solutionPath)
    helloworld.build()
}