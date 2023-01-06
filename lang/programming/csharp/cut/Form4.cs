using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using CefSharp.WinForms;

namespace MathpixCsharp
{
    public partial class Form4 : Form
    {
        ChromiumWebBrowser browser = null;

        public Form4()
        {
            InitializeComponent();

            MainAsync();

            ////string path = AppDomain.CurrentDomain.BaseDirectory + @"dist/index.html";
            //String path = string.Format(@"{0}\dist\index.html", Application.StartupPath);

            ////String path = "http://baidu.com";

            //browser = new ChromiumWebBrowser(path);
            //browser.JavascriptObjectRepository.Settings.LegacyBindingEnabled = true;

            //this.Controls.Add(browser);
            //browser.Dock = DockStyle.Fill;

            ////browser.GetBrowser().MainFrame.ExecuteJavaScriptAsync("document.dispatchEvent(new CustomEvent('event_name', { detail: { para: 'para' } }));");

            //var setting = new CefSettings { RemoteDebuggingPort = 33229 };
            ////CefSharp.Cef.Initialize(setting);

            //await browser.WaitForInitialLoadAsync();

        }

        private async void MainAsync()
        {
            //string path = AppDomain.CurrentDomain.BaseDirectory + @"dist/index.html";
            String path = string.Format(@"{0}\dist\index.html", Application.StartupPath);

            //String path = "http://baidu.com";

            browser = new ChromiumWebBrowser(path);
            browser.JavascriptObjectRepository.Settings.LegacyBindingEnabled = true;

            this.Controls.Add(browser);
            browser.Dock = DockStyle.Fill;

            //browser.GetBrowser().MainFrame.ExecuteJavaScriptAsync("document.dispatchEvent(new CustomEvent('event_name', { detail: { para: 'para' } }));");

            var setting = new CefSettings { RemoteDebuggingPort = 33229 };
            //CefSharp.Cef.Initialize(setting);

            await browser.WaitForInitialLoadAsync();

            browser.GetBrowser().MainFrame.ExecuteJavaScriptAsync("document.dispatchEvent(new CustomEvent('event_name', { detail: { para: 'para' } }));");
        }
    }
}
