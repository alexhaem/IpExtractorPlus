import os, json, urllib.request, re, datetime
from multiprocessing.dummy import Pool as ThreadPool 


THREAD_NUMBER = 4


class LinksProcessor:    
    def getLocationForIp(self, ip):
        result = ''
        
        try:
            urlFoLocation = "http://www.freegeoip.net/json/{0}".format(ip)
            locationInfo = json.loads((urllib.request.urlopen(urlFoLocation).read()).decode('utf-8'))
            
            if locationInfo['country_name']:
                result = ' (Location: ' + locationInfo['country_name']
                
                if locationInfo['city']:
                    result = result + ', ' + locationInfo['city'] + ')'
                else:
                    result = result + ')'
    
        except Exception as e:
            print(e)
            
        return result


    def extractIpFromUrl(self, url):
        result = ''
        
        try:
            header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
            request = urllib.request.Request(url, headers=header)
            page = urllib.request.urlopen(request)
            byte_content = page.read()
            
            try:
                text_content = byte_content.decode('utf-8')
            except:
                text_content = byte_content.decode('windows-1252')
            
            pattern = "(\d{2,3}\.\d{1,3}\.\d{2,3}\.\d{1,3})|(\w{3,4}:\w{3,4}:\w{3,4}:\w{3,4}:\w{3,4}:\w{3,4}:\w{3,4}:\w{3,4})"
            search_result = re.search(pattern, text_content)
            
            if search_result is not None:
                ip = search_result.group(0)
                
                result = ip + " for " + url + self.getLocationForIp(ip)
                
            else:
                result = "IP address could not be defined for " + url
        except Exception as e:
            result = "Something went wrong for " + url + ": " + str(e)
        
        print(result)

        return result

    
    def extractAllIps(self, path):
        # make the Pool of workers
        pool = ThreadPool(THREAD_NUMBER) 
        
        urls = []
        
        # read lines from the file
        with open(path) as fp:
            for line in fp:
                urls.append(line.rstrip())
        
        results = pool.map(self.extractIpFromUrl, urls)
        
        # close the pool and wait for the work to finish 
        pool.close() 
        pool.join() 

        return results
    
    
    def writeIpsToFile(self, ip_list, target_file):
        timestamp = "Ip_results_" + datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S") + ".txt"
        file = os.path.join(target_file, timestamp)
        result_file = open(file, 'w')
        result_file.writelines(["%s\n" % item  for item in ip_list])

        
    def processLinks(self, source_file, target_folder):
        ip_list = self.extractAllIps(source_file)
        self.writeIpsToFile(ip_list, target_folder)
