using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

/*
 
 dotnet publish -c Release -r linux-x64 # 在dangan 根目录运行

 cd /mnt/dangan/Server/bin/Release/net5.0/linux-x64

 ./dangan.Server --urls http://0.0.0.0:5000
	# 外网正常访问
 
 */

namespace dangan.Server
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //anime.import();

            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    webBuilder
                    //.UseUrls("http://*:5000", "https://*:5001")
                    .UseStartup<Startup>();
                });
    }
}
