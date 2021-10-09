using dangan.Shared;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace dangan.Server.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class searchController : ControllerBase
    {

        public static bool initQ = false; 

        private static readonly string[] Summaries = new[]
        {
            "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
        };

        private readonly ILogger<searchController> _logger;

        public searchController(ILogger<searchController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public IEnumerable<WeatherForecast> Get()
        {
            var rng = new Random();
            return Enumerable.Range(1, 5).Select(index => new WeatherForecast
            {
                Date = DateTime.Now.AddDays(index),
                TemperatureC = rng.Next(-20, 55),
                Summary = Summaries[rng.Next(Summaries.Length)]
            })
            .ToArray();
        }

        [HttpPost]
        public async Task<JsonResult> Post()
        {

            Response.Headers.Add("Access-Control-Allow-Origin", "*");

            if (!Request.Form.ContainsKey("keyword") || !Request.Form.ContainsKey("lang_select"))
            {
                return new JsonResult(new
                {
                    status = 201,
                    msg = "Form args not correct.",
                    data = new JArray()
                });
            }

            string prms = $" {{ \"keyword\" : \"{Request.Form["keyword"]}\", \"lang_select\": \"{Request.Form["lang_select"]}\" }} ";  // $ 里面的 { 要双写进行转义

            string keyword = "";
            string lang_select = "";

            Dictionary<string, string> prmsJson = null;
            if (prms == null || prms == "")
            {
                return new JsonResult(new
                {
                    status = 201,
                    msg = "参数为空",
                    data = new JArray()
                });
            }
            else
            {
                try
                {
                    prmsJson = JsonConvert.DeserializeObject<Dictionary<string, string>>(prms);
                    keyword = prmsJson["keyword"];
                    lang_select = prmsJson["lang_select"];

                    if (keyword == "")
                    {
                        return new JsonResult(new
                        {
                            status = 201,
                            msg = "参数为空",
                            data = new JArray()
                        });
                    }
                }
                catch (Exception)
                {
                    return new JsonResult(new
                    {
                        status = 201,
                        msg = "参数json 解析错误",
                        data = new JArray()
                    });
                }
            }



            string ret = await anime.search(keyword);
            prmsJson["result"] = ret;

            return new JsonResult(new { status = 200, msg = "success.", data = prmsJson });
        }
    }
}
