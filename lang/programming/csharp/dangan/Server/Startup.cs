using Blazored.SessionStorage;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.ResponseCompression;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Configuration.Json;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using System.IO;
using System.Linq;
using System.Text.Encodings.Web;
using System.Text.Unicode;

using dangan.Shared;

namespace dangan.Server
{
    public class Startup
    {
        readonly string myAllowSpecificOrigins = "_myAllowSpecificOrigins";

        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        // For more information on how to configure your application, visit https://go.microsoft.com/fwlink/?LinkID=398940
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllersWithViews();
            services.AddRazorPages();

            // section 支持
            services.AddBlazoredSessionStorage();

            // json 里的中文乱码
            services.AddControllers().AddJsonOptions(options =>
            {
                options.JsonSerializerOptions.Encoder = JavaScriptEncoder.UnsafeRelaxedJsonEscaping; // JavaScriptEncoder.Create(UnicodeRanges.All);
                //options.JsonSerializerOptions.Encoder = JavaScriptEncoder.Create(UnicodeRanges.All);
            });

            // 支持跨域
            services.AddCors(policy =>
            {
                policy.AddPolicy(myAllowSpecificOrigins, builder => builder.WithOrigins("http://echodict.com:80/")
                     .AllowAnyMethod()
                     .AllowAnyHeader()
                     .AllowCredentials());
            });


            //var config = new ConfigurationBuilder()
            //     .SetBasePath(Directory.GetCurrentDirectory())
            //     .AddJsonFile("appsettings.json")
            //     .Build();

            //var debugQ = bool.Parse(config["debugQ"]);
            //var hostDebug = config["hostDebug"];
            //var host = config["host"];

            //Config.debugQ = debugQ;
            //Config.hostDebug = hostDebug;
            //Config.host = host;


            //services.AddCors(options =>
            //{
            //    options.AddPolicy("any", builder =>
            //    {
            //        builder.AllowAnyOrigin()
            //        .AllowAnyMethod()
            //        .AllowAnyHeader();

            //    });
            //});

        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
                app.UseWebAssemblyDebugging();
            }
            else
            {
                app.UseExceptionHandler("/Error");
            }

            app.UseBlazorFrameworkFiles();
            app.UseStaticFiles();

            app.UseRouting();

            //添加CORS到管道中，记得一定要放在UseRouting和UseEndpoints之间，否则没用
            app.UseCors(myAllowSpecificOrigins);

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapRazorPages();
                endpoints.MapControllers();
                endpoints.MapFallbackToFile("index.html");
            });
        }
    }
}
