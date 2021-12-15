class phoneusageonweekend:
    def __init__(self):

        
        self.Instagram   = {"screen_on_time":"28mins", "notification_recived":"139 notifications","times_opened":"50times"}
        self.facebook  = {"screen_on_time":"21mins","notification_recived":"71 notifications","times_opened":"13times"}
        self.whatsapp     ={"screen_on_time":"1hr_14mins","notification_recived":"60 notifications","times_opened":"59times"}
        self.Youtube   ={"screen_on_time":"1hr_7mins","notification_recived":"5 notifications","times_opened":"9times"}



        print("time ON screen")

        
        print("Instagram :",self.Instagram["screen_on_time"])
        print("facebook :",self.facebook["screen_on_time"])
        print("whatsapp :",self.whatsapp["screen_on_time"])
        print("Youtube :",self.Youtube["screen_on_time"],"\n")
    


        print("Notification recived in a day \n")

        print("Instagram:",self.Instagram["notification_recived"])
        print("facebook:",self.facebook["notification_recived"])
        print("whatsapp:",self.whatsapp["notification_recived"])
        print("Youtube:",self.Youtube["notification_recived"],"\n")
        

        print("Apps opened in a day \n")

        print("Instagram :",self.Instagram["times_opened"])
        print("facebook :",self.facebook["times_opened"])
        print("whatsapp :",self.whatsapp["times_opened"])
        print("Youtube:",self.Youtube["times_opened"],"\n")
       


    def saturday(self):
        self.instagram   = {"screen_on_time":"32mins", "notification_recived":"214 notifications","times_opened":"48times"}
        self.facebook ={"screen_on_time":"58mins","notification_recived":"14 notifications","times_opened":"22times"}
        self.whatsapp  = {"screen_on_time":"9mins","notification_recived":"57 notifications","times_opened":"14times"}
        self.Youtube   ={"screen_on_time":"1hr_3mins","notification_recived":"5 notifications","times_opened":"7times"}


        print("Time used  in a day \n")
        
        print("instagram :",self.Instagram["screen_on_time"])
        print("facebook :",self.facebook["screen_on_time"])
        print("whatsapp :",self.whatsapp["screen_on_time"])
        print("Youtube :",self.Youtube["screen_on_time"],"\n")

        

        print("Notification recived in a day \n")

        print("instagram :",self.Instagram["notification_recived"])
        print("facebook :",self.facebook["notification_recived"])
        print("whatsapp :",self.whatsapp["notification_recived"])
        print("Youtube :",self.Youtube["notification_recived"],"\n")
    
        print("Apps opened in a day \n")

        print("instagram --",self.Instagram["times_opened"])
        print("facebook --",self.facebook["times_opened"])
        print("whatsapp --",self.whatsapp["times_opened"])
        print("Youtube--",self.Youtube["times_opened"],"\n")
    
        
    def sunday(self):
        self.instagram   = {"screen_on_time":"27mins", "notification_recived":"169 notifications","times_opened":"57times"}
        self.facebook ={"screen_on_time":"58mins","notification_recived":"18 notifications","times_opened":"25times"}
        self.whatsapp  = {"screen_on_time":"9mins","notification_recived":"43 notifications","times_opened":"13times"}
        self.Youtube   ={"screen_on_time":"16mins","notification_recived":"5 notifications","times_opened":"6times"}


        print("Time used  in a day \n")

        print("instagram --",self.Instagram["screen_on_time"])
        print("facebook --",self.facebook["screen_on_time"])
        print("whatsapp --",self.whatsapp["screen_on_time"])
        print("Youtube --",self.Youtube["screen_on_time"],"\n")
        


        print("Notification recived in a day \n")

        print("instagram --",self.Instagram["notification_recived"])
        print("facebook --",self.facebook["notification_recived"])
        print("whatsapp --",self.whatsapp["notification_recived"])
        print("Youtube --",self.Youtube["notification_recived"],"\n")
        

        print("Apps opened in a day \n")

        print("instagram --",self.Instagram["times_opened"])
        print("facebook --",self.facebook["times_opened"])
        print("whatsapp --",self.whatsapp["times_opened"])
        print("Youtube--",self.Youtube["times_opened"],"\n")
        

    #def time_used(self):
usage = phoneusageonweekend()
usage.saturday()
usage.sunday()
