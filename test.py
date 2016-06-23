class myTest:
    video_path = "hahahh"
    
    def getMyTestInfo(self):
        video_path = "{}{}".format(11213, self.video_path) if self.video_path else self.video_path
        testVal = 1
        print(testVal)
        print(video_path)
        return ""

myTest1 = myTest();
myTest1.getMyTestInfo()
