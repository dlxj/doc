using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Forms;

using MaterialSkin;
using MaterialSkin.Controls;
using Tesseract;
using System.IO;
using PaddleOCRSharp;

namespace MathpixCsharp
{
    public partial class Form1 : Form
    {
        //GetCode gg = new GetCode();
        //[System.Runtime.InteropServices.DllImport("user32.dll")]
        //private static extern bool RegisterHotKey(IntPtr hWnd, int id, int fsModifiers, int vk);
        Bitmap bit;
        public bool success;
        public bool cancelled;
        int last_choice = 3;
        string app_id = "";
        string app_key = "";

        public PaddleOCREngine engine = null;

        public Bitmap Bit { get => bit; set => bit = value; }

        public Form1()
        {
            InitializeComponent();
            this.pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;

            this.退出_toolStripMenuItem1.Click += new System.EventHandler(this.退出ToolStripMenuItem_Click);

            //使用默认中英文V3模型
            OCRModelConfig config = null;
            //使用默认参数
            OCRParameter oCRParameter = new OCRParameter();

            //建议程序全局初始化一次即可，不必每次识别都初始化，容易报错。     
            engine = new PaddleOCREngine(config, oCRParameter);

        }


        private void button1_Click(object sender, EventArgs e)
        {
            Clipboard.SetDataObject("set by C#.");
            string t = Clipboard.GetText(TextDataFormat.Text);


            ScreenShot sf = new ScreenShot();
            sf.Owner = this;
            this.Opacity = 0.0;
            this.success = false;
            this.cancelled = false;
            sf.ShowDialog();//make sure it's done
            if (this.cancelled)
            {
                this.Opacity = 1.0;
                return;
            }
            if (!this.success)
            {
                this.Opacity = 1.0;
                MessageBox.Show("错误，请重试");
                return;
            }

            this.pictureBox1.Image = Bit;
            Bit.Save("xxxxxxxxxxx.bmp");
            //ScreenShotToCode(Bit);
            this.Opacity = 1.0;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

            GlobalHotKey.RegisterHotKey("Alt + Shift + S", () =>
            {

                Clipboard.SetDataObject("set by C#.");
                string t = Clipboard.GetText(TextDataFormat.Text);


                ScreenShot sf = new ScreenShot();
                sf.Owner = this;
                this.Opacity = 0.0;
                this.success = false;
                this.cancelled = false;
                sf.ShowDialog();//make sure it's done
                if (this.cancelled)
                {
                    this.Opacity = 1.0;
                    return;
                }
                if (!this.success)
                {
                    this.Opacity = 1.0;
                    MessageBox.Show("错误，请重试");
                    return;
                }

                this.pictureBox1.Image = Bit;
                Bit.Save("xxxxxxxxxxx.bmp");
                //ScreenShotToCode(Bit);
                this.Opacity = 1.0;

                // https://github.com/charlesw/tesseract-samples
                // https://github.com/tesseract-ocr/tessdata/blob/main/chi_sim.traineddata 先下载语言文件 自动安装的语言模型很小，不准确
                // paddleocr --image_dir ./xxxxxxxxxxx.bmp --lang=ch
                // 换 powershell 它才不乱码

                // https://github.com/raoyutian/PaddleOCRSharp/blob/main/doc/UseInCsharp.md 
                // PPOCR C# 版

                // engine.SetVariable("tessedit_char_whitelist", "一些中文");

                //识别结果对象
                OCRResult ocrResult = null;
                {
                    ocrResult = engine.DetectText("xxxxxxxxxxx.bmp");
                }
                
                if (ocrResult != null) {
                    string text = ocrResult.Text;
                    MessageBox.Show(text, "识别结果");

                    //new Form3(text).Show();
                    new Form4().Show();

                } 

                //using (var engine = new TesseractEngine(@"./tessdata", "chi_sim", EngineMode.LstmOnly))
                //{

                //    using (var img = Pix.LoadFromFile("xxxxxxxxxxx.bmp"))
                //    {
                //        using (var page = engine.Process(img))
                //        {
                //            var text = page.GetText();

                //            File.WriteAllText(@"./xxxxxxxxxxxx.txt", text, new System.Text.UTF8Encoding(false));
                //        }
                //    }
                //}
            });

            //SystemHotKey.RegHotKey(this.Handle, 701, SystemHotKey.KeyModifiers.Alt | SystemHotKey.KeyModifiers.Ctrl | SystemHotKey.KeyModifiers.Shift, System.Windows.Forms.Keys.Back);
        }

        //protected override void WndProc(ref Message m)
        //{
        //    if ( m.Msg == WmHotKey)
        //    {
        //        var a = 1;
        //    }

        //    base.WndProc(ref m);
        //}

        private void 退出ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.ExitThread();
        }
    }
}
