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

            //string path = AppDomain.CurrentDomain.BaseDirectory + @"dist/index.html";
            String path = string.Format(@"{0}\dist\index.html", Application.StartupPath);

            //String path = "http://baidu.com";

            browser = new ChromiumWebBrowser(path);
            browser.JavascriptObjectRepository.Settings.LegacyBindingEnabled = true;

            this.Controls.Add(browser);
            browser.Dock = DockStyle.Fill;

            var setting = new CefSettings { RemoteDebuggingPort = 33229 };
            //browser.Initialize(setting);

        }
    }
}
