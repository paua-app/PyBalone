import services.log as log
import tools.onKeyListener

class BasicInput(tools.onKeyListener.OnKeyListener):
    def onInput(self, key):
        #TODO just for testing. A tool with an input listener but no render listener is not thaaat useful.
        log.info("onInput-dummyProcessing", str(key))
