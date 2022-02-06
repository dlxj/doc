using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using Microsoft.Extensions.Configuration;


namespace dangan.Shared
{
    public class Config
    {
        //private static IConfigurationRoot conf = new ConfigurationBuilder()
        //         .SetBasePath(Directory.GetCurrentDirectory())
        //         .AddJsonFile("config.json")
        //         .Build();


        public static bool debugQ = true;
        public static string host { get{ return "echodict.com"; } }  // 209.141.34.77:80  // echodict.com
        public static string hostDebug = "localhost:5000";


    }

    public class WeatherForecast
    {
        public DateTime Date { get; set; }

        public int TemperatureC { get; set; }

        public string Summary { get; set; }

        public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
    }
}
